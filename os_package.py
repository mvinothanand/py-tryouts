import os
import csv
import datetime
import json

YYYYMMDD = datetime.date.today().strftime("%Y%m%d")
fieldnames = ["YYYYMMDD","release_date","title","CBFC_rating","original_lang","tags","image_name","poster_message","tag_line","release","update_tci_db"]

def check_continue(prompt="Do you want to continue (y/n)?: "):
  while True:
    response = input(prompt).strip().lower()
    if response in ["y","n"]:
      return True if response == "y" else False
    else:
      print("Invalid response.")

def get_movie_name():
  while True:
    movie_name = input("Enter the movie name: ").strip()
    if len(movie_name) > 0:
      return movie_name
  else:
    print("Invalid movie name")


def get_poster_message():
  poster_message = ""
  while True:
    poster_message = input("Provide the poster message: ").strip()
    if not poster_message:
      print("Invalid message")
      continue
    else:
      break
  return poster_message


def get_release_status():
  release = ""
  while True:
    release_input = input("Provide release status: (a- already, t - today, c -coming soon)? ").strip()
    if release_input not in ['a', 't', 'c']:
      print("Invalid input.")
      continue
    else:
      match release_input:
        case 'a':
          release = "already"
        case 't':
          release = "today"
        case 'c':
          release = "coming_soon"
        case _:
          release = "a"
      break
  return release


def get_db_update_option():
  while True:
    user_response = input("Should this record be updated to db? (y/n) ").strip().lower()
    if user_response in ["y", "n"]:
      return "yes" if user_response == "y" else "no"
    else:  
      print("Invalid input.")


def get_user_response(prompt="Response: "):
  return input(prompt).strip()


def get_matched_content(input_file, search_string):
  #print(f"Searching {input_file} for {search_string}...")
  with open (input_file, "r") as file:
    for line in file:
      if search_string.lower() in line.lower():
        #print("Match found")
        return line
  return None


def check_valid_image_extn(input_file):
  return input_file.strip().split(".")[1] in ["jpeg", "jpg", "png"]


def map_to_dict(input_csv_string):
  mapped_dict = csv.DictReader([input_csv_string],fieldnames=fieldnames)
  return next(mapped_dict)


def create_new_entry(image_name, existing_details=None):
  global YYYYMMDD 
  # get the poster message from user
  poster_message = get_poster_message()
  # get the release status from user
  release = get_release_status()
  # get if the details to be updated to the tci db
  update_tci_db = get_db_update_option()
  
  return {
    "YYYYMMDD": YYYYMMDD,
    "release_date": existing_details["release_date"] if existing_details else get_user_response("Enter the release date in dd-mmm-yyyy: "),
    "title": existing_details["title"] if existing_details else get_user_response("Enter the title: "),
    "CBFC_rating": existing_details["CBFC_rating"] if existing_details else get_user_response("Enter the CBFC Rating: "),
    "original_lang": existing_details["original_lang"] if existing_details else get_user_response("Original language: "),
    "tags": existing_details["tags"] if existing_details else get_user_response("Tags: "),
    "image_name": image_name,
    "poster_message": poster_message,
    "tag_line": existing_details["tag_line"] if existing_details else get_user_response("Tag Line: "),
    "release": release,
    "update_tci_db": update_tci_db
  }


def write_new_entry(new_entry, target_file):
  global fieldnames
  #record = f'{new_entry["YYYYMMDD"]},{new_entry["release_date"]},{new_entry["title"]},{new_entry["CBFC_rating"]},{new_entry["original_lang"]},{new_entry["tags"]},{new_entry["image_name"]},{new_entry["poster_message"]},{new_entry["tag_line"]},{new_entry["release"]},{new_entry["update_tci_db"]}'
  with open(target_file, "a") as file:
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writerow(new_entry)
  return True

def main():
  global fieldnames
  img_folder="/home/vinoth/Documents/tci/posters/wget-downloads/20230728/"
  lookup_data_folder = "/home/vinoth/git-repositories/tci-data/data/daily/"
  new_file = "/home/vinoth/git-repositories/tci-data/data/daily/20230728-dummy.csv"
  results_file = "./results.json"
  with open(new_file, "w") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

  results = []
  
  # get the list of files in the target_folder path
  with os.scandir(img_folder) as images:
    img_folder_contents = list(images)

  lookup_folder_contents = sorted(os.listdir(lookup_data_folder), reverse=True)

  img_files = list(filter(lambda item : check_valid_image_extn(item.name), img_folder_contents))
  if len(img_files) > 0:
    print(f"{len(img_files)} images found.")
  else:
    print("No images found. Exiting.")
    return
  
  if not check_continue():
    return

  counter = 1   
  for entry in sorted(img_files, key=lambda file: file.name):
    process_item = {}
    print(f"#{counter} {entry.name} {entry.stat().st_size}")
    movie_name = get_movie_name()
    
    process_item["image_name"] = entry.name
    process_item["title"] = movie_name

    for lookup_folder_entry in lookup_folder_contents:        
      if lookup_folder_entry.endswith(".csv"):
        existing_entry = get_matched_content(f"{lookup_data_folder}{lookup_folder_entry}", movie_name)
        
        if existing_entry:
          print(f"found an entry for {movie_name}: {existing_entry}")            
          if check_continue("Is the match ok (y/n)?: "):
            prev_entry = map_to_dict(existing_entry)
            new_entry = create_new_entry(entry.name, prev_entry)
            process_item["status"] = "Created new record."
            break

    if not existing_entry:
      print(f"entry not found for {movie_name}")
      prev_entry = {}
      
      if check_continue("Do you want to provide the details (y/n)? "):
        new_entry = create_new_entry(entry.name)
        process_item["status"] = "Created new record."
      else:
        new_entry = {}
        process_item["status"] = "Skipped"
    
    process_item["prev_entry"] = prev_entry
    process_item["new_entry"] = new_entry
    results.append(process_item)
    write_new_entry(new_entry, new_file)

    counter += 1
  
  #print(json.dumps(results, indent=2,ensure_ascii=False))
  with open(results_file, "w") as file:
    file.write(json.dumps(results, indent=2,ensure_ascii=False))
  # ask the movie name from user
  # if found show the data and ask for confirmation from user
  # if the user wants to change accept the new input
  # write the data to a new 


def test():
  src_path = "/home/vinoth/20230222.lst"
  dest_path = "/home/vinoth/Documents/temp/20230222.lst"
  os.rename(src_path, dest_path)


if __name__ == "__main__":
  #main()
  test()

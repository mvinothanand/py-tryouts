#import python native packages
import datetime
import re
import requests
import sys

from pymongo import MongoClient
from bson import ObjectId
from colorama import Fore, Style

#import functions needed from my common package
from common import (
  csvToList
)


# import configurations
from config import (
  INPUT_FILE_PATH,
  CONN_STRING,
  DB_NAME,
  TCI_MOVIES_API
)

# Create mongodb client
def connect_to_mongo_db(conn_string):
  #Client = MongoClient("mongodb+srv://tci-dev-admin:tcidevadmin123@tci-dev.npdhenm.mongodb.net/")
  return MongoClient(conn_string)


def search_db(db, collection_name, query, project_fields = {"_id": 0}, sort_order = {}):
  return list(db[collection_name].find(query, project_fields))


def add_movie(movie):
  url = TCI_MOVIES_API["add_api_end_point"]
  res = requests.post(url, data = movie)
  res_json = res.json()
  message = res_json["message"]
  text_color = f"{Fore.GREEN}" if message["status"] == "SUCCESS" else f"{Fore.RED}" 
  print(f"{text_color}{message['text']}")
  if message["status"] == "FAILURE":
    print(f"{res_json['errors']}")



def get_content_id(title, yor):
  title_cleaned = re.sub(r"[^a-zA-Z0-9 ]", "", title.strip().lower())
  words = title_cleaned.split(" ")
  num_of_words = len(words)

  if num_of_words == 1:
    return f"{words[0]}{yor}"

  content_id = ""  
  for i, word in zip(range(num_of_words), words):
    if i+1 < num_of_words:
      content_id = content_id + word[0]
    else:
      content_id = content_id + word
  return f"{content_id}{yor}"
    

def main():
  # Create db connection
  Client = connect_to_mongo_db(CONN_STRING)
  db = Client[DB_NAME]

  # initialize variables
  YYYYMMDD = datetime.date.today().strftime("%Y%m%d")
  #print(YYYYMMDD)

  # get the daily file data to dict
  input_file_name = f"{INPUT_FILE_PATH}{YYYYMMDD}.csv"
  #input_file_name = f"{INPUT_FILE_PATH}20230827.csv"
  print(input_file_name)
  data = list(filter(lambda item: item["update_tci_db"] == "yes", csvToList(input_file_name)))
  #data = csvToList(input_file_name)
  #print("New items today: ", [item["title"] for item in data ])

  # Loop through the list
  for item in data:
    title = item["title"].upper()
    release_date_str = item["release_date"].strip()
    print(f"{Fore.CYAN}{Style.BRIGHT}\nTitle: {title}, Release date: {release_date_str}")
    release_date = datetime.datetime.strptime(release_date_str, "%d-%b-%Y") if release_date_str else ""
    #print(release_date)
    # Get the release year
    yor = release_date.year if release_date_str else datetime.date.today().year

    release_date_yyyymmdd = release_date.strftime("%Y-%m-%d") if release_date else ""
    release_status = "RELEASED" if item["release"] in ["already", "today"] else "COMING SOON"

    movie = {
            "contentType": "FEATURE_FILM",
            "cbfcCertificate": item['CBFC_rating'].replace("/", ""),
            "releaseMedium": "THEATRICAL", 
            "title": title, 
            "yearOfRelease": yor, 
            #"dateOfRelease": f"{release_date.year}-{release_date.month}-{release_date.day}",
            "dateOfRelease": release_date_yyyymmdd,
            "originalLang": item['original_lang'],
            "titleVariations": [title],
            "contentId": get_content_id(title, yor),
            "status": release_status
        }

    #print(movie)
    #sys.exit()
    # Check item is already in the db
    query = {}
    query["title"] = title
    if yor:
      query["yearOfRelease"] = yor

    matches = search_db(db, "MOVIES", query, {"title": 1, "yearOfRelease": 1, "dateOfRelease": 1, "originalLang": 1, "_id": 0})
    #matches = list(db.MOVIES.find (query, {"title": 1, "yearOfRelease": 1, "dateOfRelease": 1, "originalLang": 1, "_id": 0}))
    
    # if not present, add the record
    if len(matches) == 0:
      print(f"No match found for {title}. Adding the record.")
      add_movie(movie)
      #result = insert_one(db, "MOVIES", movie)
      # if result.inserted_id:
      #   print(f"{Fore.GREEN}{title} added successfully to db with id: {result.inserted_id}")
      # else:
      #   print(f"{Fore.RED}{title} - Update to DB failed.")
    # if more than one match skip and report for manual intervention
    elif len(matches) > 1:
      print(f"{Fore.RED}More than one match found for {title}. Skipping.")
      continue
    # if already present, update the record with the additional details
    else:
      print(f"{Fore.GREEN}Match found")
      print(matches)
      
  
  # Close the db connection
  Client.close()
  
  # Save the result to a json file



if __name__ == "__main__":
  main()
  #print(get_content_id("3.6.9", 2023))
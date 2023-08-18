# import csv module
import csv

# take the input file name and full path
input_file = "/home/vinoth/git-repositories/tci-data/data/streaming-data/20230731.csv"
output_file = "/home/vinoth/git-repositories/tci-data/data/streaming-data/2023-netflix-tamil.csv"

# read the records one by one to a dictionary
with open (output_file, "w") as out_file:
  writer = csv.DictWriter(out_file, ["title","netflix_id","release_type","content_type"])
  writer.writeheader()
  with open (input_file, "r") as file:
    reader = csv.DictReader(file)
    for record in reader:
      print (record["title"])
      if record["streaming_on"] == "netflix":
        writer.writerow({"title": record["title"], "netflix_id": record["streaming_url"].split("/")[-1], "release_type": record["release_type"], "content_type": record["content_type"]})

# write only the required fields to a new file
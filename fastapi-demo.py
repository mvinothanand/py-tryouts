import contextlib
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

app = FastAPI()
Client = MongoClient("mongodb+srv://tci-dev-admin:tcidevadmin123@tci-dev.npdhenm.mongodb.net/")
db = Client["tci-tryouts"]

@app.get("/movies")
def get_movies(sort_by: str = "date", yor: str = None):
  # sort by date in descending
  if sort_by == "date":
    sort_field = "dateOfRelease"
    sort_order = -1

 # sort by title in ascending
  if sort_by == "title":
    sort_field = "title"
    sort_order = 1

  # form the query
  #query = {"yearOfRelease": 2023}
  query = {}
  print(f"yor: {yor}")
  if yor:
    query["yearOfRelease"] = int(yor)

  movies = db.MOVIES.find(query, {"title": 1, "yearOfRelease": 1, "dateOfRelease": 1, "originalLang": 1, "_id": 0}).sort(sort_field, sort_order)
  return list(movies)
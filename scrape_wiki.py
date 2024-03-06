from bs4 import BeautifulSoup
import requests


url = "https://en.wikipedia.org/wiki/List_of_Tamil_films_of_2023"


def get_html_document(url):
  response = requests.get(url)
  return response.text

def main():
  #html_doc = get_html_document(url)
  html_doc = "tamil_movies_2023.html"

  with open (html_doc, "r") as fp:
    content = fp.read()
    soup = BeautifulSoup(content, "html5lib")

  data_tables = soup.find_all("table", class_ = "wikitable sortable jquery-tablesorter")
  print(len(data_tables))

if __name__ == "__main__":
  main()


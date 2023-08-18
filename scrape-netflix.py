from bs4 import BeautifulSoup

input_html = "/home/vinoth/Documents/temp/netflix.html"

with open(input_html, "r") as input_file:
  content = input_file.read()
  soup = BeautifulSoup(content,"html5lib")
  #print(html_content)
  #print(soup.prettify())
  
title_cards = soup.find_all("div", class_ = "ptrack-content")
for tag in title_cards:
  for child in tag.children:
    netflix_id = child["href"].split("/")[2].split("?")[0]
    movie_title = child.find("p", class_ = "fallback-text").text
    print (f"{movie_title},{netflix_id}")

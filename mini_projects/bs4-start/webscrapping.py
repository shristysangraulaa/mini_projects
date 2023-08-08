from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")
a_findtitle = soup.find_all("h3",attrs={"class" : "title"})
movie_list= []
for word in a_findtitle:
    movie_list.append(word.text)

for item in reversed(movie_list):
    print(item)

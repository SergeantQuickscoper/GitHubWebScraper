import requests
from bs4 import BeautifulSoup as bs

username = input("Enter a valid GitHub User: ")
website = "https://github.com/"
finalURL = website + username

r = requests.get(finalURL)

soup = bs(r.content, "html.parser")

profile_image = soup.find('img', class_ = "avatar avatar-user width-full border color-bg-default")["src"]

print(profile_image)
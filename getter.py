import requests
from bs4 import BeautifulSoup as bs

username = input("Enter a valid GitHub User: ")
website = "https://github.com/"
finalURL = website + username

r = requests.get(finalURL)
r.encoding = r.apparent_encoding
content = r.text
r.raise_for_status()

soup = bs(content, "html.parser")

profile_image = soup.find('img', class_ = "avatar avatar-user width-full border color-bg-default")["src"]

name = soup.find('span', {"itemprop" : "name"}).get_text()

followersArray = soup.find_all("span", class_ = "text-bold color-fg-default")
followers, following = followersArray
followers = followers.string
following = following.string

print("Name: " + name)
print("Profile Picture: " + profile_image)
print("Followers: " + followers)
print("Following: " + following)

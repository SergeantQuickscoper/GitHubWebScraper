import requests
from bs4 import BeautifulSoup as bs

def getData():
    profile_image = soup.find('img', class_ = "avatar avatar-user width-full border color-bg-default")["src"]
    name = soup.find('span', {"itemprop" : "name"}).get_text()
    followersArray = soup.find_all("span", class_ = "text-bold color-fg-default")
    followers, following = followersArray
    followers = followers.string
    following = following.string
    contributions = soup.find('h2', class_ = "f4 text-normal mb-2").string
    return name, profile_image, followers, following, contributions

def Intro():
    print("Github Scraper by Don Chacko. To get started fill in the given info:\n")

def PrintInfo():
    nameToPrint, profileImageToPrint, followersToPrint, followingToPrint, contributionsToPrint = getData()

    print("Name: " + nameToPrint)
    print("Profile Picture: " + profileImageToPrint)
    print("Followers: " + followersToPrint)
    print("Following: " + followingToPrint)
    print("This user has " + contributionsToPrint)


Intro()
username = input("Enter a valid GitHub User: ")
website = "https://github.com/"
finalURL = website + username

r = requests.get(finalURL)
r.encoding = r.apparent_encoding
content = r.text
r.raise_for_status()
soup = bs(content, "html.parser")

PrintInfo()


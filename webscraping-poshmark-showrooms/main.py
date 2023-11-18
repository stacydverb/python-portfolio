from bs4 import BeautifulSoup
import requests

with open("showrooms.txt", "a") as m:

    response = requests.get("https://poshmark.com/brands")
    website_data = response.text

    soup = BeautifulSoup(website_data, "html.parser")

    showrooms = soup.find_all("a", attrs={"class": "", "data-et-name": "showrooms"})
    print(showrooms)

    for name in showrooms:
        showroom_name = name.getText()
        m.write(f"{showroom_name}")


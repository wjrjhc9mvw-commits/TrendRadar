import requests
from bs4 import BeautifulSoup

url = "https://tophub.today/n/J0b0vmloB1G"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

titles = soup.select(".cc-cd .t")[0:10]

with open("email.txt", "a", encoding="utf8") as f:
    for i, t in enumerate(titles, start=1):
        text = t.get_text(strip=True)
        link = t["href"]
        if not link.startswith("http"):
            link = "https://tophub.today" + link
        f.write(f"{i}. {text}\n{link}\n\n")

import requests
from bs4 import BeautifulSoup


def scrape_website(url):

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title Found"

        meta_description = ""

        meta = soup.find("meta", attrs={"name": "description"})

        if meta:
            meta_description = meta.get("content")

        paragraphs = soup.find_all("p")

        content = " ".join([p.get_text() for p in paragraphs[:10]])

        return {
            "title": title,
            "description": meta_description,
            "content": content
        }

    except Exception as e:

        return {
            "error": str(e)
        }
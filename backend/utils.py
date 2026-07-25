import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from backend.config import REQUEST_TIMEOUT, USER_AGENT

def validate_url(url):
    try:
        result = urlparse(url)
        return result.scheme in ("http", "https") and bool(result.netloc)
    except Exception:
        return False

def fetch_page(url):

    headers = {
        "User-Agent": USER_AGENT
    }

    start = time.time()

    response = requests.get(
        url,
        headers = headers,
        timeout = REQUEST_TIMEOUT
    )
    end = time.time()

    response_time = round(end - start, 3)
    return response, response_time

def parse_html(html):
    return BeautifulSoup(html, "lxml")

def extract_title(soup):

    if soup.title:
        return soup.title.get_text(strip=True)

    return "No Title Found"

def extract_meta_description(soup):

    meta = soup.find("meta", attrs = {"name": "description"})

    if meta and meta.get("content"):
        return meta["content"]
    return "No Meta Description"

def count_h1(soup):
    return len(soup.find_all("h1"))

def count_missing_alt(soup):

    images = soup.find_all("img")

    missing = 0

    for image in images:
        alt = image.get("alt")

        if alt is None or alt.strip() == "":
            missing +=1
    return missing

def count_words(soup):

    text = soup.get_text(separator=" ", strip= True)

    words = text.split()

    return len(words)
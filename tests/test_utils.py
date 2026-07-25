from bs4 import BeautifulSoup
from backend.utils import (
    extract_title,
    extract_meta_description,
    count_h1
)


def test_extract_title():
    html = "<html><head><title>Page Pulse</title></head></html>"
    soup = BeautifulSoup(html, "html.parser")

    assert extract_title(soup) == "Page Pulse"


def test_missing_meta_description():
    html = "<html><head></head></html>"
    soup = BeautifulSoup(html, "html.parser")

    assert extract_meta_description(soup) == "Not Found"


def test_no_h1():
    html = "<html><body><p>Hello World</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")

    assert count_h1(soup) == 0

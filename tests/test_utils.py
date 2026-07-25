import sys
import os

# Add backend folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "backend")
    )
)

from bs4 import BeautifulSoup
from utils import (
    extract_title,
    extract_meta_description,
    count_h1,
    count_missing_alt
)


def test_extract_title():
    html = "<html><head><title>Page Pulse</title></head></html>"
    soup = BeautifulSoup(html, "html.parser")

    assert extract_title(soup) == "Page Pulse"


def test_missing_meta_description():
    html = "<html><head></head></html>"
    soup = BeautifulSoup(html, "html.parser")

    assert extract_meta_description(soup) == "No Meta Description"


def test_no_h1():
    html = "<html><body><p>Hello World</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")

    assert count_h1(soup) == 0

def test_missing_alt_images():
    html = """
    <html>
        <body>
            <img src="a.jpg">
            <img src="b.jpg" alt="Image">
            <img src="c.jpg" alt="">
        </body>
    </html>
    """

    soup = BeautifulSoup(html, "html.parser")

    assert count_missing_alt(soup) == 2

import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.vatican.va/archive/ENG0015/"

def get_catechism_links():
    """Get all internal links from the Catechism index."""
    index_url = BASE_URL + "_INDEX.HTM"
    response = requests.get(index_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']
        if href.endswith(".HTM") and not href.startswith("_"):
            full_url = BASE_URL + href
            links.append(full_url)

    return links

def scrape_catechism():
    """Scrape all text from the Catechism."""
    all_text = ""
    links = get_catechism_links()
    print(f"Found {len(links)} links")

    for link in links:
        page = requests.get(link)
        page_soup = BeautifulSoup(page.content, "html.parser")

        # Remove scripts and styles
        for script in page_soup(["script", "style"]):
            script.decompose()

        text = page_soup.get_text(separator="\n")
        all_text += text + "\n\n"

        time.sleep(0.3)  # polite delay

    return all_text

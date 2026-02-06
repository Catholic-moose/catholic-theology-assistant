import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.vatican.va/archive/ENG0015/"

def get_catechism_links():
    """Get all internal links from the Catechism index."""
    index_url = BASE_URL + "_INDEX.HTM"
    response = requests.get(index_url)
    if response.status_code != 200:
        raise Exception(f"Failed to load index page: {response.status_code}")
    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    # Find all links to .HTM files that are not starting with "_"
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
        if page.status_code != 200:
            print(f"Warning: failed to load {link}")
            continue
        page_soup = BeautifulSoup(page.content, "html.parser")

        # Remove scripts, styles, and navigation elements
        for tag in page_soup(["script", "style", "nav"]):
            tag.decompose()

        # Extract text
        text = page_soup.get_text(separator="\n")
        text = text.strip()
        if text:
            all_text += text + "\n\n"

        time.sleep(0.2)  # polite delay

    if not all_text:
        print("Warning: no text was scraped!")
    return all_text

import requests
from bs4 import BeautifulSoup
import random
import time
import pandas as pd
from requests.adapters import HTTPAdapter, Retry

# -------------------------------
# ROTATING USER AGENTS
# -------------------------------
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
]

def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9",
    }


# -------------------------------
# SESSION WITH RETRIES
# -------------------------------
def create_session():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session

session = create_session()


# -------------------------------
# FETCH PAGE (with error-handling)
# -------------------------------
def fetch_page(url):
    try:
        response = session.get(url, headers=get_headers(), timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print("❌ Error fetching page:", e)
        return None


# -------------------------------
# PARSE PRICE SAFELY
# -------------------------------
def parse_price(price_text):
    if not price_text:
        return None
    cleaned = "".join(ch for ch in price_text if ch.isdigit() or ch in ".,")
    cleaned = cleaned.replace(",", "")
    try:
        return float(cleaned)
    except:
        return None


# -------------------------------
# PARSE A SINGLE PRODUCT TILE
# -------------------------------
def parse_product(item):
    try:
        title_elem = item.select_one("h2 a span")
        title = title_elem.get_text(strip=True) if title_elem else ""

        price_elem = item.select_one(".a-price .a-offscreen")
        price = parse_price(price_elem.get_text(strip=True)) if price_elem else None

        rating_elem = item.select_one(".a-icon-alt")
        rating = rating_elem.get_text(strip=True).split()[0] if rating_elem else None

        reviews_elem = item.select_one(".a-size-base.s-underline-text")
        reviews = reviews_elem.get_text(strip=True).replace(",", "") if reviews_elem else None

        link_elem = item.select_one("h2 a")
        link = "https://www.amazon.in" + link_elem["href"] if link_elem else ""

        return {
            "title": title,
            "price": price,
            "rating": rating,
            "reviews": reviews,
            "link": link
        }
    except Exception as e:
        print("⚠ Error parsing product:", e)
        return None


# -------------------------------
# SCRAPE MULTIPLE AMAZON SEARCH PAGES
# -------------------------------
def scrape_amazon_search(keyword="black friday sale", pages=3):
    base_url = "https://www.amazon.in/ref=nav_logo"
    all_products = []

    for page in range(1, pages + 1):
        print(f"\n🔍 Scraping Page {page}...")

        url = f"{base_url}{keyword}&page={page}"
        soup = fetch_page(url)
        if soup is None:
            continue

        items = soup.select("div.s-result-item[data-component-type='s-search-result']")
        print(f"➡ Found {len(items)} items")

        for item in items:
            product = parse_product(item)
            if product and product["title"]:
                all_products.append(product)

        # Random sleep to avoid blocking
        delay = random.uniform(2.5, 6.5)
        print(f"⏳ Sleeping {delay:.1f} seconds...")
        time.sleep(delay)

    return all_products


# -------------------------------
# RUN SCRAPER
# -------------------------------
if __name__ == "__main__":
    keyword = "laptop"
    products = scrape_amazon_search(keyword, pages=2)

    if products:
        df = pd.DataFrame(products)
        df.to_excel("amazon_scraped_products.xlsx", index=False)
        print("\n🎉 Saved to amazon_scraped_products.xlsx")
    else:
        print("⚠ No products scraped (Amazon may be blocking requests).")

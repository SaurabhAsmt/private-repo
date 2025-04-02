from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Configure Selenium to use headless Chrome
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Base URL handling pagination
def get_page_html(page_number):
    url = "https://boodmo.com/catalog/4033-time_belt/" if page_number == 1 else f"https://boodmo.com/catalog/4033-time_belt/page-{page_number}/"
    driver.get(url)
    # Wait for the JavaScript to load (adjust sleep as necessary or use explicit waits)
    time.sleep(5)
    return driver.page_source

# Function to scrape a single page
def scrape_page(page_number):
    html = get_page_html(page_number)
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all("div", class_="product-item-tile")
    print(f"Found {len(products)} product items on page {page_number}")

    scraped_data = []
    for product in products:
        name_tag = product.find("span", class_="product-item-tile__title")
        price_tag = product.find("span", class_="product-item-tile__price__current")
        part_no_tag = product.find("span", class_="product-item-tile__desc__number")

        scraped_data.append({
            "name": name_tag.get_text(strip=True) if name_tag else "N/A",
            "price": price_tag.get_text(strip=True) if price_tag else "N/A",
            "part_number": part_no_tag.get_text(strip=True) if part_no_tag else "N/A",
        })
    return scraped_data

all_data = []
# Scrape pages 1 through 10
for page in range(1, 11):
    print(f"Scraping page {page}...")
    page_data = scrape_page(page)
    print(f"Scraped {len(page_data)} items from page {page}")
    all_data.extend(page_data)

# Print collected data
for item in all_data:
    print(item)

driver.quit()



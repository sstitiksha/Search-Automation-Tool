from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def google_search(query: str):
    query = query.replace(" ", "+")

    options = Options()
    options.add_argument("--start-maximized")

    service = Service()  # assumes chromedriver is in PATH
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://www.google.com/search?q={query}"
    driver.get(url)

    time.sleep(5)
    return driver

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python google_search.py <search query>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    google_search(query)

#selenium>=4.15.0

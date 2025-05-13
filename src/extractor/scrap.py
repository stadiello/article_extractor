import requests
from bs4 import BeautifulSoup
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Scraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
        self.options = webdriver.ChromeOptions()
    
    def scrapeSiteMap(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print("Erreur de chargement:", response.status_code)
            exit()

        # Parsing XML
        soup = BeautifulSoup(response.content, "xml")

        # Extraction des liens <loc>
        links = [loc.text for loc in soup.find_all("loc")]
        print(f"{len(links)} liens trouvés.")

        # Sauvegarde dans CSV
        with open("data/extracted.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Lien"])
            for link in links:
                writer.writerow([link])

        print(f"{len(links)} liens enregistrés dans 'extracted.csv'")
    
    def scrapUrl(self, url):
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        try:
            driver.get(url)
            body = driver.find_element(By.TAG_NAME, "body")
            paragraphs = body.find_elements(By.TAG_NAME, "p")
            text = " ".join(p.text for p in paragraphs if p.text.strip() != "")
            return text
        finally:
            driver.quit()
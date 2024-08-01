import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebCrawler:
    def __init__(self, base_url, session=None):
        self.base_url = base_url
        self.visited_urls = set()
        self.found_forms = []
        self.session = session or requests.Session()

    def crawl(self, url=None):
        if url is None:
            url = self.base_url

        if url in self.visited_urls:
            return

        self.visited_urls.add(url)
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'lxml')

            # Find and store all forms
            self.found_forms += self.extract_forms(url, soup)

            # Find and visit all links
            for link in soup.find_all('a', href=True):
                new_url = urljoin(self.base_url, link['href'])
                if new_url not in self.visited_urls and self.base_url in new_url:
                    self.crawl(new_url)

        except requests.exceptions.RequestException as e:
            print(f"Error crawling {url}: {e}")

    def extract_forms(self, url, soup):
        forms = soup.find_all('form')
        return [(url, form) for form in forms]

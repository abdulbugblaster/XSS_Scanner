import argparse
from crawler import WebCrawler
from detector import XSSDetector
from authenticator import Authenticator
from utils import load_payloads

def main():
    parser = argparse.ArgumentParser(description="Advanced XSS Scanner")
    parser.add_argument('--url', required=True, help='Target URL')
    parser.add_argument('--login-url', help='Login URL if authentication is needed')
    parser.add_argument('--login-data', help='Login data in key=value&key2=value2 format')
    parser.add_argument('--payloads', default='payloads.txt', help='File containing XSS payloads')

    args = parser.parse_args()

    payloads = load_payloads(args.payloads)
    if not payloads:
        print("No payloads loaded, exiting.")
        return

    # Authentication handling if needed
    session = None
    if args.login_url and args.login_data:
        login_data = dict(item.split("=") for item in args.login_data.split("&"))
        authenticator = Authenticator(args.login_url, login_data)
        authenticator.authenticate()
        session = authenticator.get_session()

    # Initialize the crawler
    crawler = WebCrawler(args.url, session=session)

    # Start crawling
    crawler.crawl()

    # XSS Payload Injection
    detector = XSSDetector(payloads)

    # Detect XSS
    for url, form in crawler.found_forms:
        if detector.test_xss(url, form, session=session):
            with open('reports/xss_report.txt', 'a') as report:
                report.write(f"XSS vulnerability found at {url}\n")
            print(f"XSS vulnerability found at {url}")

if __name__ == "__main__":
    main()

import requests
from urllib.parse import urljoin

class XSSDetector:
    def __init__(self, payloads):
        self.payloads = payloads

    def test_xss(self, url, form, session=None):
        session = session or requests.Session()
        action = form.get('action')
        method = form.get('method', 'get').lower()
        inputs = form.find_all(['input', 'textarea'])

        for payload in self.payloads:
            form_data = {}
            for input in inputs:
                name = input.get('name')
                if input.get('type') == 'text':
                    form_data[name] = payload
                else:
                    form_data[name] = input.get('value', '')

            try:
                target_url = urljoin(url, action)
                if method == 'post':
                    response = session.post(target_url, data=form_data)
                else:
                    response = session.get(target_url, params=form_data)

                if self.check_response(payload, response):
                    return True

            except requests.exceptions.RequestException as e:
                print(f"Error testing XSS on {target_url}: {e}")
                continue

        return False

    def check_response(self, payload, response):
        content_type = response.headers.get('Content-Type', '').lower()
        if 'json' in content_type:
            return any(payload in value for value in response.json().values())
        elif 'xml' in content_type:
            return payload in response.content.decode()
        else:
            return payload in response.text

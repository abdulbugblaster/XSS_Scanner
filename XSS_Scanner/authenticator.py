import requests

class Authenticator:
    def __init__(self, login_url, login_data):
        self.session = requests.Session()
        self.login_url = login_url
        self.login_data = login_data

    def authenticate(self):
        try:
            response = self.session.post(self.login_url, data=self.login_data)
            response.raise_for_status()
            print("Authentication successful")
        except requests.exceptions.RequestException as e:
            print(f"Authentication failed: {e}")

    def get_session(self):
        return self.session

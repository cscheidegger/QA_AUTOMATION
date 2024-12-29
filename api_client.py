import requests

BASE_URL = "https://demoqa.com"  # Endereço base das APIs


class APIClient:
    def __init__(self):
        self.session = requests.Session()  # Reutiliza conexões para maior eficiência

    def create_user(self, username, password):
        url = f"{BASE_URL}/Account/v1/User"
        payload = {"userName": username, "password": password}
        response = self.session.post(url, json=payload)
        return response.json()

    def generate_token(self, username, password):
        url = f"{BASE_URL}/Account/v1/GenerateToken"
        payload = {"userName": username, "password": password}
        response = self.session.post(url, json=payload)
        return response.json()

    def authorize_user(self, username, token):
        url = f"{BASE_URL}/Account/v1/Authorized"
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"userName": username}
        response = self.session.post(url, json=payload, headers=headers)
        return response.status_code == 200

    def list_books(self):
        url = f"{BASE_URL}/BookStore/v1/Books"
        response = self.session.get(url)
        return response.json()["books"]

    def reserve_books(self, user_id, token, books):
        url = f"{BASE_URL}/BookStore/v1/Books"
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"userId": user_id, "collectionOfIsbns": [{"isbn": book} for book in books]}
        response = self.session.post(url, json=payload, headers=headers)
        return response.json()

    def get_user_details(self, user_id, token):
        url = f"{BASE_URL}/Account/v1/User/{user_id}"
        headers = {"Authorization": f"Bearer {token}"}
        response = self.session.get(url, headers=headers)
        return response.json()

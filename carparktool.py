import requests

ENDPOINT_URL = "https://blackmarketcpm.onrender.com/api"

class CPMNuker:
    def _init_(self):
        self.auth_token = None

    def login(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        response = requests.post(f"{ENDPOINT_URL}/account_login", data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")

    def register(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        response = requests.post(f"{ENDPOINT_URL}/account_register", data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")

    def delete(self):
        if self.auth_token is None:
            return False
        payload = {"account_auth": self.auth_token}
        response = requests.post(f"{ENDPOINT_URL}/account_delete", data=payload)
        return response.json().get("ok", False)

    def get_player_data(self) -> dict:
        if self.auth_token is None:
            return {}
        payload = {"account_auth": self.auth_token}
        response = requests.post(f"{ENDPOINT_URL}/get_data", data=payload)
        return response.json()

    def set_player_rank(self) -> bool:
        if self.auth_token is None:
            return False
        payload = {"account_auth": self.auth_token}
        response = requests.post(f"{ENDPOINT_URL}/set_rank", data=payload)
        return response.json().get("ok", False)

    def get_key_data(self) -> dict:
        response = requests.get(f"{ENDPOINT_URL}/get_key_data")
        return response.json()

    def set_player_money(self, amount) -> bool:
        if self.auth_token is None:
            return False
        payload = {"account_auth": self.auth_token, "amount": amount}
        response = requests.post(f"{ENDPOINT_URL}/set_money", data=payload)
        return response.json().get("ok", False)

    def set_player_coins(self, amount) -> bool:
        if self.auth_token is None:
            return False
        payload = {"account_auth": self.auth_token, "amount": amount}
        response = requests.post(f"{ENDPOINT_URL}/set_coins", data=payload)
        return response.json().get("ok", False)

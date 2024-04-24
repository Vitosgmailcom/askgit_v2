
class Payloads:
    def not_existing_user(self):
        payload = {
            "email": "jon.snow@gameofthrones.com",
            "password": "GameOfThrones"
        }
        return payload

    def admin_user(self):
        pass
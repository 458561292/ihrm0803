import app


class UserLogin:
    def __init__(self):
        self.login_url = app.BASE_URL + "login"

    def login(self, session, mobile, password):
        myLoginJson = {"mobile": mobile, "password": password}
        response = session.post(self.login_url, json=myLoginJson)
        token = response.json().get("data")
        app.TOKEN = token
        return session.post(self.login_url, json=myLoginJson)

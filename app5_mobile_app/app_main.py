"""Mobile app using kivy library
"""

from datetime import datetime
import os
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


USER_DB = "user_db.json"

class RootWidget(ScreenManager):
    pass


class LoginScreen(Screen):
    def sign_up(self):
        """Sign up button press callback
        """
        self.manager.current = "sign_up_screen"


class SignUpScreen(Screen):
    def new_account(self, uname, pwd):
        """ Create a new account

        Parameters
        ----------
        uname : the username

        pwd : the password

        """
        users = dict()
        with open(USER_DB) as db_file:
            db_file.seek(0)
            if db_file.read(1):
                users = json.load(db_file)

        users[uname] = {'username': uname,
                        'password': pwd,
                        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open(USER_DB, 'w') as db_file:
            json.dump(users, db_file)

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    if not os.path.exists(USER_DB):
        with open(USER_DB, "w"):
            pass
    Builder.load_file('AppDesign.kv')
    MainApp().run()

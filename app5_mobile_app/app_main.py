"""Mobile app using kivy library
"""

from datetime import datetime
import os
import json
import glob
from pathlib import Path
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior


USER_DB = "user_db.json"

def get_users():
    users = dict()
    with open(USER_DB) as db_file:
        db_file.seek(0)
        if db_file.read(1):
            db_file.seek(0)
            users = json.load(db_file)
    return users



class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class LoginScreen(Screen):
    def log_in(self, uname, pwd):
        users = get_users()
        if uname in users and users[uname]['password'] == pwd:
            self.manager.current = "app_main_screen"
        else:
            self.ids.login_fail.text = "Wrong username or password"
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
        users = get_users()
        users[uname] = {'username': uname,
                        'password': pwd,
                        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open(USER_DB, 'w') as db_file:
            json.dump(users, db_file)
        self.manager.current = "sign_up_screen_success"



class SignUpScreenSuccess(Screen):
    def show_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"



class AppMainScreen(Screen):
    def enlighten(self, feeling):
        feeling = feeling.lower()
        files = glob.glob("quotes/*txt")
        feelings_available = [Path(filename).stem for filename in files]
        if feeling in feelings_available:
            with open(f"quotes/{feeling}.txt") as quote_file:
                quotes = quote_file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    if not os.path.exists(USER_DB):
        with open(USER_DB, "w"):
            pass
    Builder.load_file('AppDesign.kv')
    MainApp().run()

"""Mobile app using kivy library
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from hoverable import HoverBehavior
import datastore


user_dstore = datastore.UserDataStore()
quotes = datastore.QuotesDataStore()

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class LoginScreen(Screen):
    def log_in(self, uname, pwd):
        if user_dstore.is_user_present(uname, pwd):
            self.ids.usr.text = ""
            self.ids.pwd.text = ""
            self.manager.current = "app_main_screen"
        else:
            self.ids.login_fail.text = "Wrong username or password"
    def sign_up(self):
        """Sign up button press callback
        """
        self.ids.usr.text = ""
        self.ids.pwd.text = ""
        self.manager.current = "sign_up_screen"


class SignUpScreen(Screen):
    def new_account(self, uname, pwd):
        """ Create a new account

        Parameters
        ----------
        uname : the username

        pwd : the password

        """
        user_dstore.add_user(uname, pwd)
        self.ids.usr.txt = ""
        self.ids.pwd.txt = ""
        self.manager.current = "sign_up_screen_success"



class SignUpScreenSuccess(Screen):
    def show_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"



class AppMainScreen(Screen):
    def enlighten(self, feeling):
        if quotes.is_feeling_available(feeling):
            self.ids.quote.text = quotes.get_quote(feeling)
        else:
            self.ids.quote.text = "Try another feeling"
    def log_out(self):
        self.ids.feeling.text = ""
        self.ids.quote.text = ""
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class MainApp(App):
    def build(self):
        return RootWidget()
    def on_stop(self):
        user_dstore.save()


if __name__ == "__main__":
    Builder.load_file('AppDesign.kv')
    MainApp().run()

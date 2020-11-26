"""Mobile app using kivy library
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


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
        print(uname, pwd)


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    Builder.load_file('AppDesign.kv')
    MainApp().run()

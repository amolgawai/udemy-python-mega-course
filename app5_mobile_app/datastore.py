"""Data Store for the app
   Provides User Data Store and Quotes Data Store
"""


from datetime import datetime
import os
import json
import glob
from pathlib import Path
import random


USER_DB = "user_db.json"

class UserDataStore:
    """Provides User Data
    """
    def __init__(self):
        "initialises user data"
        if not os.path.exists(USER_DB):
            with open(USER_DB, "w"):
                pass
        with open(USER_DB) as db_file:
            db_file.seek(0)
            if db_file.read(1):
                db_file.seek(0)
                self.users = json.load(db_file)
            else:
                self.users = dict()

    def save(self):
        "writes to users to file"
        with open(USER_DB, 'w') as db_file:
            json.dump(self.users, db_file)

    def is_user_present(self, uname, pwd):
        """ Checks if the user is present in the data store
        Note - Plain text password handling must not be used in production
        Parameters
        ----------
        uname : name of the user

        pwd : password of the user


        Returns
        -------
        Boolean : True if user is present, False if not

        """
        return uname in self.users and self.users[uname]['password'] == pwd

    def add_user(self, uname, pwd):
        """ Adds a user in the datastore

        Parameters
        ----------
        uname : The user name to add

        pwd : corresponding password

        """
        self.users[uname] = {'username': uname,
                        'password': pwd,
                        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}



class QuotesDataStore:
    """ Provides random quote for a feeling
    """
    def __init__(self):
        """ Initialises the class with quotes
        """
        files = glob.glob("quotes/*txt")
        self.feelings = [Path(filename).stem for filename in files]

    def is_feeling_available(self, feeling):
        """ Checks i the feeling is available to get a quote

        Parameters
        ----------
        feeling : feeling type


        Returns
        -------
        Boolean : True if available, False if not

        """
        feeling = feeling.lower()
        return feeling in self.feelings

    def get_quote(self, feeling):
        """ Gets a random quote for given feeling

        Parameters
        ----------
        feeling : feeling type


        Returns
        -------
        str : a quote string

        """
        with open(f"quotes/{feeling}.txt") as quote_file:
            quotes = quote_file.readlines()
            return random.choice(quotes)

from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_adress_mather=re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_adress_mather.match(email) else False

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: sha512-hashed password form login form
        :return: A sha512->pbkdf_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password the user sent matches that of the databasebase
        The database password is encrypted mor than the users password at this moment.
        :param password: sha512-hashed password
        :param hashed password: pbkdf2_sha512 encrypted password
        :return: True if passwords match
        """
        return pbkdf2_sha512.verify(password, hashed_password)
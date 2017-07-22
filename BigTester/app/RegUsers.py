import re
from sqlrw import (crt_users,
                   get_users,
                   up_del_users
                   )


class RegUsersForm:
    def __init__(self, email: str, username: str, password: str, re_password: str, statusadmin: int):
        self.email = email
        self.username = username
        self.password = password
        self.re_password = re_password
        self.statusadmin = statusadmin
        self.error_forms = {}
        self.sql = "SELECT `email` FROM `Users` WHERE `email`='{}' ".format(self.email)

        if self.password != self.re_password \
                or re.match('<script', self.password) != None \
                or len(self.password) > 10 \
                or len(self.password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_forms.update(password_error)

        if len(self.username) < 4 \
                or len(self.username) > 15 \
                or re.search(r'[!?<:>/]', self.username) != None \
                or re.match('<script', self.username) != None:
            password_error = {
                'username': 'The length of the username must be at least 4 characters and not more than 15'}
            self.error_forms.update(password_error)

        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match('<script', self.email) != None:
            password_error = {
                'email': 'No  correct email '}
            self.error_forms.update(password_error)

        if get_users(self.sql, self.email) == True:
            password_error = {
                'emailbd': 'Such an email is in the database'
            }
            self.error_forms.update(password_error)

    def write_users(self):
        if len(self.error_forms) == 0:
            crt_users(self.username, self.email, self.password, self.statusadmin)
            return print('write to base data')
        else:
            return print('no write to base data', self.error_forms)

    def errors(self):
        return self.error_forms


class UpdateUsersForm:
    def __init__(self, email: str, username: str, old_password: str, new_password: str, re_newpassword: str):
        self.email = email
        self.username = username
        self.old_password = old_password
        self.new_password = new_password
        self.re_newpassword = re_newpassword
        self.error_update = {}
        self.sql = "UPDATE `Users`SET `password` = '{}' WHERE `Users`.`email` = '{}'" \
            .format(self.new_password, self.email)

    def update_users(self):
        up_del_users(self.sql)


class DeleteUsersForm:
    def __init__(self, email: str, password: str, re_password: str):
        self.email = email
        self.password = password
        self.re_password = re_password
        self.error_delete = {}
        self.sql = "DELETE FROM `Users` WHERE `Users`.`email` = '{}'".format(self.email)

    def delete_users(self):
        up_del_users(self.sql)

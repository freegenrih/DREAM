import re
from sqlrw import (crt_users,
                   get_users,
                   up_del_users,
                   get_users_sign_in
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
                or re.match(r'<script', self.username) != None:
            password_error = {
                'username': 'The length of the username must be at least 4 characters and not more than 15'}
            self.error_forms.update(password_error)

        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or self.email.find('@') == -1 \
                or self.email.find('.') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match(r'<script', self.email) != None:
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
        self.error_updates = {}
        self.sql = "UPDATE `Users`SET `password` = '{}' WHERE `Users`.`email` = '{}'" \
            .format(self.new_password, self.email)

        if self.new_password != self.re_newpassword \
                or re.match('<script', self.new_password) != None \
                or re.match('<script', self.re_newpassword) != None \
                or len(self.old_password) > 10 \
                or len(self.old_password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_updates.update(password_error)

        if len(self.username) < 4 \
                or len(self.username) > 15 \
                or re.search(r'[!?<:>/]', self.username) != None \
                or re.match(r'<script', self.username) != None:
            username_error = {
                'username': 'The length of the username must be at least 4 characters and not more than 15'}
            self.error_updates.update(username_error)

        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or self.email.find('@') == -1 \
                or self.email.find('.') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match(r'<script', self.email) != None:
            email_error = {
                'email': 'No  correct email '}
            self.error_updates.update(email_error)

    def update_users(self):
        if len(self.error_updates) == 0:
            up_del_users(self.sql)
            return print('update info to users')
        else:
            return print('no update users to base data', self.error_updates)

    def errors_updates(self):

        return self.error_updates


class DeleteUsersForm:
    def __init__(self, email: str, password: str, re_password: str):
        self.email = email
        self.password = password
        self.re_password = re_password
        self.error_delete = {}
        self.sql = "DELETE FROM `Users` WHERE `Users`.`email` = '{}'".format(self.email)

        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or self.email.find('@') == -1 \
                or self.email.find('.') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match(r'<script', self.email) != None:
            email_error = {
                'email': 'No  correct email '}
            self.error_delete.update(email_error)

        if self.password != self.re_password \
                or re.match('<script', self.password) != None \
                or re.match('<script', self.re_password) != None \
                or len(self.password) > 10 \
                or len(self.password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_delete.update(password_error)

    def delete_users(self):

        up_del_users(self.sql)

    def errors_delete(self):
        print(self.error_delete)
        return self.error_delete


class SignIn:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.error_sign_in = {}
        self.sql = "SELECT `password`, `email` FROM `Users` WHERE `email`='{}'".format(self.email)

        if len(self.email) > 64 \
                or self.email.find('@') == -1 \
                or self.email.find('.') == -1 \
                or len(self.email) == 0 \
                or re.search(r'[!?<:>/]', self.email) != None \
                or re.match(r'<script', self.email) != None:
            email_error = {
                'email': 'No  correct email '}
            self.error_sign_in.update(email_error)

        if re.match('<script', self.password) != None \
                or len(self.password) > 10 \
                or len(self.password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_sign_in.update(password_error)

    def validate(self):
        if get_users_sign_in(self.sql, self.password, self.email) == True:
            return True

        else:
            False

    def error_signin(self):
        return self.error_sign_in


class IPSender:
    def __init__(self, name, key, password):
        self.name = name
        self.key = key
        self.password = password
        self.error_ipsender = {}

        if re.match('<script', self.name) != None \
                or len(self.name) > 20 \
                or len(self.name) < 5:
            name_error = {'name': 'Need Len Name <20 and >5 '}
            self.error_ipsender.update(name_error)


        if re.match('<script', self.password) != None \
                or len(self.password) > 10 \
                or len(self.password) < 5:
            password_error = {'password': 'No confirm password'}
            self.error_ipsender.update(password_error)


    def create_ipsender(self):
        if len(self.error_ipsender) == 0:
            pass
        pass

    def delete_ipsender(self):
        pass

    def get_errors_ipsender(self):
        return self.error_ipsender

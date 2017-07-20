import re
from sqlrw import crt_users, list_users


class RegUsersForm:
    def __init__(self, email: str, username: str, password: str, re_password: str, stateadmin: int):
        self.email = email
        self.username = username
        self.password = password
        self.re_password = re_password
        self.stateadmin = stateadmin
        self.error_forms = {}

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

    def writeusers(self):
        if len(self.error_forms) == 0:
            crt_users(self.username, self.email, self.password, self.stateadmin)
            return print('write to base data')
        else:
            return print('no write to base data', self.error_forms)

    def errors(self):
        return self.error_forms

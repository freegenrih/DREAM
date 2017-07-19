from RegUsers import RegUsersForm
email = 'admin@admin.ru'
username = 'Gena'
password = '<scrip password'
re_password = '<scrip password'

reg_form = RegUsersForm(email, username, password, re_password)

a = reg_form.errors()

reg_form.writeusers()
print(a)
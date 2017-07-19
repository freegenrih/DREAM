from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from sqlrw import list_users, crt_users, delet_users
from RegUsers import RegUsersForm

app = Flask(__name__)

dates = {
    'kay': 'secret',
    'CH1': 123,
    'CH2': 456,
    'CH3': 789,
    'CH4': 1011,
    'CH5': 2343,
    'CH6': 23123,
    'CH7': 1255,
    'CH8': 1212,
}


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST' \
            and request.form['email'] == 'admin@admin.ru' \
            and request.form['password'] == 'admin':
        if request.form['email'] == 'admin@admin.ru':
            user = 'Gennadyi'
        else:
            user = 'None'
        data = {
            'user': user,
            'email': request.form['email'],
            'password': request.form['password'],
        }
        return render_template("home.html", data=data)

    else:
        return render_template('signin.html')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/monitoring', methods=['GET'])
def monitoring():
    return render_template("monitoring.html", data=dates)


@app.route('/monitoring-online', methods=['GET'])
def monitoring_online():
    return render_template("monitoring-online.html", data=dates)


@app.route('/monitoring-database', methods=['GET'])
def monitoring_database():
    return render_template("monitoring-database.html", data=dates)


@app.route('/monitor', methods=['GET'])
def monitor():
    if request.method == 'GET' and request.args['key'] == 'yyy':
        data = {
            'kay': request.args['key'],
            'CH1': request.args['ch1'],
            'CH2': request.args['ch2'],
            'CH3': request.args['ch3'],
            'CH4': request.args['ch4'],
            'CH5': request.args['ch5'],
            'CH6': request.args['ch6'],
            'CH7': request.args['ch7'],
            'CH8': request.args['ch8'],

        }
        global dates
        dates = data
        return render_template("monitor.html", data=dates)
    else:
        return render_template("monitor.html")


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    return render_template("settings.html")


@app.route('/settings-users', methods=['POST', 'GET'])
def settings_users():
    if request.method == 'POST':
        if request.form['submit'] == '          RegisterUser           ':
            reg_form = RegUsersForm(request.form['email'],
                                    request.form['username'],
                                    request.form['password'],
                                    request.form['re_password']
                                    )
            reg_form.writeusers()
            data = list_users()
            errors = reg_form.errors()
            return render_template("settings-users.html", data=data, errors=errors)

        elif request.form['submit'] == '           DeleteUser            ' and request.form['iduser'] != '':

            delet_users(request.form['iduser'])
            data = list_users()
            return render_template("settings-users.html", data=data)
        else:
            data = list_users()
            return render_template("settings-users.html", data=data)

    else:
        data = list_users()
        return render_template("settings-users.html", data=data)


@app.route('/settings-ipsender', methods=['POST', 'GET'])
def settings_ipsenders():
    return render_template("settings-ipsender.html")


if __name__ == '__main__':
    app.run(debug=True)

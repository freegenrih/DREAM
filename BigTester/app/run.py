from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)

dates = {}


@app.route('/base', methods=['POST', 'GET'])
def base():
    return render_template("base.html")


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
        # return render_template("monitor.html", data=data)

    else:
        global dates
        return render_template("monitor.html", data=dates)


@app.route('/settings')
def settings():
    return render_template("settings.html")


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST' \
            and request.form['email'] == 'admin@admin.ru'\
            and request.form['password'] == 'admin':
        if request.form['email'] == 'admin@admin.ru':
            user ='Gennadyi'
        else:
            user='None'
        data = {
            'user':user,
            'email': request.form['email'],
            'password': request.form['password'],
        }
        return render_template("enter.html", data=data)

    else:

        return render_template('signin.html')


if __name__ == '__main__':
    app.run()

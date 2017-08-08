from flask import Flask
from flask import render_template
from flask import request

from sqlrw import list_users, wraper_read

from Users import (RegUsersForm,
                   UpdateUsersForm,
                   DeleteUsersForm,
                   SignIn,
                   IPSenderRegDel,
                   IPsenderGet
                   )



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
    if request.method == 'POST':
        signin_form = SignIn(request.form['email'], request.form['password'])
        signin_errors = signin_form.error_signin()
        if signin_form.validate() == True:
            return render_template("home.html")
        else:
            return render_template('signin.html', signin_errors=signin_errors)
    else:
        return render_template('signin.html')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/monitoring', methods=['GET'])
def monitoring():
    return render_template("monitoring.html")


@app.route('/monitoring-online', methods=['GET'])
def monitoring_online():
    return render_template("monitoring-online.html", data=dates)


@app.route('/monitoring-database', methods=['GET'])
def monitoring_database():
    sql = "SELECT * FROM `IPSenderData`"
    data = wraper_read(sql)
    return render_template("monitoring-database.html", data=data)


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
        if request.form['submit'] == 'RegisterUser':
            if request.form['statusadmin'] == 'Admin':
                statusadmin = 1
            else:
                statusadmin = 0

            reg_form = RegUsersForm(request.form['email'],
                                    request.form['username'],
                                    request.form['password'],
                                    request.form['re_password'],
                                    statusadmin
                                    )
            reg_form.write_users()
            return render_template("settings-users.html", data=list_users(), errors=reg_form.errors())


        elif request.form['submit'] == 'DeleteUser' and request.form['email'] != '':
            if request.form['password'] == request.form['re_password']:
                del_form = DeleteUsersForm(request.form['email'],
                                           request.form['password'],
                                           request.form['re_password'],
                                           )
                del_form.delete_users()
                return render_template("settings-users.html", data=list_users(), errors_delete=del_form.errors_delete())

            else:
                return render_template("settings-users.html", data=list_users())

        elif request.form['submit'] == 'Update Password' and request.form['email'] != '':
            update_form = UpdateUsersForm(request.form['email'],
                                          request.form['username'],
                                          request.form['old_password'],
                                          request.form['newpassword'],
                                          request.form['re_newpassword'],
                                          )
            update_form.update_users()
            errors_edit = update_form.errors_updates()
            return render_template("settings-users.html", data=list_users(), errors_edit=errors_edit)

        else:
            return render_template("settings-users.html", data=list_users())

    else:
        return render_template("settings-users.html", data=list_users())


@app.route('/settings-ipsender', methods=['POST', 'GET'])
def settings_ipsenders():
    if request.method == 'POST' and request.form['submit'] == "Create IPS":
        ipsender = IPSenderRegDel(request.form['name'], request.form['key'], request.form['password'])
        errors = ipsender.get_errors_ipsender()
        ipsender.create_ipsender()
        ipsender_list = IPsenderGet().list_ipsender()
        return render_template("settings-ipsender.html", errors_ipsender=errors, ipsender_list=ipsender_list)

    if request.method == 'POST' and request.form['submit'] == "Delete IPS":
        ipsender = IPSenderRegDel(request.form['name'], request.form['key'], request.form['password'])
        errors = ipsender.get_errors_ipsender()
        ipsender.delete_ipsender()
        ipsender_list = IPsenderGet().list_ipsender()
        return render_template("settings-ipsender.html", errors_ipsender=errors, ipsender_list=ipsender_list)

    else:
        ipsender_list = IPsenderGet().list_ipsender()
        return render_template("settings-ipsender.html", ipsender_list=ipsender_list)


if __name__ == '__main__':
    app.run(debug=True)

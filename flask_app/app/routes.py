""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, url_for
from app import app
from app import database as db_helper

@app.route("/create", methods=['POST'])
def create():
    """Receives post requests for creation of a new vehicle"""
    data = request.get_json()
    db_helper.insert_new_vehicle(data)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/delete", methods=['POST'])
def delete():
    """ Receives post requests for deleting entry"""
    data = request.get_json()
    print(data)
    try:
        db_helper.remove_vehicle(data)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)


@app.route("/employeehomepage")
def employee_home():
    items = db_helper.fetch_by_company()
    return render_template("index.html", items=items)

@app.route("/userhomepage")
def user_home():
    return render_template("user_homepage.html")

@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_by_company()
    return render_template("entry.html", items=items)


@app.route("/search/<key>")
def search(key):
    print(key)
    """ returns rendered homepage """
    items = db_helper.search_database(key)
    return render_template("search.html", items=items)

@app.route("/sp")
def run_sp():
    items = db_helper.run_stored_proc()
    return render_template("sp.html", items = items)


@app.route("/update", methods=['POST'])
def update():
    """Updates the database"""
    data = request.get_json()
    db_helper.update_status(data)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/custom.html")
def open_custom_page():
    return render_template("custom.html")

@app.route("/customquery1/<b1>/<c1>/<b2>/<c2>", methods=['GET'])
def custom_1(b1, c1, b2, c2):
    result = db_helper.custom_1(b1, c1, b2, c2)
    return render_template("custom1results.html", items=result)

@app.route("/customquery2/<brand>", methods=['GET'])
def custom_2(brand):
    result = db_helper.custom_2(brand)
    return render_template("custom2results.html", items=result)

# New Methods Added Routes to Handle User and Employee Login Spearatelt
# Idea: Structure: Let users and employees log in to different sections. For users, let there be a map to view chargers around
# For Users, Have the CRUD applications
# Also, can add the option of charger search for users

@app.route('/employee-login', methods=['GET', 'POST'])
def emp_login():
    error = None
    data = request.get_json()
    if request.method == 'POST':
        print(data['id'])
        print(data['password'])
        if data['id'] != 'admin' or data['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
            print(error)
        else:
            result = {'success': True, 'response': 'Done'}
            # return redirect(url_for('employee_home'))
            return jsonify(result)
    return render_template('entry.html', error=error)


@app.route('/user-login', methods=['GET', 'POST'])
def user_login():
    error = None
    data = request.get_json()
    if request.method == 'POST':
        print(data['id'])
        print(data['password'])
        boolean_indicator = db_helper.check_user_creds(data['id'], data['password'])
        if boolean_indicator == False:
            error = 'Invalid Credentials. Please try again.'
            print(error)
        else:
            result = {'success': True, 'response': 'Done'}
            return jsonify(result)
    return render_template('entry.html', error=error)
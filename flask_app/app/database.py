"""Defines all the functions related to the database"""
from dataclasses import dataclass

from matplotlib.pyplot import connect
from app import db

def fetch_by_company() -> dict:
    """Shows all vehicles listed in the database table that belong to a particular company
    Returns:
        A list of dictionaries
    """
    c = db.connect()
    result = c.execute("SELECT Brand, count(*) from Vehicle Group By Brand ORDER BY count(*) DESC").fetchall()
    c.close()

    #Creating a list of dictionaries
    vehicle_list = []

    for r in result:
        vehicle = {
            "brand": r[0],
            "number": r[1]
        }
        vehicle_list.append(vehicle)

    return vehicle_list
    # Establishing connection with the database
    




def insert_new_vehicle(data: dict) ->  int:
    """Insert new Vehicle to Vehicle table.
    """   
    vehicle_id = data['Vehicle_ID']
    brand = data['Brand']
    model = data['Model']
    price = data['Price']
    avg = data['Average_Maintenance_Cost']
    stat = data['Upcoming_Current']

    c = db.connect()
    query = 'Insert Into Vehicle(Vehicle_ID, Brand, Model, Price, Average_Maintenance_Cost, Upcoming_Current) VALUES ("{}", "{}","{}", "{}","{}", "{}");'.format(vehicle_id, brand, model, price, avg, stat)
    c.execute(query)

    query_results = c.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    c.close()

    return task_id


def remove_vehicle(data:dict) -> None:
    """ remove entries based on task ID """
    vehicle_id = data['Vehicle_ID']
    c = db.connect()
    query = 'Delete From Vehicle where Vehicle_ID={};'.format(vehicle_id)
    c.execute(query)
    c.close()


def search_database(key:str) -> dict:
    """Shows all vehicles listed in the database table that belong to a particular company
    Returns:
        A list of dictionaries
    """
    # Establishing connection with the database
    c = db.connect()
    n_key = '%%'+key+'%%'
    print(key)
    result = c.execute('SELECT * from Vehicle WHERE Vehicle_ID like "{}"or Brand Like "{}" or Model Like "{}" or Price Like "{}" or Average_Maintenance_Cost Like "{}" or Upcoming_Current Like "{}" ORDER By Brand'.format(n_key, n_key, n_key,n_key,n_key, n_key)).fetchall()
    c.close()

    #Creating a list of dictionaries
    vehicle_list = []

    for r in result:
        vehicle = {
            "id": r[0],
            "brand": r[1],
            "model": r[2],
            "price": r[3],
            "avg": r[4],
            "stat": r[5],
        }
        vehicle_list.append(vehicle)

    return vehicle_list

def update_status(data : dict) -> None:
    """Updates status of vehicle
    """
    brand = data['Brand']
    model = data['Model']
    n_stat = data['Upcoming_Current']

    c = db.connect()
    query = 'Update Vehicle set Upcoming_Current = "{}" WHERE Brand = "{}" and Model = "{}";'.format(n_stat, brand, model)
    c.execute(query)
    c.close()


def custom_1(b1:str, c1:str, b2: str, c2:str) -> dict :
    "Returns the result of the first custom query"
    n_c1 = '%%'+c1+'%%'
    n_c2 = '%%'+c2+'%%'

    c = db.connect()
    query = """SELECT v.Vehicle_ID, Brand, Model, w.Charger_Type 
            FROM Vehicle v NATURAL JOIN Compatible_With w 
            WHERE Brand = "{}" and w.Charger_Type Like "{}" 
            UNION 
            SELECT v1.Vehicle_ID, Brand, Model, w1.Charger_Type 
            FROM Vehicle v1 NATURAL JOIN Compatible_With w1 
            WHERE Brand = "{}" and w1.Charger_Type Like "{}"
            ORDER BY Vehicle_ID LIMIT 15;""".format(b1, n_c1, b2, n_c2)

    result = c.execute(query).fetchall()
    c.close()

    #Creating a list of dictionaries
    vehicle_list = []

    for r in result:
        vehicle = {
            "id": r[0],
            "brand": r[1],
            "model": r[2],
            "Charger_type": r[3]
        }
        vehicle_list.append(vehicle)

    return vehicle_list

def custom_2(b1:str) -> dict :
    "Returns the result of the second custom query"
    c = db.connect()
    query = """SELECT Brand, avg(Price) 
                FROM Vehicle 
                GROUP BY Brand 
                HAVING avg(Price) < (SELECT avg(price) 
                FROM Vehicle 
                WHERE Brand = "{}") ORDER BY avg(price)
                LIMIT 15;""".format(b1)

    result = c.execute(query).fetchall()
    c.close()

    #Creating a list of dictionaries
    vehicle_list = []

    for r in result:
        vehicle = {
            "brand": r[0],
            "price": r[1]
        }
        vehicle_list.append(vehicle)

    return vehicle_list

def check_user_creds(id:str, password:str) -> bool:
    "Checks for the credentials of a user"
    c = db.connect()
    query = """SELECT Password 
                FROM User 
                WHERE User_ID = {};""".format(id)

    actual_password = c.execute(query).fetchall()[0][0]
    c.close()

    print("actual_password", actual_password)
    if actual_password == password:
        print("Checked credentials. Works fine")
        return True
    else:
        return False

def run_stored_proc():
    c = db.connect()
    result = c.execute("call GetBrandRating();").fetchall()
    c.close()

    ratings = []

    for r in result:
        rating= {
            "b": r[0],
            "p": r[1],
            "c": r[2],
            "d": r[3],
            "a":r[4],
            "r":r[5]
        }
        ratings.append(rating)

    return ratings


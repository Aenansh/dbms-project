from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Database Configuration
db = pymysql.connect(
    host="localhost",
    user="root",
    password="vasu",
    database="CollegeTaxiSystem"
)

@app.route('/book_taxi', methods=['POST'])
def book_taxi():
    data = request.json
    cursor = db.cursor()
    query = """
        INSERT INTO StudentRequests (Student_ID, No_of_People, Pickup_Location, Drop_Location, Time, Car_Type, Day)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data['Student_ID'], data['No_of_People'], data['Pickup_Location'],
        data['Drop_Location'], data['Time'], data['Car_Type'], data['Day']
    ))
    db.commit()
    return jsonify({"message": "Request booked successfully!"})

@app.route('/available_cars', methods=['GET'])
def available_cars():
    car_type = request.args.get('Car_Type')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = """
        SELECT * FROM AvailableCars
        WHERE Car_Type = %s AND Availability_Status = TRUE
    """
    cursor.execute(query, (car_type,))
    cars = cursor.fetchall()
    return jsonify(cars)

@app.route('/calculate_cost', methods=['GET'])
def calculate_cost():
    drop_location = request.args.get('Drop_Location')
    cursor = db.cursor()
    query = "SELECT Cost FROM Locations WHERE Location_Name = %s"
    cursor.execute(query, (drop_location,))
    cost = cursor.fetchone()
    return jsonify({"Cost": cost[0]})

if __name__ == '__main__':
    app.run(debug=True)

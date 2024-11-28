from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "vasu",  # Update this to your MySQL password
    "database": "CollegeTaxiSystem"
}

# Establish database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/request', methods=['GET', 'POST'])
def request_taxi():
    if request.method == 'POST':
        data = request.form
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO StudentRequests 
            (Student_ID, Student_Phone, No_of_People, Pickup_Location, Drop_Location, Time, Car_Type, Day)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data['Student_ID'], data['Student_Phone'], data['No_of_People'], data['Pickup_Location'],
            data['Drop_Location'], data['Time'], data['Car_Type'], data['Day']
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Taxi request submitted successfully!"})
    return render_template('request.html')

# @app.route('/availability')
# def availability():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     query = "SELECT * FROM AvailableCars WHERE Availability_Status = TRUE"
#     cursor.execute(query)
#     cars = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return render_template('availability.html', cars=cars)

@app.route('/availability')
def availability():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Ensure we're using dictionary cursor for better JSON handling
    query = "SELECT * FROM AvailableCars WHERE Availability_Status = TRUE"
    cursor.execute(query)
    cars = cursor.fetchall()  # Fetch all available cars
    cursor.close()
    conn.close()
    return jsonify(cars)  # Return the data as JSON


if __name__ == '__main__':
    app.run(debug=True)

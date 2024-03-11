from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
# MySQL database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'craigslist'
}

def get_data_from_mysql():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Replace 'your_table' with the actual table name
        query = 'SELECT * FROM cities'
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Convert rows to a list of dictionaries
        # data = [row for row in rows]
        data = [{'id': row[0], 'name': row[1], 'url': row[2], 'timezone': row[3], 'checked':row[4]} for row in rows]

        return data

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

@app.route('/api/data', methods=['GET'])
def serve_data():
    data = get_data_from_mysql()

    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to retrieve data from MySQL'}), 500

if __name__ == '__main__':
    app.run(debug=True)

import mysql.connector
import json

def render_json_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        if not file_content:
            print(f"Error: File '{file_path}' is empty.")
            return

        json_data = json.loads(file_content)
        return json_data

data = render_json_file('reformed.json')

# # MySQL database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'craigslist'
}

# # Sample data for insertion
data_list = data

def insert_rows(connection, cursor, data_list):
    try:


        # Insert data into the table using a for loop
        insert_query = '''
        INSERT INTO cities (time_zone, url, name, checked) VALUES (%s, %s, %s, %s)
        '''
        for entry in data_list:
            cursor.execute(insert_query, (entry['time_zone'], entry['url'], entry['name'], entry['checked']))

        # Commit the changes
        connection.commit()
        print(f"{cursor.rowcount} row(s) inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    # Establish a connection to the MySQL server
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Call the function to insert rows
        insert_rows(connection, cursor, data_list)

    except mysql.connector.Error as err:
        print(f"Error: {err}")


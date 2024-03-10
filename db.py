import mysql.connector

# Replace these with your actual database details
host = 'https://finally12123.000webhostapp.com/index.php'
user = 'id21969666_db'
password = 'Database1!'
database = 'id21969666_db'

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Example: Execute a simple SELECT query
query = "SELECT * FROM cities"
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Display the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='craigslist'
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a simple SELECT query
cursor.execute("SELECT * FROM cities")

# Fetch all the results
results = cursor.fetchall()

# Display the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
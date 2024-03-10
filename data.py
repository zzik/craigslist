import json
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'craigslist'
}
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


def render_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            if not file_content:
                print(f"Error: File '{file_path}' is empty.")
                return

            json_data = json.loads(file_content)
            return json_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in '{file_path}': {e}")

data = render_json_file('please.json')

json_file_path = 'reformed.json'

# read existing JSON
with open(json_file_path, 'r') as file:
    current_data = json.load(file)

    for state in data:
        for city in state['cities']:
            new_data = {
                "time_zone":state["time_zone"],
                "url":city["link"]+"search/remote-jobs",
                "name":city["text"],
                "checked":False
            }
            current_data.append(new_data)

insert_query = '''
        INSERT INTO users (time_zone, url, name, checked) VALUES (%s, %s, %s, %s)
        '''
cursor.executemany(insert_query, current_data)

# Commit the changes
connection.commit()
print(f"{cursor.rowcount} row(s) inserted successfully.")
cursor.close()
connection.close()
# with open(json_file_path, 'w') as file:
#     json.dump(current_data, file, indent=2)
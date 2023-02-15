from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import sqlite3
import json

options = webdriver.ChromeOptions()

#check that the correct version of the driver is installed for the version of Chrome is installed
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def get_query(file_path):
    'Returns a random search query from a text file.'
    with open(file_path, 'r') as f:
        lines = f.readlines()
        line = random.choice(lines).strip()
        return line


results = {} # Initiate empty dictionary to capture results
def get_searchResults():
    'Function to get search results from google and save them into a dictionary'
    #get a random search query from given txt files
    query = get_query('bowling.txt')
    # Specify number of pages on google search, each page contains 10 #links
    n_pages = 5
    links = [] # Store Results in list
    for page in range(1, n_pages):
        #create Url and enter it into driver
        url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #Use beautiful soup to find all cases of certain class
        search = soup.find_all('div', class_="yuRUbf")
        #Add searches to list
        for h in search:
            links.append(h.a.get('href'))
    # time_sleep = random.randint(0, 60)
    # time.sleep(time_sleep*60)
    driver.close()

    # Store the search results in the dictionary
    results[query] = links

    print(results)


def create_table(db_path, table_name):
    # Establish connection to database
    conn = sqlite3.connect(db_path)

    # Drop table if it exists
    conn.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Create table
    conn.execute(f"CREATE TABLE {table_name} (my_data TEXT)")

    # Close connection
    conn.close()


def store_dict_in_sqlite(my_dict, db_path, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Convert the dictionary to a JSON string
    json_str = json.dumps(my_dict)
    # Define the SQL query that will insert the JSON string into the database
    query = f"INSERT INTO {table_name} (my_data) VALUES (?)"

    # Execute the query with the JSON string as a parameter
    conn.execute(query, (json_str,))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()
def main():
    create_table('test.db', 'table1')
    get_searchResults()
    store_dict_in_sqlite(results, 'test.db','table1')
main()
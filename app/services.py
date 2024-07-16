import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
datafolder = os.path.join(BASE_DIR, "data")
datasource = os.path.join(datafolder, "users.json")

def check_dataset_exists():
    """
    Ensure the data folder and JSON file exist.
    Creates them if they do not.
    """
    if not os.path.exists(datafolder):
        os.mkdir(datafolder)
    if not os.path.exists(datasource):
        # Initialize the JSON file with an empty list
        with open(datasource, "w") as f:
            f.write('{"data": []}')

def read_usersdata():
    """
    Read user data from the JSON file.
    Returns the parsed JSON data.
    """
    check_dataset_exists()
    with open(datasource, "r") as f:
        content = f.read()
        if content == "":
            content = '{"data": []}'  # Fallback if file is empty
        users = json.loads(content)
    return users

def add_userdata(user: dict):
    """
    Add a new user to the JSON file.
    """
    users = read_usersdata()
    # Append the new user to the 'data' list
    if "data" in users:
        users["data"].append(user)
    else:
        users["data"] = [user]
    
    # Write the updated data back to the file
    with open(datasource, "w") as f:
        json.dump(users, f, indent=2)

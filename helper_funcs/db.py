from deta import Deta
import streamlit as st

# Initialize Deta Object with Project Key
deta_cred = st.secrets['db_credentials']
deta = Deta(deta_cred['deta_key'])

def get_all_user_details():
    usernames = {}
    users = deta.Base("users") # Get User Db
    all_users_obj = users.fetch() #Get All Users (Rows)
    users = all_users_obj.items
    
    # Wrangling structure for Authentication
    for user in users:
        usernames[user["username"]] = user
    return usernames


def create_user(usernames):
    users = deta.Base("users")
    previous_users = users.fetch().items
    previous_usernames = [x["username"] for x in previous_users]

    usernames = {
        key: value for key, value in usernames.items() if key not in previous_usernames
    }

    key = list(usernames.keys())[0]
    insert_user = usernames[key]
    insert_user["username"] = key
    users.insert(insert_user)
    

import json
import os
from datetime import datetime, timedelta

DATA_FILE = "user_data.json"

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_users(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def start_trial(user_id):
    users = load_users()
    if str(user_id) in users:
        return False
    end_date = datetime.now() + timedelta(days=1)
    users[str(user_id)] = {"end_date": end_date.strftime("%Y-%m-%d %H:%M:%S"), "type": "trial"}
    save_users(users)
    return True

def subscribe_user(user_id, days):
    users = load_users()
    end_date = datetime.now() + timedelta(days=days)
    users[str(user_id)] = {"end_date": end_date.strftime("%Y-%m-%d %H:%M:%S"), "type": f"{days}-day"}
    save_users(users)

def is_subscription_active(user_id):
    users = load_users()
    if str(user_id) not in users:
        return False
    end = datetime.strptime(users[str(user_id)]["end_date"], "%Y-%m-%d %H:%M:%S")
    return datetime.now() < end

def get_expiry(user_id):
    users = load_users()
    if str(user_id) not in users:
        return None
    return users[str(user_id)]["end_date"]
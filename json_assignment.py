# json_assignment.py
# JSON Assignment Solution
# Author: Venky

import json

# -------------------------------
# Task 1 — Build a JSON Structure
# -------------------------------
user_profile = {
    "name": "Venky",
    "age": 25,
    "email": "venky@example.com",
    "is_active": True,
    "skills": ["Python", "Machine Learning", "Networking"]
}

print("Task 1 — JSON Structure:")
print(json.dumps(user_profile, indent=4))
print("\n")

# -------------------------------
# Task 2 — Parse an API Response
# -------------------------------
api_response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'
parsed_response = json.loads(api_response)

username = parsed_response["data"]["username"]
score = parsed_response["data"]["score"]

print("Task 2 — API Response Parsing:")
print("Username:", username)
print("Score:", score)
print(f"User {username} scored {score} points")
print("\n")

# -------------------------------
# Task 3 — Handle Nested JSON
# -------------------------------
user_data = {
    "name": "Priya",
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "zip": "560001"
    }
}

city = user_data["address"]["city"]
zip_code = user_data["address"]["zip"]

print("Task 3 — Nested JSON Handling:")
print("City:", city)
print("Zip Code:", zip_code)

# Add new key "country" inside address
user_data["address"]["country"] = "India"

print("Updated JSON:")
print(json.dumps(user_data, indent=4))
Python
# Simulated user data (replace with actual storage mechanism)
users = {
    "user1": {"enrolled_data": "hashed_fingerprint_data"}
}

def enroll_user(username, biometric_data):
  # Simulate secure storage (e.g., hash and store)
  users[username] = {"enrolled_data": hash_function(biometric_data)}
  print(f"User {username} enrolled successfully.")

def authenticate_user(username, captured_data):
  # Simulate data retrieval and comparison (replace with library calls)
  if users.get(username) and users[username]["enrolled_data"] == hash_function(captured_data):
    print(f"User {username} authenticated successfully.")
  else:
    print("Authentication failed.")

# Enrollment example
enroll_user("user1", "sample_fingerprint")

# Authentication example (replace with actual capture method)
captured_data = "user_provided_fingerprint"
authenticate_user("user1", captured_data)

import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Load .env file

token = os.getenv("CLICKUP_API_TOKEN")
print("Loaded token:", token)  # For debugging

headers = {
    "Authorization": token
}

response = requests.get("https://api.clickup.com/api/v2/user", headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())

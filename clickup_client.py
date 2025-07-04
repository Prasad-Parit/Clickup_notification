import requests
import os
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "Authorization": os.getenv("CLICKUP_API_TOKEN"),
    "Content-Type": "application/json"
}

# Define the statuses to filter
STATUSES = [
    "Open",
    "Waiting for support",
    "Waiting for approval",
    "On hold"
]

def get_filtered_tasks_for_list(list_id):
    # Construct the query string with multiple statuses
    status_query = "&".join([f"statuses[]={status.replace(' ', '%20')}" for status in STATUSES])
    url = f"https://api.clickup.com/api/v2/list/{list_id}/task?{status_query}"

    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Error fetching tasks for list {list_id}: {response.status_code}")
        return []

    return response.json().get("tasks", [])

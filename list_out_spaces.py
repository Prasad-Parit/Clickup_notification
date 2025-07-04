import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("CLICKUP_API_TOKEN")

headers = {
    "Authorization": token
}

def get_teams():
    r = requests.get("https://api.clickup.com/api/v2/team", headers=headers)
    return r.json()["teams"]

def get_spaces(team_id):
    r = requests.get(f"https://api.clickup.com/api/v2/team/{team_id}/space", headers=headers)
    return r.json()["spaces"]

def get_folders(space_id):
    r = requests.get(f"https://api.clickup.com/api/v2/space/{space_id}/folder", headers=headers)
    return r.json()["folders"]

def get_lists(folder_id):
    r = requests.get(f"https://api.clickup.com/api/v2/folder/{folder_id}/list", headers=headers)
    return r.json()["lists"]

def get_tasks(list_id):
    r = requests.get(f"https://api.clickup.com/api/v2/list/{list_id}/task", headers=headers)
    return r.json().get("tasks", [])

teams = get_teams()

for team in teams:
    print(f"👥 Team: {team['name']}")
    spaces = get_spaces(team["id"])
    
    for space in spaces:
        print(f"  🗂 Space: {space['name']}")
        folders = get_folders(space["id"])
        
        for folder in folders:
            print(f"    📁 Folder: {folder['name']}")
            lists = get_lists(folder["id"])
            
            for lst in lists:
                print(f"      📋 List: {lst['name']} (ID: {lst['id']})")
                tasks = get_tasks(lst['id'])

                if not tasks:
                    print("        ❌ No tasks found")
                else:
                    for task in tasks:
                        print(f"        ✅ Task: {task['name']} (Status: {task['status']['status']})")

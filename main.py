from clickup_client import get_filtered_tasks_for_list
from datetime import datetime, timezone
import pytz

# Mapping of list IDs to readable names
LISTS = {
    "900200424416": "AWS",
    "900200424417": "GitHub",
    "901604984656": "MongoDB Atlas",
    "900200645782": "Jenkins",
    "900200667461": "Miscellaneous",
    "901608469670": "Prod Temp Access VPN",
    "901608574162": "Prod Temp Access DB"

}


def number_of_days(created_ts):
    created_sec = int(created_ts) / 1000
    created_date = datetime.fromtimestamp(created_sec, tz=timezone.utc)
    now = datetime.now(timezone.utc)
    delta = now - created_date
    return round(delta.days)



for list_id, list_name in LISTS.items():
    print(f"\n🗂️ {list_name}")
    print("ClickUp ID | Duration | Created By | Assignee")
    print("-" * 100)

    tasks = get_filtered_tasks_for_list(list_id)

    if not tasks:
        print("No open tasks found.")
        continue

    
    for task in tasks:
        custom_id = task.get("custom_id", task["id"])
        link = task["url"]
        clickable_id = f"<{link}|{custom_id}>"
        created = task.get("date_created", 0)
        duration_days = number_of_days(created) if created else 0

        if duration_days <= 14:
            continue  # Skip tasks newer than or equal to 14 days

        duration_str = f"{duration_days} days"
        assignee_list = task.get("assignees", [])
        assignee = assignee_list[0]["username"] if assignee_list else "Unassigned"
        creator = task.get("creator", {}).get("username", "Unknown")

        print(f"{clickable_id} | {duration_str} | {creator} | {assignee}")

import os
import extract_msg
import json

filename = "TOP - SEC/Paul Search Term -stock/Reminder - 1st additional Northbound trading day (H-1) on 25 May 2023.msg"
print(filename)
with open(filename, "rb") as f:
    msg = extract_msg.message.Message(f)
    msg_json = json.loads(msg.getJson())
    print(json.dumps(msg_json, indent=4))

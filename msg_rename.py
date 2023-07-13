import datetime
import os
import extract_msg
import json
from utils import encode_receivers, parse_contact


rootdir = "TOP - SEC"
name_set = dict()

count = 0
for subdir, dirs, files in os.walk(rootdir):
    for file in [f for f in files if f.endswith(".msg")]:
        count += 1
        if count > 10000:
            break
        filename = os.path.join(subdir, file)
        with open(filename, "rb") as f:
            try:
                msg = extract_msg.message.Message(f)
                msg_json = msg.getJson()
                msg_info = json.loads(msg_json)
                sender = msg_info["from"]
                receivers = msg_info["to"].split(">; ")
                # Tue, 07 Feb 2023 08:02:10 -0500
                date = datetime.datetime.strptime(
                    msg_info["date"], "%a, %d %b %Y %H:%M:%S %z"
                ).strftime("%m-%d-%Y")
                new_name = (
                    subdir
                    + "/"
                    + parse_contact(sender)
                    + " exchanges with "
                    + encode_receivers(receivers)
                    + " "
                    + date
                )
                if new_name in name_set:
                    name_set[new_name] += 1
                    seq = name_set[new_name]
                    new_name += "(" + str(seq) + ")"
                    print(seq)
                else:
                    name_set[new_name] = 1
                new_name += ".msg"
                print(f"{filename},{new_name},{sender},{receivers},{date}")
                os.rename(filename, new_name)
            except Exception as e:
                sender = msg_info["from"]
                receivers = msg_info["to"]
                date = msg_info["date"]
                print(
                    f"{filename}, went wrong. from: {sender}, to: {receivers}, date: {date}"
                )

import datetime
import eml_parser
import glob
import os
from utils import encode_receivers, parse_contact


eml_path = "multi part 3"
ep = eml_parser.EmlParser()
name_set = dict()

for filename in glob.glob(os.path.join(eml_path, "*.eml")):
    with open(filename, "rb") as fhdl:
        # print("old name:", filename)
        raw_email = fhdl.read()

        parsed_eml = ep.decode_email_bytes(raw_email)
        content = parsed_eml["header"]["header"]
        sender = content["from"][0]
        receivers = content["to"][0].split(", ")
        # Fri, 22 Jul 2022 04:34:24 +0000
        date = datetime.datetime.strptime(
            content["date"][0], "%a, %d %b %Y %H:%M:%S %z"
        ).strftime("%m-%d-%Y")
    new_name = (
        eml_path
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
    new_name += ".eml"
    print(f"{filename},{new_name},{sender},{receivers},{date}")
    os.rename(filename, new_name)

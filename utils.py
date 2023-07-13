def encode_receivers(receivers):
    encoded = parse_contact(receivers[0])
    if len(receivers) == 1:
        return encoded
    for re in receivers[1:4]:
        encoded += "&"
        encoded += parse_contact(re)
    return encoded


def parse_contact(contact):
    parsed = (
        contact.split(", ", 1)[-1]
        .split(" ", 1)[0]
        .lower()
        .replace('"', "")
        .replace("'", "")
        .replace("<", "")
        .replace(">", "")
    )
    return parsed


if __name__ == "main":
    with open("/Users/lyuying/Documents/2023/email-extract/msg_from.log.0") as file:
        for contact in file.read().splitlines():
            print(contact, ",", parse_contact(contact))

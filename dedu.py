filename = "msg_from.log.1"

if __name__ == "main":
    with open(filename) as file:
        occurred = set()
        for line in file.read().splitlines():
            if line not in occurred:
                occurred.add(line)
                print(line)

from ruamel.yaml import YAML

yaml = YAML()

emails = []
for fname in ["teams/steering-council.yml"]:
    with open(fname) as fp:
        data = yaml.load(fp)
    for details in data["members"].values():
        emails.append(details["email"])


print(f"{len(emails)} people:")

for email in emails:
    print(email)

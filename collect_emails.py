emails = []
for fname in ["steering.csv"]:
    with open(fname) as fp:
        for line in fp:
            email = line.split(",")[1].strip()
            if email != "email":
                emails.append(email)


print("%d people:" % len(emails))

for email in emails:
    print(email)

with open("emails.txt") as emails:
    emails = emails.readlines()

for email in emails:
    if "hotmail" in email:
        print(email.rstrip())
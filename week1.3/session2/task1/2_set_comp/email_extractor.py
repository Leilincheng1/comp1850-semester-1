"""Normalize and deduplicate email addresses using set comprehensions."""
raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com",
              "UserB@yahoo.com", "admin@site.com"]
emails = {email.strip().lower() for email in raw_emails}
print(sorted(emails))

raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com",
               "admin@site.com", "UserB@yahoo.com"]
valid_emails = {email.strip().lower() for email in raw_emails2
                if "@" in email and email.count("@") == 1}
print(sorted(valid_emails))

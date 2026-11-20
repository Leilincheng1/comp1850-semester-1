"""Normalize and deduplicate email addresses using set comprehensions."""
raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com",
              "UserB@yahoo.com", "admin@site.com"]
emails = {email.strip().lower() for email in raw_emails}
print(sorted(emails))

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]


# set comprehension to extract a clean, unique set of lowercase email addresses


# print the clean set of email addressed


# Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).
# raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
# write another set comprehension for this case to extract a clean, unique set of valid, lowercase email addresses
raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
clean_email = {email.lower() for email in raw_emails2 if "@" in emails}
raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com",
               "admin@site.com", "UserB@yahoo.com"]
valid_emails = {email.strip().lower() for email in raw_emails2
                if "@" in email and email.count("@") == 1}
print(sorted(valid_emails))

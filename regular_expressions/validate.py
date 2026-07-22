import re
email = input("What's your email").strip()


# strip for avoid leading and trailing white spaces


# username, domain = email.split('@')

# if username and domain.endswith(".edu"):
#     print("valid")
# else:
#     print("Invalid")


# using re library now to check patterns

if re.search(".*@.*", email):
    print("valid")
else:
    print("Invalid")
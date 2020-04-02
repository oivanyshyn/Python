import re

phone_number=input("Enter a phone-number matchin XXX-XXX-XXXX pattern:")
pattern= "\w{3}-\w{3}-\w{4}"

if re.search(pattern, phone_number):
        print("Valid phone number")
else:
        print("Invalid phone number")
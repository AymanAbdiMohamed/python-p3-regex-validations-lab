import re

# ------------------------------
# Name regex: fully robust
# ------------------------------
name = r"^([A-Z][a-z]*(?:[-'][A-Z][a-z]*)?)( [A-Z][a-z]*(?:[-'][A-Z][a-z]*)?)*$"
name_regex = re.compile(name)

# ------------------------------
# Phone regex: robust
# ------------------------------
phone_number = r"^(\(\d{3}\)\s?|\d{3}[-. ]?)\d{3}[-. ]?\d{4}$"
phone_regex = re.compile(phone_number)

# ------------------------------
# Email regex: must start with a letter
# ------------------------------
email_address = r"^[A-Za-z][\w\.-]*@[\w-]+(\.[\w-]+)+$"
email_regex = re.compile(email_address)

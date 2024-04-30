import re


# is email valid
def is_email_valid(email: '') -> True or False:
    # Regular expression for validating an email address
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the regular expression
    if re.match(email_regex, email):
        return True
    else:
        return False




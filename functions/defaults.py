import re
import requests


# is email valid
def is_email_valid(email: '') -> True or False:
    # Regular expression for validating an email address
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the regular expression
    if re.match(email_regex, email):
        return True
    else:
        return False



def get_current_country():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        country = data.get("country")
        if country:
            print("Current country:", country)
        else:
            print("Unable to determine current country.")
    except Exception as e:
        print("Error:", e)

get_current_country()




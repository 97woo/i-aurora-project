import re

def validate_password(trinity_password):
    password_regex = '^[0-9]{6,6}$'
    return re.match(password_regex, trinity_password)
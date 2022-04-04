import re

def validate_identification(identification):
    id_regex = '^[a-zA-z-0-9]{6,20}$'
    return re.match(id_regex, identification)

def validate_password(password):
    password_regex = '^[0-9]{6,6}$'
    return re.match(password_regex, password)
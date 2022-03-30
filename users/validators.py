import re

def validate_id(trinity_id):
    id_regex = '^[a-zA-z-0-9]{6,20}$'
    return re.match(id_regex, trinity_id)

def validate_password(trinity_password):
    password_regex = '^[0-9]{6,6}$'
    return re.match(password_regex, trinity_password)
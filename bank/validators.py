import re

def validate_account_kb(account_number):
    id_regex = '([0-9,\-]{6,6}\-[0-9,\-]{2,2}\-[0-9,\-]{6,6})'
    return re.match(id_regex, account_number)

def validate_account_ibk(account_number):
    id_regex = '([0-9,\-]{3,3}\-[0-9,\-]{6,6}\-[0-9,\-]{2,2}\-[0-9,\-]{3,3})'
    return re.match(id_regex, account_number)

def validate_account_sh(account_number):
    id_regex = '([0-9,\-]{3,3}\-[0-9,\-]{4,4}\-[0-9,\-]{6,6})'
    return re.match(id_regex, account_number)

def validate_account_nh(account_number):
    id_regex = '[0-9,\-]{3,3}\-[0-9,\-]{4,4}\-[0-9,\-]{4,4}\-[0-9,\-]{2,2})'
    return re.match(id_regex, account_number)

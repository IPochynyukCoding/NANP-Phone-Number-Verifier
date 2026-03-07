import re 
import json

def phone_checker(phone_number:str,formats:dict,is_international:bool=False):
    if is_international:
        for format in formats['with_country_code']:
            if re.search(format,phone_number):
                return True
    else:
        for format_2 in formats["without_country_code"]:
            if re.search(format_2,phone_number):
                return True
    return False

if __name__ == "__main__":
    with open("valid_formats.json") as phone_format:
        phone_formats=json.load(phone_format)
    while True:
        phone_number=input("Enter your phone number or press 'q' to quit: ")
        if phone_number.lower() == "q":
            quit()
        if phone_number.startswith("+1"):
            is_valid_phone_number=phone_checker(phone_number,phone_formats,True)
        else:
            is_valid_phone_number=phone_checker(phone_number,phone_formats)
        print(f"Your phone number {phone_number} is{"" if is_valid_phone_number else "not"} a valid phone number.")
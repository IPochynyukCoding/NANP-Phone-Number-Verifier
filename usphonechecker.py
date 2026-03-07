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
        is_international=False
        if phone_number.lower() == "q":
            quit()
        elif phone_number.startswith("+1"):
            is_international=True
            is_valid_phone_number=phone_checker(phone_number,phone_formats,is_international)
        else:
            is_valid_phone_number=phone_checker(phone_number,phone_formats)
        print(f"Your phone number {phone_number} {"is" if is_valid_phone_number else "is not"} a valid {"international" if is_international else "local"} phone number.")
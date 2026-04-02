import re 
import json

def phone_format_checker(phone_number:str,formats:dict,is_international:bool):
    format_list:dict = formats["with_country_code"] if is_international else formats["without_country_code"]
    for format in format_list:
        if re.search(format,phone_number):
            return True
    return False

def standardize_format(phone_number:str):
    standardized_number=""
    for char in phone_number:
        if char.isnumeric():
            standardized_number+=char
    return standardized_number[1:] if standardized_number.startswith("1") and len(standardized_number)==11 else standardized_number
def area_code_checker(phone_number:str,valid_parameters:list):
    current_area_code=int(phone_number[0:3])
    if phone_number=="7106274387":
        return "federal government"
    for area_code in valid_parameters:
        if current_area_code in area_code["code_range"]:
            return area_code["type"]
    return False
if __name__ == "__main__":
    with open("valid_parameters.json") as valid_parameter:
        valid_parameters:dict=json.load(valid_parameter)
    while True:
        phone_number=input("Enter your phone number or press 'q' to quit: ")
        if phone_number.lower() == "q":
            quit()
        is_international=True if phone_number.startswith("1") or phone_number.startswith("+1") else False
        is_valid_phone_format=phone_format_checker(phone_number,valid_parameters['valid_formats'],is_international)
        if is_valid_phone_format:
            print(f"The phone number {phone_number} passes the formatting test.")
        else:
            print(f"The phone number {phone_number} fails the formatting test.")
            continue
        standardized_phone=standardize_format(phone_number)
        area_code_type=area_code_checker(standardized_phone,valid_parameters["valid_area_codes"])
        #7106274387 is only valid 710 area code number
        if area_code_type or standardized_phone == "7106274387":
            print(f"The phone number {phone_number} is a valid {area_code_type} number{" using the international format." if is_international else "."}")
        else:
            print(f"The phone number {phone_number} uses the correct format, but it is an invalid phone number.")

       
        
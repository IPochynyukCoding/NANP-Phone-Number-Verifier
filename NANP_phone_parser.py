import json
import os
import re
from datetime import datetime
def phone_number_finder(file_contents:str,regex_formats:list):
    phone_numbers:list[str]=[]
    for format in regex_formats:
        results:list[str]=re.findall(format,file_contents)
        if results:
            for result in results:
                if result not in phone_numbers:
                    phone_numbers.append(result)
    return phone_numbers
if __name__ == "__main__":
    with open("valid_parameters.json") as valid_parameters_json:
        valid_parameters=json.load(valid_parameters_json)
    while True:
        is_valid_file=False
        while(not is_valid_file):
            file_name=input("Text file to search for phone numbers: ").strip("'").strip('"')
            if os.path.isfile(file_name):
                with open(file_name) as file_opener:
                    file_contents=file_opener.read()
                is_valid_file=True
            elif file_name.lower()=="q":
                quit()
            else:
                print("The file you provided is invalid!")
        phone_finder=phone_number_finder(file_contents,valid_parameters['valid_formats_parser'])
        if phone_finder:
            phone_finder=list(map(lambda x:x+"\n",phone_finder))
            phone_finder[-1]=phone_finder[-1].strip("\n")
            print("Found numbers:")
            for phone_number in phone_finder:
                print(phone_number.strip("\n"))
            current_time=datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name=f"found_numbers_{current_time}.txt"
            with open(file_name,'w') as phone_list:
                phone_list.writelines(phone_finder)
            file_directory=os.path.join(os.getcwd(),file_name)
            print(f"Successfully added {file_directory} with {len(phone_finder)} unique phone number(s)")
        else:
            print("Unable to find phone numbers within this file")
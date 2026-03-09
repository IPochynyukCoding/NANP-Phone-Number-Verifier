import json
if __name__ == "__main__":
    with open("valid_parameters.json") as valid_json:
        valid_parameters:dict = json.load(valid_json)
    while True:
        area_type=input("Area code type: ")
        code_range=input("Phone range: ").split(",")
        try:
            code_range=list(map(lambda x:int(x),code_range))
        except ValueError:
            print("code range is invalid")
            continue
        valid_parameters['valid_area_codes'].append({"type":area_type,"code_range":code_range})
        print(f"Successfully added {area_type} with {code_range}")
        with open("valid_parameters.json","w") as valid_json_write:
            json.dump(valid_parameters,valid_json_write,indent=4)



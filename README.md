# North American Numbering Plan (NANP) Phone Number Suite

## Brief History of NANP 
### Initial concept
The NANP (North American Numbering Plan) system was introduced in the 1940s by Bell System to unify numbering plans across North America, reducing long-distance costs, labor for switchboard operators (later replaced with automated exchanges), and call completion times. The first direct call using area codes was from 10 November 1951 from Englewood, New Jersey to Alameda, California, proving the concept to be successful.
### Expansion and where it stands today
Initally, the NANP system was only meant for the US and Canada, but the NANP system was expanded in 1958 with Bermuda and other Caribbean islands with area code 809 but later on, other Caribbean nations split away from area code 809, such as Jamaica with area codes 658 and 876 to deal with the growing phonebase.

The most recent member of the NANP system was Sint Maarten (A Dutch island in the Carribbean) in 2011 with area code 721. In addition, the most recent NANP "relief assignment"* happened (as of the time of writing this README file) is in 23 February 2026 with area code 483 for Southeastern Alabama, so this repository will be updated to reflect any new "relief assignments". 

*A relief assignment is made when the NANP administrator suspects when an area code is nearing number exhausion, where an area code cannot assign any new phone numbers to phones, so a new area code will be assigned to the area to combat number exhausion.

## Scope

Here are the allowed phone number formats for this project:
* Dot notation (123.456.7890)
* Dash notation (123-456-7890)
* Space notation (123 456 7890)
* Parenthesis notation ((123) 456-7890)

### Things Out of Scope for this Project
* The parser and validator will not cover vanity phone numbers (i.e., 1-800-GOT-JUNK or 1-800-GOT-FLOWERS).
* Mixed-case phone numbers like (1-234.456-7890) will also not be covered, since it is an invalid format, despite being a valid phone number.

## Technical Details
### valid_parameters.json
This JSON file contains the regular expressions for the phone number validator (valid_formats) with each format in the scope having a local format and an international format, alongside the phone number parser, but the parser only has regular expressions for local format (for example 1-800-123-4567 will only get 800-123-4567). In addition, it contains the phone number types and valid area codes for the phone number validator with all US states and territories, all Canadian provinces, Anguilla, Bahamas, Barbados, Bermuda, British Virgin Islands, Cayman Islands, Dominica, Dominican Republic, Grenada, Guam, Jamaica, Montserrat, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Sint Maarten, Trinidad and Tobago, and Turks and Caicos Islands.
### NANP_phone_parser.py
The parser will ask you for a path to plaintext file to scan for phone numbers with checks to ensure your file path will be valid with a simple "Press 'q' to quit" if you want to quit. Next, it will use the same regular expressions in the valid_parameters.json to scan the file for valid phone numbers. Finally, it will show the results in both the terminal and in the text file with the format "found_numbers_YYYYMMDD_HHMMSS.txt", with YYYMMDD_HHMMSS being the current date and time.
### NANP_phone_validator.py
The checker will ask you for a phone number to validate, with the same "Press 'q' to quit" if you want to quit the program as the parser. The first step will be a regular expression check from the valid_parameters.json file to ensure your phone number matches the valid formats and spits out an error if the phone number's format is invalid. The second step strips the parenthesis and dashes to form a standard ten digit number (i.e., 123-456-7890 will be 1234567890). The final step will check the phone number's area code to see if it is valid, which uses the valid_parameters.json file for getting the valid area codes and spits out an error if the area code is invalid. This step also has a special check for the GETS Number (also known as the Federal number for emergency services), which is 710-627-4387, and will immediately flag this number as valid.



Sources used for history section: https://en.wikipedia.org/wiki/North_American_Numbering_Plan 

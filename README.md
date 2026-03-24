# North American Numbering Plan (NANP) Phone Number Suite
## Description
The NANP_phone_parser.py parses unique phone numbers (i.e., if there are two or more phone numbers with the exact same format and number, it will only count the first instance) from text files and .msg (Microsoft Outlook) files and outputs the unique phone numbers to a text file for your convenience. 

The NANP_phone_verifier.py determines if the phone number is valid and outputs the area code for the phone number if both the area code and the phone number's format is valid. 

Here are the allowed phone number formats for this project:

* Dot notation (123.456.7890)
* Dash notation (123-456-7890)
* Space notation (123 456 7890)
* Parenthesis notation ((123) 456-7890)


Please see https://en.wikipedia.org/wiki/North_American_Numbering_Plan for more details regarding the North American Numbering Plan.

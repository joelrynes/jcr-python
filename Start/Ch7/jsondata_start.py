# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json 


# Open the URL and read the data
api_url="https://uselessfacts.jsph.pl/api/v2/facts/random"
read_it=urllib.request.urlopen(api_url)
#print(read_it)
# Read the JSON data from the source
contents=json.loads(read_it.read())
print(contents)


# Print the content of the 'text' field
print(contents["text"])
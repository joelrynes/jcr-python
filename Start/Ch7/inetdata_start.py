# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
import urllib.request

#request and read
open_web=urllib.request.urlopen("http://example.com")
contents=open_web.read()
print(contents)
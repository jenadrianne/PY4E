import json
import urllib.request as ur
count = 0


url = input("Enter location: ")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_162.json"
print ("Retrieving ", url)

uh = ur.urlopen(url)
data= uh.read()
print ("Retrieved: " + str(len(data)) + " characters")

info = json.loads(data)
for item in info["comments"]:
	number = int(item["count"])
	count = count + number
print ("Count:", count)

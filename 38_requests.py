import requests

# make a get request to a URL and copy its content
r = requests.get('https://example.com')
#print(r.text)

# write the content copied from a URL to a text file
with open("new-text-file.txt", "w") as f:
	f.write(r.text)


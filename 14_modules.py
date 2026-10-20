# Python has built-in moudles and external modules. 

import mymodule # custom module I created in mymodule.py
import requests
# import antigravity

mymodule.hello()    

r = requests.get("https://www.google.com")
print(r.text)


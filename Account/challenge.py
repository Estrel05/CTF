import os
import base64

os.chdir("C:\\Users\\Estrel\\Documents\\GitHub\\CTF\\Account")

with open("account", "rb") as file:
    data = file.read()
    print(base64.b64encode(data))

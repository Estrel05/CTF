import os
from PIL import Image
from io import BytesIO

os.chdir("C:\\Users\\Estrel\\Documents\\GitHub\\ctf\\endianness-v2")

with open("challengefile", "rb") as file:
    data = file.read()

converted_data = b""
for i in range(0, len(data), 4):
    word = data[i : i + 4]
    converted_data += word[::-1]

image = Image.open(BytesIO(converted_data))
image.save("flag.jpeg")

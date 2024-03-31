import base64

encrypted = "cGljb0NURntNRTc0RDQ3QV9ISUREM05fNGRhYmRkY2J9Cg=="
flag = base64.b64decode(encrypted)

print(flag)

a = input()
b = a.split(":")
c = b[2]
d = c[2:]
e = c[:2]
if d == "AM":
    if a == "12:00:00AM":
        print("00:00:00")
    else:
        print(b[0] + ":" + b[1] + ":" + e)
else:
    if a == "12:00:00PM":
        print("12:00:00")
    else:
        b[0] = str(12 + int(b[0]))
        print(b[0] + ":" + b[1] + ":" + e)
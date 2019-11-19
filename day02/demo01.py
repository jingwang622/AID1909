f = open("test","w")
while True:
    data = input(">>")
    if not data:
        break
    f.write(data)
    f.flush()
f.close()
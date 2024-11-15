# readline 会一行一行的读取
file = open("readme")

while True:
    text = file.readline()
    print(text)

    if not text:
        break

file.close()

with open("readme", "r") as file:
    print(file.read())
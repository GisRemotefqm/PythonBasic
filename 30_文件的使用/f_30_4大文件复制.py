file_read = open("readme", "r")
file_write = open("readme_附件", "w")

while True:
    text = file_read.read()

    if not text:
        break

    file_write.write(text)

file_read.close()
file_write.close()
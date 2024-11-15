file_read = open("readme", "r")
file_write = open("readme_附件", "w")

text = file_read.read()
file_write.write(text)


file_read.close()
file_write.close()

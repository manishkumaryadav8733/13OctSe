# Lab 4b: Writing Multiple Strings into a File
f = open("data.txt", "w")
f.writelines(["Line1\n", "Line2\n", "Line3\n"])
f.close()

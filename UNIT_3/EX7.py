#  Write a program to copy a text file using file handling mechanism.

openfile = open("file2.txt","r")

writefile = open("file3.txt","w")

copy = openfile.read()

writefile.write(copy)
writefile.close()

content = open("file3.txt","r")
c = content.read()
print(c)

openfile.close()
writefile.close()
content.close()

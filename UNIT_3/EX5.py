#WAP to read a file and display its contents. At the end it shall also display no. of words available in file

file1 = open("mymodule.py","r")
reads = file1.read()
print(reads)

# Split Content and count words 
s = reads.split()
words=len(s)

print(f"Number Of Words in file - {words}")
file1.close()

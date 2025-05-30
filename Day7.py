#To open a file

myfile=open("C:\\Users\\faith\\Desktop\\myfile.txt","r")
print(myfile.read())

#To update an existing file

myfile=open("C:\\Users\\faith\\Desktop\\myfile.txt","a")
myfile.write("add new content to the end of file")

#to over write any existing file

myfile=open("C:\\Users\\faith\\Desktop\\myfile.txt","w")
myfile.write("Replacing the content of the file with this...")

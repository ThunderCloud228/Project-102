import os

def mergeFileData():
    file1 = input("Enter the first file's name here: ")
    file2 = input("Enter the second file's name here: ")
    path = input("Enter the path you want to create the new file in: ")

    file3 = 'mergedFile.txt'

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()
    
    with open(os.path.join(path, file3), 'w') as c:
        c.write(data_a+"\n")
        c.write(data_b)
    

mergeFileData()


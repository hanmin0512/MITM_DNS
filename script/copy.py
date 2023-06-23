inFp = open("./read.txt", "r")
outFp = open("./read_copy.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.write(inStr)
    print(inStr)
inFp.close()
outFp.close()

#read txt file
infp = open('./read.txt')

inStr = infp.readline()
print(inStr, end='')
infp.close()


FILENAME = "pands-weekly-tasks/topick07-files/count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# main
num = readNumber()
num += 1
print (f"we have run this program {num} times")
writeNumber(num)

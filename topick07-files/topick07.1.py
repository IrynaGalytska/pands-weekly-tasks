


with open("pands-weekly-tasks/topick07-files/test-a.txt") as f:
    data=f.read()
    print(data)

with open("pands-weekly-tasks/topick07-files/test-b.txt","w") as f2:
    data=f2.write("test b\n")
    print(data)

with open("pands-weekly-tasks/topick07-files/test-b.txt","a") as f3:
    data=f3.write("another line\n")
    print(data)
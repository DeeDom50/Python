def readfile():
    with open('names.txt', 'r') as file:
        names = file.readlines()
    names = [name.strip() for name in names]
    names.sort()
    print("Sorted Names:")
    for name in names:
        print(name)
    return names

def writefile(sorted_names):
    with open('sorted_names.txt', 'w') as file:
        for name in sorted_names:
            file.write(name + '\n')

def appendfile(student_id):
    with open('sorted_names.txt', 'a') as file:
        file.write(student_id + '\n')


print("devdom5222") 
sorted_names = readfile()
writefile(sorted_names)
appendfile("devdom5222")
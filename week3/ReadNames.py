print("devdom5222")  

def readfile():
    path = r"C:\Users\ddomi\OneDrive - ECPI University\Desktop\dDominicci_cis_123\names.txt"
    names = []
    fopen = open(path, "r")
    for line in fopen:
        line = line.replace("\n", "")  # Remove the newline character
        names.append(line)
    fopen.close()
    names.sort()  # Sort the names alphabetically
    return names

def writefile(names):
    path = r"C:\Users\ddomi\OneDrive - ECPI University\Desktop\dDominicci_cis_123\sorted_names.txt"
    fopen = open(path, "w")
    for line in names:
        fopen.write(line + "\n")  # Add a newline character after each name
    fopen.close()
    
def appendfile(line):
    path = r"C:\Users\ddomi\OneDrive - ECPI University\Desktop\dDominicci_cis_123\sorted_names.txt"
    fopen = open(path, "a")
    fopen.write(line + "\n")  # Append the line with a newline character
    fopen.close()
    
    
# Call readfile function
names = readfile()
writefile(names)
appendfile("End of file")
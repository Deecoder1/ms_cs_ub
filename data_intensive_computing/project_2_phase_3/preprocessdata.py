file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
file2 = open('myfilemodified.txt', 'w')
for line in Lines:
    node = line.split(' ')[0]
    weight = line.split(' ')[1]
    adj_list = ''
    for j in ((((line.split(' ')[2]).strip()).split(':'))):
        if len((j.split(',')[0])) !=0:
            adj_list += (j.split(',')[0])+':'
    print(node, weight, adj_list[:-1])
    file2.writelines(node+" "+weight+" "+adj_list[:-1])
    file2.writelines("\n")

file2.close()
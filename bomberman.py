print("Welcome to Bomberman! I am your personal assistant.\nPlease " +\
               "decide what files you'd like to open.\n")

input1 = str(raw_input("First file to open: "))
input2 = str(raw_input("Second file to open: "))

print("\n")

file1 = open(input1, 'r')
file2 = open(input2, 'r')

list1 = []
list2 = []

for line in file1:
    list1.append(line.strip())

for line in file2:
    list2.append(line.strip())
x = 0

if len(list1) > len(list2):
    listi = list2
else:
    listi = list1

for x in range(0, len(listi)):
    if list1[x] != list2[x]:
        print(input1 + " has: " + list1[x])
        print(input2 + " has: " + list2[x])
        print("\n")
        x = 1

if x == 0:
    print("Bomberman found no discrepancies between these files.\n")

print("Thank you for using Bomberman! Shutting down now...")

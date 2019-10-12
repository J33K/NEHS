import math
import tkinter
waste_index=[]
tax_index=[]

total=0
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
f = open("database-all", "a+")
s = open("database-waste", "a+")
t = open("database-tax", "a+")
ad = open("database-address", "a+")
address_list = ["6 Ceder Point Ave", "8 Ceder Point Ave", "10 Ceder Point Ave", "5 Kerwin Ave", "7 Kerwin Ave", "16 Ocean View Ave", "18 Ocean View Ave", "20 Ocean View Ave",  "45 Brandt Beach Ave", "47 Brandt Beach Ave", "49 Brandt Beach Ave", "51 Brandt Beach Ave", "53 Brandt Beach Ave", "55 Brandt Beach Ave", "57 Brandt Beach Ave"]
for x in address_list:
    a=int(input('Number ' + x + ' :'))
    print("-----------------------------")
    if a >= 2:
        tax=str(50 * 2 ** (a-2))
    else:
        tax=0
    a = [a]
    tax=[tax]
    waste_index = waste_index + a
    tax_index = tax_index + tax
print()
print()
print()
print("Statistics after updating")
for i in range(len(address_list)):
    print("Address: " + str(address_list[i]))
    print("--------------------------")
    print("Waste: " + str(waste_index[i]) + " trash cans")
    print("--------------------------")
    print("Fine: " + str(tax_index[i]) + " dollars")
    print("--------------------------")


total_waste=0
total_tax=0

for g in range(len(address_list)):
    f.write(str(address_list[g]))
    f.write("\n")
    f.write(str(waste_index[g]))
    f.write("\n")
    f.write(str(tax_index[g]))
    f.write("\n")
print()
print()
for g in range(len(address_list)):
    s.write(str(waste_index[g]))
    s.write("\n")
print()
print()
for g in range(len(address_list)):
    t.write(str(tax_index[g]))
    t.write("\n")
for g in range(len(address_list)):
    ad.write(str(address_list[g]))
    ad.write("\n")
f.close()
s.close()
t.close()
ad.close()
f = open("database-all", "r")
s = open("database-waste", "r")
t = open("database-tax", "r")
ad = open("database-address", "r")
total_waste = 0
searching_tax = 0
counting = 0
list1 = s.read()
list1 = list1.splitlines()
list2 = t.read()
list2 = list2.splitlines()
list3 = []
list4 = ad.read()
list4 = list4.splitlines()
list5 = []
j = 0

for i in list1:
    if RepresentsInt(i):
        j = i
    else:
        j = 0
    total_waste += int(j)
j = 0
for i in list2:
    if RepresentsInt(i):
        total_tax += int(i)
j = 0
for i in list2:
    if RepresentsInt(i):
        if int(i) > 0:
            list3.append(list4[counting])
            list5.append(list2[counting])
    else:
        j = 0
    counting += 1
print("Total waste: " + str(total_waste) + " trash cans")
print()
print("Total revenue gained from fines: " + str(total_tax) + " dollars")
print()
print("Users that must pay fines: " + str(list3) + " Amount to be paid: " + str(list5))




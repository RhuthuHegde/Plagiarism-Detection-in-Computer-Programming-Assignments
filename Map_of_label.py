# converts the csv to dictionary for the dataset
import csv
dict_from_csv = {}

with open('/Users/rhuthuhegde/Desktop/Others/Plagiarism_Dataset_A', mode='r') as inp:
    reader = csv.reader(inp)
    headings = next(reader)
    dict_from_csv = {rows[0]:0 for rows in reader}
print(dict_from_csv)

# makes a list of the assignments which are plagiarised
file1 = open('/Users/rhuthuhegde/Desktop/Others/dynamic_features_assignmentlist.txt', 'r')
Lines = file1.readlines()
label_list=[]


for line in Lines:
	label_list.append(line.strip())

new_list=[]
count=0

for i in range(len(label_list)):
	if count < 896:
		new_list.append('A2016\\'+label_list[count])
		# print(str(i)+' '+'A2016\\'+list[count])
	# elif 897<=count<1023:
	# 	new_list.append('B2016\\' + label_list[count])
	# 	# print(str(i)+' '+'B2016\\'+list[count])
	elif count>=1024:
		new_list.append('A2017\\' + label_list[count])
		# print(str(i)+' '+'A2017\\'+list[count])
	count+=1
# print(len(list)==count)
new_list.pop(0)

for value in new_list:
	if not value in dict_from_csv:
		dict_from_csv[value] = 0
	else:
		dict_from_csv[value] += 1

print(dict_from_csv)
# updates the value in dictionary for the dataset which are plagiarised as 1 and the non plagiarised assignments as 0
for value in new_list:
	if not value in dict_from_csv:
		dict_from_csv[value] = 0
	else:
		dict_from_csv[value] = 1

print(dict_from_csv)

# makes a csv file and stores the labels with assignment names
with open('label_for_A.csv', 'w') as file:
    for key in dict_from_csv.keys():
        file.write("%s,%s\n"%(key,dict_from_csv[key]))
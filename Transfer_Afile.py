import csv
with open('/Users/rhuthuhegde/Desktop/Others/plagiarism_student_dataset.csv', 'r') as f,open('Plagiarism_Dataset_A.csv', 'w') as f_out:
    reader = csv.reader(f)
    writer = csv.writer(f_out)
    lines = list(reader)
    writer.writerows(lines[:1669])
print("The values have been transferred to the csv file")

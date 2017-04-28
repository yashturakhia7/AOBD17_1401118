import xlwt
import xlrd
import sys
import fileinput
import json
import csv

book = xlwt.Workbook()
ws = book.add_sheet('First Sheet')  # Add a sheet

with open('test1.txt', 'r') as file :
  filedata = file.read()

u = ['\u2022', '\u25cf', '\u00ac']
# Replace the target string
filedata = filedata.replace('\u2022', '')
filedata = filedata.replace('\u25cf', '')
filedata = filedata.replace('\u00ac', '')
filedata = filedata.replace('\u2013', '-')
filedata = filedata.replace('\uf0a7', '')
filedata = filedata.replace('\u0219', 's')
filedata = filedata.replace('\u021b', 't')
filedata = filedata.replace('\u2018', "'")
filedata = filedata.replace('\xe9', 'e')
filedata = filedata.replace('\xa3', '')
filedata = filedata.replace('\u2019', "'")
filedata = filedata.replace('\u00e9', 'e')
filedata = filedata.replace('\u0303', '~')
filedata = filedata.replace('\u00f1', 'n')
filedata = filedata.replace('\u00a9', '')
filedata = filedata.replace('\u2026', '...')
filedata = filedata.replace('\u2713', '')
filedata = filedata.replace('\u00a3', '')
filedata = filedata.replace('\u00f6', 'o')
filedata = filedata.replace('\u27a2', '')


# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata)

with open("file.txt", "rb") as fin:
    content = json.load(fin)
with open("stringJson.txt", "wb") as fout:
    json.dump(content, fout, indent=1)
# f = open('stringJson.txt', 'r+')

# data = f.readlines() # read all lines at once
with open("stringJson.txt", "rb") as fin:
	x = json.load(fin)

f = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["CandidateID", "Company", "Job-Description", "Job Title", "Job-Duration",  "Skills", "Additional-Info", "Location", "Institute", "School-Duration", "Qualification", "Resume-Summary"])

for x in x:
    f.writerow([x["CandidateID"],
                x["Work-Experience"]["Company"],
                x["Work-Experience"]["Job-Description"],
                x["Work-Experience"]["Job Title"],
                x["Work-Experience"]["Job-Duration"],
                x["Skills"],
                x["Additional-Info"],
                x["Location"],
                x["Education"]["Institute"],
                x["Education"]["School-Duration"],
                x["Education"]["Qualification"],
                x["Resume-Summary"]])
# for i in range(len(data)):
#   row = data[i].split('", "')  # This will return a line of string data, you may need to convert to other formats depending on your use case
#   for j in range(len(row)):
#     ws.write(i, j, row[j])  # Write to cell i, j
# book.save('test' + '.xls')
# f.close()

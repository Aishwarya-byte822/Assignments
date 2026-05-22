import csv

data = [['Name','Address','Mobile','Email'],
        ['Aish','38 Jagatpura road','789457834','aish1@gmail.com'],
        ['Raj','48 Mansarovar','7865465603','raj2@gmail.com'],
        ['Yash','45 Vaishali','7546835454','yash3@gmail.com']
]
with open('data.csv','w') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)


                

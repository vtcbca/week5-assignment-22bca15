#python program create csv file student.csv(sid,sname,city,contact)
import csv
field=['sid','sname','city','contact']
rows=[1,'om','bardoli',45639],
     [2,'sai','surat',17209],
     [3,'ram','vyara',96864],
     [4,'radhe','bardoli',87564],
     [5,'krishna','navsari',12760]
filename="c:\\sqlite3\\csv\\student.csv"
#insert record through user input
l=[]
for i in range(5):
    no=int(input("Enter id:"))
    name=input("Enter name:")
    city=input("Enter city:")
    contact=int(int(input("Enter contact number:"))
    t=(no,name,city,contact)
    l.append(t)
with open(filename,'w',newline='')as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)
    csvwriter.writerows(1)
#reading dat from csv file.
with open(filename,'r')as csvfile:
    csvreader=csv.reader(csvfile)
    for record in csvreader:
        print(record)
print("Total no.of rows:%d"%(csvreader.line_num))
    
    
    


import csv
import os
output="newContacts.csv"
fields=["Name","Given Name","Additional Name","Family Name","Yomi Name","Given Name Yomi","Additional Name Yomi","Family Name Yomi","Name Prefix","Name Suffix","Initials","Nickname","Short Name","Maiden Name","Birthday","Gender","Location","Billing Information","Directory Server","Mileage","Occupation","Hobby","Sensitivity","Priority","Subject","Notes","Language","Photo","Group Membership","E-mail 1 - Type","E-mail 1 - Value","E-mail 2 - Type","E-mail 2 - Value","E-mail 3 - Type","E-mail 3 - Value","IM 1 - Type","IM 1 - Service","IM 1 - Value","Phone 1 - Type","Phone 1 - Value","Phone 2 - Type","Phone 2 - Value","Address 1 - Type","Address 1 - Formatted","Address 1 - Street","Address 1 - City","Address 1 - PO Box","Address 1 - Region","Address 1 - Postal Code","Address 1 - Country","Address 1 - Extended Address","Organization 1 - Type","Organization 1 - Name","Organization 1 - Yomi Name","Organization 1 - Title","Organization 1 - Department","Organization 1 - Symbol","Organization 1 - Location","Organization 1 - Job Description","Website 1 - Type","Website 1 - Value"]
reply=input(f"Hi {os.getlogin()}, do you want to import a csv file?")
if reply=="yes" or reply=="Yes":
    print("Enter the file name: ")
    file_name=input()
    try:
        with open(file_name) as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            myList={"Name":[],"Type":[],"Number":[]}
            newList={"Name":[],"Type":[],"Number":[]}
            line_count=0
            for row in csv_reader:
                if line_count==0:
                    line_count +=1
                else:
                    row[39]=''.join(row[39].split())
                    row[39]=row[39].replace("+","")
                    row[39]=row[39].replace("-","")
                    print(row[39])
                    if row[39].isnumeric()==True:
                        myList["Name"].append(row[0])
                        myList["Type"].append(row[38])
                        myList["Number"].append(row[39])
                        line_count +=1
            line_count -=1
            c=0
            for i in range(line_count):
                if myList["Number"][i] not in newList["Number"]:
                    newList["Name"].append(myList["Name"][i])
                    newList["Type"].append(myList["Type"][i])
                    if (myList["Number"][i].find("39")!=-1 or myList["Number"][i].find("212")!=-1 ):
                        newList["Number"].append('+'+myList["Number"][i])
                    else:
                        newList["Number"].append(myList["Number"][i])
                    c +=1
            print(f"Number of elements: {c}")
            for i in range(c):
                print(myList["Name"][i],myList["Number"][i])
            duplicate=len(myList["Number"])-len(set(myList["Number"]))
            print("Duplicates: ",duplicate)
        with open(output,'w',newline='') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(fields)
            for i in range(c):
                csvwriter.writerow([newList["Name"][i]]+['']*37+[newList["Type"][i]]+[newList["Number"][i]]+['']*21)
            print("Saved file")
    except:
        print("Error in opening the file")
else:
    print("I hope you liked the programm :)")

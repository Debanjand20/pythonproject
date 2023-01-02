import csv
import re
import matplotlib.pyplot as plt
import numpy as np
def new_batch(batch_id,batch_name,department_name,batch_courselist,batch_studentlist):
    batch_list=[]
    batch_file=open("Batch Data.csv",'r')
    batch_reader=csv.reader(batch_file)
    for row in batch_reader:
        batch_list.append(row)
    batch_file.close()
    batch_coursestr=""
    length=len(batch_courselist)
    for i in range(length-1):
        batch_coursestr=batch_coursestr+batch_courselist[i]+":"
    batch_coursestr=batch_coursestr+batch_courselist[length-1]
    batch_studentstr=""
    length=len(batch_studentlist)
    for i in range(length-1):
        batch_studentstr=batch_studentstr+batch_studentlist[i]+":"
    batch_studentstr=batch_studentstr+batch_studentlist[length-1]
    batch_list.append([batch_id,batch_name,department_name,batch_coursestr,batch_studentstr])
    batch_file=open("Batch Data.csv",'w',newline='')
    csvwriter=csv.writer(batch_file)
    csvwriter.writerows(batch_list)
    batch_file.close()
def studentlist_batch(batch_id,batch_name):
    batch_list=[]
    batch_file=open("Batch Data.csv",'r')
    batch_reader=csv.reader(batch_file)
    for row in batch_reader:
        batch_list.append(row)
    batch_file.close()
    k=0
    length=len(batch_list)
    for i in range(length):
        if((batch_list[i][0]==batch_id)and(batch_list[i][1]==batch_name)):
            std_liststr=batch_list[i][4]
            k=1
    if(k==1):
        std_list=re.split(':',std_liststr)
        student_list=[]
        student_file=open("Student Data.csv",'r')
        student_reader=csv.reader(student_file)
        for row in student_reader:
            student_list.append(row)
        student_file.close()
        length1=len(std_list)
        length2=len(student_list)
        print("Student ID\tClass Roll Number\tStudent Name")
        for i in range(length1):
            for j in range(length2):
                if(std_list[i]==student_list[j][0]):
                    print(student_list[j][0]+"\t\t"+student_list[j][2]+"\t\t\t"+student_list[j][1])
    else:
        print("Batch ID or Batch name is incorrect or Batch does not exist!")
def courselist_batch(batch_id,batch_name):
    batch_list=[]
    batch_file=open("Batch Data.csv",'r')
    batch_reader=csv.reader(batch_file)
    for row in batch_reader:
        batch_list.append(row)
    batch_file.close()
    k=0
    length=len(batch_list)
    for i in range(length):
        if((batch_list[i][0]==batch_id)and(batch_list[i][1]==batch_name)):
            crse_liststr=batch_list[i][3]
            k=1
    if(k==1):
        crse_list=re.split(':',crse_liststr)
        course_list=[]
        course_file=open("Course Data.csv",'r')
        course_reader=csv.reader(course_file)
        for row in course_reader:
            course_list.append(row)
        course_file.close()
        length1=len(crse_list)
        length2=len(course_list)
        print("Course ID\t\tCourse Name")
        for i in range(length1):
            for j in range(length2):
                if(crse_list[i]==course_list[j][0]):
                    print(course_list[j][0]+"\t\t\t"+course_list[j][1])
    else:
        print("Batch ID or Batch name is incorrect or Batch does not exist!")

def performance_batch(batch_id,batch_name):
    batch_list=[]
    batch_file=open("Batch Data.csv",'r')
    batch_reader=csv.reader(batch_file)
    for row in batch_reader:
        batch_list.append(row)
    batch_file.close()
    k=0
    length=len(batch_list)
    for i in range(length):
        if((batch_list[i][0]==batch_id)and(batch_list[i][1]==batch_name)):
            std_liststr=batch_list[i][4]
            crse_liststr=batch_list[i][3]
            k=1
    if(k==1):
        std_list=re.split(':',std_liststr)
        student_list=[]
        student_file=open("Student Data.csv",'r')
        student_reader=csv.reader(student_file)
        for row in student_reader:
            student_list.append(row)
        student_file.close()
        crse_list=re.split(':',crse_liststr)
        course_list=[]
        course_file=open("Course Data.csv",'r')
        course_reader=csv.reader(course_file)
        for row in course_reader:
            course_list.append(row)
        course_file.close()
        length1=len(std_list)
        length2=len(student_list)
        length3=len(crse_list)
        length4=len(course_list)
        print("Class Roll Number\tStudent Name\tPercentage Obtained")
        for i in range(length1):
            for j in range(length2):
                if(std_list[i]==student_list[j][0]):
                    totmarks=0
                    for m in range(length3):
                        for n in range(length4):
                            if(crse_list[m]==course_list[n][0]):
                                stdid_marks_list=re.split(":|-",course_list[n][2])
                                length5=len(stdid_marks_list)
                                for o in range(length5):
                                    if(student_list[j][0]==stdid_marks_list[o]):
                                        totmarks=totmarks+int(stdid_marks_list[o+1])
                    percentage=totmarks/length3
                    print(student_list[j][2]+"\t\t\t"+student_list[j][1]+"\t"+str(percentage))
    else:
        print("Batch ID or Batch name is incorrect or Batch does not exist!")
def pie_batch(batch_id,batch_name):
    batch_list=[]
    batch_file=open("Batch Data.csv",'r')
    batch_reader=csv.reader(batch_file)
    for row in batch_reader:
        batch_list.append(row)
    batch_file.close()
    k=0
    length=len(batch_list)
    for i in range(length):
        if((batch_list[i][0]==batch_id)and(batch_list[i][1]==batch_name)):
            std_liststr=batch_list[i][4]
            crse_liststr=batch_list[i][3]
            k=1
            break
    if(k==1):
        std_list=re.split(':',std_liststr)
        student_list=[]
        student_file=open("Student Data.csv",'r')
        student_reader=csv.reader(student_file)
        for row in student_reader:
            student_list.append(row)
        student_file.close()
        crse_list=re.split(':',crse_liststr)
        course_list=[]
        course_file=open("Course Data.csv",'r')
        course_reader=csv.reader(course_file)
        for row in course_reader:
            course_list.append(row)
        course_file.close()
        length1=len(std_list)
        length2=len(student_list)
        length3=len(crse_list)
        length4=len(course_list)
        a=b=c=d=e=f=0
        for i in range(length1):
            for j in range(length2):
                if(std_list[i]==student_list[j][0]):
                    totmarks=0
                    for m in range(length3):
                        for n in range(length4):
                            if(crse_list[m]==course_list[n][0]):
                                stdid_marks_list=re.split(":|-",course_list[n][2])
                                length5=len(stdid_marks_list)
                                for o in range(length5):
                                    if(student_list[j][0]==stdid_marks_list[o]):
                                        totmarks=totmarks+int(stdid_marks_list[o+1])
                    percentage=totmarks/length3
                    if(percentage>=90):
                        a=a+1
                    elif((percentage<90)and(percentage>=80)):
                        b=b+1
                    elif((percentage<80)and(percentage>=70)):
                        c=c+1
                    elif((percentage<70)and(percentage>=60)):
                        d=d+1
                    elif((percentage<60)and(percentage>=40)):
                        e=e+1
                    elif(percentage<40):
                        f=f+1
        plt.pie(np.array([a,b,c,d,e,f]),labels=['A','B','C','D','E','F'])
        plt.legend()
        plt.show()
    else:
        print("Batch ID or Batch name is incorrect or Batch does not exist!")

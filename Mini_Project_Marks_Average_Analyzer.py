# -*- coding: utf-8 -*-
#Marks Average Analyzer 
#Input
print("-----------------------------------------------------------------------")
numstudents=int(input("Enter no of students:"))

marks1= []   
for i in range(numstudents):
    marks2= int(input("Enter marks of the students: "))
    
    marks1.append(marks2)
    print(marks1)
print("-----------------------------------------------------------------------")

print("1.Calculate Average of marks\n2.Find the highest of the marks\n3.Find lowest of the marks")
print("------------------------------------------------------------------------")

n= int(input("Enter no of the operation from (1,2,or3) of which you want to perform:"))

print("------------------------------------------------------------------------")




#1.Calculate average 
if n==1:
   sum1= sum(marks1)
   average= sum1/numstudents
   print("Average marks of all ",numstudents," students:" ,round(average,3))
   print("------------------------------------------------------------------------")


#2.Finding Highest
elif n==2:
   maximum= max(marks1)
   print("The Highest marks are:",maximum)
   print("------------------------------------------------------------------------")
   
#3.Finding Lowest
elif n==3:
   lowest= min(marks1)
   print("The Lowest marks are:",lowest)
   print("------------------------------------------------------------------------")
   
#4.If conditions are not satisfied 
else:
    print("Enter Correct Number:")
    print("------------------------------------------------------------------------")
    
    




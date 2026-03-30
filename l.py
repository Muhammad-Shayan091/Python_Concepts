# print("My name is shayan.")
# print("and i am 21 years old.")
# print("My dream is to become tourist")
# print("To see the world.")
# print("Not to become old in one job,one country and one type life.")
# print("now i start data analytics")
# print("I learning python programing language , which is used in data science field mostly.")

# # Variables 
# name = "shayan"
# Age = 21
# print("my name is ",name,"and i am ",Age,"years Old")

# # Operations
# num1 = 12
# num2 = 6
# print("Sum of ",num1," and ",num2," is :-> ",num1+num2)
# print("Subtraction of ",num1," and ",num2," is :-> ",num1-num2)
# print("Product of ",num1," and ",num2," is :-> ",num1*num2)
# print("Division of ",num1," and ",num2," is :-> ",num1/num2)
# print("Reminder of ",num1," and ",num2," is :-> ",num1%num2)

# # Updation of a number

# number = 10
# print("Number : ",number)
# number = number + 5
# print("Updated number : ",number)

# # Swap numbers

# number1 = 10
# number2 = 12
# print("number 1 : ",number1)
# print("number 2 : ",number2)
# temp = number1
# number1 = number2
# number2 = temp
# print("After Swaping : ")
# print("number 1 : ",number1)
# print("number 2 : ",number2)

# # age calculation 

# age = 21
# print("My age is : ",age)
# age = age+10
# print("My age after 10 years : ",age)

# # datatypes 

# name = "shayan"
# age = 21
# cgpa = 3.74
# is_Married = False

# print("type of name : ",name," is : ",type(name))
# print("type of Age : ",age," is : ",type(age))
# print("type of CGPA : ",cgpa," is : ",type(cgpa))
# print("type of is_Married : ",is_Married," is : ",type(is_Married))

# print("conversion of int to str : ",age," is : ",type(str(age)))
# print("conversion of float to int : ",cgpa," is : ",type(int(cgpa)))

# # Comparison

# a = 4
# b = 3

# print("a>b",(a > b))
# print("a=b",(a == b))
# print("10<a<50",(10 < a < 50))

# age = 23
# print("Age for vote : ",age > 18)

# # Input Output in python 
# # find average of marks
# sub1 = int(input("Enter marks of subj 1 : "))
# sub2 = int(input("Enter marks of subj 2 : "))
# sub3 = int(input("Enter marks of subj 3 : "))

# Average = (sub1 + sub2 + sub3)/3
# print("Average : ",Average)

# # Find the Area of Rectangle

# length = int(input("Enter length : "))
# width = int(input("Enter width : "))


# area = length * width
# print("Area Of Rectangle : ",area)

# # conversion from celcius to fahrenhite

# Temp_in_Celcius = int(input("Enter temprature : "))

# tepm_in_fahrenhite  = (Temp_in_Celcius*9/5) + 32                 # normal temprature : 37C or 98.6F
# print("Temprature in fahrenhite : ",tepm_in_fahrenhite)

# # find the square and cube of a number

# number = int(input("Enter number : "))
# square = number*number              
# cube = number*number*number                                        # Or cube = square*number
# print("the square of ",number," is :-> ",square,"\nCube of ",number," is :-> ",cube)

# Conditional statement

# # Check whether number is enven or odd

# number = 11

# if(number%2 == 0):
#     print("Number is Even.")
# else :
#     print("Number is Odd.")

# # Check wether number is possitive or negative 

# number = 10

# if(number >= 0):
#     print("number is possitive")
# else:
#     print("number is negative.")

# # Check the largest number between two numbers

# number1 = 5
# number2 = 5
# if(number1 > number2):
#     print("number 1 is greater.")
# elif(number1 < number2):
#     print("number 2 is greater.")
# else:
#     print("Both numbers are equal.")

# # Check the largest among three numbers

# number1 = 5 
# number2 = 4
# number3 = 6

# if(number1 > number2):
#     if(number1 > number3):
#         print("Number 1 is Greater.")
#     else:
#         print("Number 3 is Greater.")
# else:
#     if(number2 > number3):
#         print("Number 2 is Greater.")
#     else:
#         print("number 3 is greater.")

# # Check that its leap year or Not

# Days_in_this_years_february = 28

# if(Days_in_this_years_february == 29):
#     print("Its leap year.")
# else:
#     print("Its not leap year.")

# # Check for vote

# age = int(input("Enter You Age : "))
# if(age >= 18):
#     print("You Can Vote.")
# else:
#     print("You Canot Vote.")

# # Check the Grade Of Students

# marks = int(input("Enter Your Marks : "))

# if(marks >= 90):
#     print("Grade A")
# elif(marks >= 80 and marks < 90):
#     print("Grade B")
# elif(marks >= 70 and marks < 80):
#     print("Grade C")
# else:
#     print("You Are Failed.")

# # Loops logic
# # print number from 1 to 10
# # by while Loop

# # i = 1 
# # while(i<=10):
# #     print(i)
# #     i+=1

# # by for Loop

# for i in range(1 , 11 , 1):
#     print(i) 

# # print Even and odd numbers from 1 to 100

# print("Even numbers : ")
# i = 1
# while(i<=100):
#     if(i % 2 == 0):
#         print(i)
#     i+=1


# print("Odd numbers : ")
# for i in range(1 , 100 , 1):
#     if( i % 2 != 0):
#         print(i)


# # Print the sum of first 10 natural numbers

# sum = 0
# i = 1
# while(i <= 100):
#     sum += i
#     i +=1

# print("Sum : ",sum)

# Table of any number
# number = int(input("Enter number : "))

# ans = 1
# i = 1
# print("Table Of : ",number)
# while(i <= 10):
#     ans = number*i
#     print(number," * ",i," : ",ans)
#     i +=1

# # Count the digits in number

# number = int(input("Enter any number : "))
# count = 0
# while (number != 0):
#     number = int(number/10)
#     count += 1

# print("Digits in numbers : ",count)

# # Reverse a number

# number = int(input("Enter any number : "))

# revers = 0
# while (number != 0):
#     Rem = (number % 10)
#     revers = (revers*10 + Rem)
#     number = int(number/10)

# print("Reverse of number : ",revers)

# # Check the word is pallindrome or not

# string = "madam"
# st = 0
# end = len(string)-1
# while(st < end):
#     if(string[st] != string[end]):
#         print("Word is not pallindrome.")
#         break
#     else:
#         st += 1 
#         end -= 1 
#     if(st >= end):
#         print("Word is Palindrome.")

# # Find the Factorial OF a number

# number = int(input("Enter number : "))
# Real = number
# fact = 1
# while(number != 1):
#     fact *= number
#     number -= 1

# print("Factorial Of : ",Real," is : ",fact)

# # Print fibonacci Series

# first = 0
# second = 1
# target = int(input("Enter nth term : "))
# print(first ,"  ",second, "  ")
# for el in range(2 , target):
#     next = first + second
#     first = second
#     second = next
#     print(next , "  ")

# # to print prime numbers 

# number = int(input("Enter number : "))

# if(number <= 1):
#     print("its non-prime number.")

# for i in range(2 , int(number**0.5)+1):
#     if(number % i == 0):
#         print("number is non prime.")
#         break
#     else:
#         print("number is prime.")

# # String OPeration And practice Question

# string = "Apna college"
# print(len(string))
# count = 0
# for i in range(0 , len(string)):
#     if((string[i] ==  "a" or string[i] == "A") or (string[i] == "e" or string[i] == "E") or (string[i] == "i" or string[i] == "I") or (string[i] == "o" or string[i] == "O") or (string[i] == "u" or string[i] == "U")):
#         count += 1

# print("Wowels in a string : ",string, " : ",count)

# # To Reverse a string
# string = "Shayan Khan"
# print(len(string))
# revers = ""
# for i in range(len(string)-1 , -1 , -1):
#     revers += string[i] 
# print(revers)

# # Check the word is pallindrome or not

# string = "madam"
# st = 0
# end = len(string)-1
# while(st < end):
#     if(string[st] != string[end]):
#         print("Word is not pallindrome.")
#         break
#     else:
#         st += 1 
#         end -= 1 
#     if(st >= end):
#         print("Word is Palindrome.")

# # Count the Occurence of string 

# new_String = "my name is khan."

# for i in range(0 , len(new_String)-1 , 1):
#     print("Occurence of ",new_String[i]," is : ",new_String.count(new_String[i]))

# # Practice Questions Using Built-in Funtions

# new_str = "My name is Muhammad Shayan"

# # Space Reoval 
# new = new_str.replace(" " , "")
# print("String Without Spaces : ",new)

# # To Upper case
# Capital = new_str.upper()
# print("String In Upper Case : ",Capital)

# # To Lower case
# small = new_str.lower()
# print("String in Lower Case : ",small)

# # Type_Swaping
# Swapping = new_str.swapcase()
# print("Case Swapping : ",Swapping)

# # Check the Strings are Anagrams are not 

# str1 = input("Enter String # 1 : ")
# str2 = input("Enter string # 2 : ")

# if(sorted(str1) == sorted(str2)):
#     print("Strings Are Anagrams.")
# else :
#     print("Strings Are not Anagrams.")

# # Find the longest word in a sentence 

# sentence = input("Enter a sntence : ")

# words = sentence.split()                   # use to make list of words
# longest = max(words , key=len)
# smallest = min(words , key=len)

# print("smallest Word in sentence : ",smallest)
# print("Largest Word in sentence : ",longest)

# LISTS IN PYTHON

# # sum of list elements, maximum and minimum element in list.

# new_List = [1,2,3,4,5,6]
# sum  = 1
# max_idx = 0
# min_idx = 0
# for i in range(1 , len(new_List) , 1):
#     sum += new_List[i]
#     if(new_List[i] > new_List[max_idx]):
#         max_idx = i
    
#     if(new_List[i] < new_List[min_idx]):
#         min_idx = i


# print("Sum Of List : ",sum)
# print("Maximum Element : ",new_List[max_idx])
# print("Minimum Element : ",new_List[min_idx])

# # To Remove Duplicate values 

# old_list = [1,2,2,1,3,4,5,5,6,7]
# new_list = list(set(old_list))

# print("Old List : ")
# print(old_list)
# print("updated List : ")
# print(new_list)

# # Write in Ascending & descending Order.

# new_List = [1,2,3,5,2,7,6,9]

# print("Sorted List in Ascending Order : ")
# new_List.sort()
# print(new_List)
# print("Sorted List in descending Order : ")
# new_List.sort(reverse=True)
# print(new_List)

# # Count Even and Odd number in List

# List = [1,2,3,4,5,6,7,8,9]
# even = 0
# odd = 0
# print("Original List : ")
# for i in range(0 , len(List) , 1):
#     if(List[i]%2 == 0):
#         even += 1
#     else :
#         odd += 1

# print("Even elements in List : ",even)
# print("Odd elements in List : ",odd)

# # Reverse A List 
# print("Reversed List : ")
# List.reverse()
# print(List)

# # Another Way

# for i in range(len(List)-1 , -1 , -1):
#     print(List[i] , end=" ")

# # Find the Second Largest Element in list

# List = [1,2,3,7,4,5,5,6]

# largest = List[0]
# sec_Largest = List[0]

# for num in List[1 : ]:
#     if(num > largest):
#         sec_Largest = largest
#         largest = num
#     elif(num > sec_Largest and num != largest):
#         sec_Largest = num
# if(largest == sec_Largest):
#     print("No second Largest element in List.")
# else:
#     print("Second Largest : ",sec_Largest)

# # Merge Two List 

# List1 = [1,2,3]
# List2 = [4,5,6]

# Merge_list = List1 + List2
# print(Merge_list)

# # Check List is Pallindrome

# List = [1,2,3,2,1]
# st = 0
# end = len(List)-1

# while(st < end ):
#     if(List[st] != List[end]):
#         print("List is not Pallindrome")
#         break
#     else :
#         st += 1
#         end -= 1
#     if(st >= end ):
#         print("List Is Pallindrome.")

# # Common Elements in Lists    
# # We Can Make Set From List and Remove Duplicacy and Then Perform Operation Like Union And Intersection 

# List1 = [1,3,4,5,6]
# List2 = [2,3,5,7,8]

# Intersection = list(set(List1) &  set(List2))            # & Is Used For  Intersection
# Union = list(set(List1) | set(List2))                    # | Is Used For Union
# print("INTERSECTION ")
# print(Intersection,"\n")
# print("UNION")
# print(Union)

# Tupples And Sets

# new_tuple = (1,2,3,4,5,6,7,8)

# print("First Tuple : ")
# print(new_tuple)
# print("\nLenth Of tuple : ",len(new_tuple))
# max_idx = 0
# min_idx = 0
# new_list = []
# for i in range(0 , len(new_tuple) , 1):
#     new_list.append(new_tuple[i])
#     if(new_tuple[i] > new_tuple[max_idx]):
#         max_idx = i

#     if(new_tuple[i] < new_tuple[min_idx]):
#         min_idx = i

# print("\nLargest Element In Tuple : ",new_tuple[max_idx])
# print("\nSmallest Element In Tuple : ",new_tuple[min_idx])
# print("\nList by tuple using Loops : ")
# print(new_list)

# # OR Any thing can be Created by Using Data structure name

# print("\nList by tuple using Data Structure Method : ")
# new_list = list(new_tuple)
# print(new_list)
# print("\nset by List : ")
# new_set = set(new_list)
# print(new_set)

# # Set Practice Questions 

# new_set = {1,2,3,4,4,5,5,6,7}
# set2 = {2,4,6,8,10}
# print("Type Of DS : ",type(new_set))
# print("\nLength Of DS : ",len(new_set))
# print("\nSet Elements : ")
# print(new_set)
# print("\nSet no 2 : ")
# print(set2)
# print("\nUnion Of Sets : ")
# print(new_set | set2)
# print("\nIntersection Of Sets : ")
# print(new_set & set2)
# print("\nDifference In Sets : ")
# print(new_set - set2)

# # Find the Target Element in set

# target = int(input("Enter any number : "))
# newlist = list(new_set)
# for i in range(0 , len(newlist) , 1):
#     if(newlist[i] == target):
#         print("Target found in the Given set at index ",i)

# # Dictionaries In Python Practice Questions

# Student = {
#     "name" : "M Shayan",
#     "Marks" : 90
# }

# Course = {
#     "C_name" : "DSA",
#     "Teacher" : "Manzoor"
# }

# Merge = { }
# Merge = Student | Course
# print(Merge)
# print(Student)

# # Key Exist Here or not

# Key_name = input("Enter Key Name : ")
# if Key_name in Student:
#     print("Key  Exist in Dictionary.")
# else:
#     print("Key Not Exist.")

# # Sorting Of Dictionaries

# List = list(Student.items())
# print(List)
# (List.sort())
# Student = dict(List)
# print(Student)

# Funtions In Python 

# # To Add Two Numbers

# def Sum(num1 , num2):
#     return (num1 + num2)

# number1 = int(input("Enter number 1 : "))
# number2 = int(input("Enter number 2 : "))
# Answer = Sum(number1, number2)
# print("Sum : ",Answer)

# Find the Largest number in List Using funtion 
# def Find_max(List):
#     max_idx = 0
#     for i in range(1,len(List) , 1):
#         if(List[i] > List[max_idx]):
#             max_idx = i
#     return List[max_idx]  

# new_list = [1,2,3,4,5]
# print("MAximum Element : ",Find_max(new_list))

# Check Logic Of Prime Numbers
# import math
# def is_Prime(num):
#     if(num <= 1):
#         return False
#     if(num == 2):
#         return 2 
#     if(num % 2 == 0):
#         return False
#     for i in range(3 , int(math.sqrt(num))+1 , 2):
#         if(num % i == 0):
#             return False
#     return True

# number = int(input("Enter Number : "))
# if(is_Prime(number)):
#     print("Number is Prime .")
# else : 
#     print("Number is Composite .")

# To Reverse a string Using Funtion 

# def reverse_str(str):
#     revers = ""
#     for i in range(len(str)-1 , -1 , -1):
#         revers += str[i]
#     return revers
# new_Str = "Shayan"
# print(reverse_str(new_Str))

# # To Calculate Factorial using Funtion 

# def fact(num):
#     fact = 1
#     for i in range(1 , num+1 , 1):
#         fact *= i
#     return fact

# number = int(input("Enter number : "))
# print("Factorial Of : ",number," : is : ",fact(number))

# # To Calculate Marks Average Using Funtion 

# def cal_Average(m1 , m2 , m3):
#     Average = (m1 + m2 + m3)/3
#     return Average

# m1 = int(input("Enter 1st paper Marks : "))
# m2 = int(input("Enter second paper Marks : "))
# m3 = int(input("Enter Third paper Marks : "))
# print("Average Of Three Papers Marks : ",cal_Average(m1 , m2 , m3 ))

# # To Check that the String is Pallindrome or not 

# def is_Pallindrome(str):
#     st = 0
#     end = len(str)-1
#     while(st < end):
#         if(str[st] != str[end]):
#             return False
#             break
#         st += 1
#         end -= 1
#     return True
 
# new_String = "MADAAM"
# if(is_Pallindrome(new_String)):
#     print(new_String," is Pallindrome.")
# else:
#     print(new_String," is not Pallindrome.")

# Count Words in a sentence 

# new_Str = "My name is Khan"
# new_List = new_Str.split()
# print(new_List)
# count = 0
# for i in range(0 , len(new_List) , 1):
#     count += 1

# print("Number Of Words in sentence : ",count)

# # Find Duplicate Elements in list

# new_List = [1,2,3,4,4,5,6,6]
# duplicate = []
# for el in new_List:
#     if new_List.count(el) > 1 and el not in duplicate:
#         duplicate.append(el)

# print(duplicate)

# # Print Pattern
# for i in range (1 , 5 , 1):
#     for j in range (1 , i+1 , 1):
#         print(j ,end=" ")
#     print("\n",end="")

# # Print Pattern

# for i in range (1 , 5 , 1):
#     for j in range (1 , i+1 , 1):
#         print("*",end=" ")
#     print("\n",end="")

# # find the missing number in list from 1 to N

# new_List = []
# sum = 0
# num = int(input("Enter number : "))
# for i in range(1 , num+1 , 1):
#     new_List.append(i) 
#     sum += i

# miss_List = [1,2,3,4,5,6,8,9]
# new_sum = 0
# for el in miss_List:
#     new_sum += el

# Missing_element = sum - new_sum
# print("Missing Element in List : ",Missing_element)











# # PROJECT 1 :-> TO Guess a random number.
# import random 
# Target = random.randint(1,100)

# while True :
#     user_choice = input("Enter Your Number OR Quit :")
#     if (user_choice == "Quit"):
#         print("You Quit the Game.")
#         break
    
#     user_choice = int(user_choice)

#     if(user_choice > Target):
#         print("Target is too small, Enter smaller number.")
#     elif(user_choice < Target):
#         print("Target is Too large, Enter larger number.")
#     else:
#         print("You Guessed the number Correctly.")
#         break

# print("_______Game Over_______")

# # PROJECT 2 :-> Random Password Genration

# import random 
# import string

# Char_Set = string.ascii_letters + string.digits + string.punctuation

# print(Char_Set)

# Password = ""
# for i in range(10):
#     Password += random.choice(Char_Set)

# print("Genrated Random Password :--->  ",Password)



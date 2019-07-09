#!/usr/bin/env python
# coding: utf-8

# In[1]:


# greater among 3 numbers
a1= int(input("enter number 1"))
a2= int(input("enter number 2"))
a3= int(input("enter number 3"))

if a1>a2 and a1>a3:
    print("a1 is the larger number")
elif a2>a1 and a2>a3:
    print("a2 is the larger number")
else:
    print("a3 is the larger number")       


# In[11]:


year= int(input("enter the year"))
if year%400 == 0:
    print("it is leap year")
else:
    print("not a leap year")      leap year or not


# ### Iteration
# * while
# * for
# * Syntax: while Boolean_condition:
#         Statements
#         Increment/Decrement

# In[13]:


x=0
while x<5:
    print("gitam")
    x=x+1


# In[15]:


# N natural numbers using WHILE loop
# input= 10
# output= 1 2 3...10


# In[20]:


n= int(input("enter a number"))
i = 1
while i <= n :
    print(i,end ='')
    i = i + 1


# In[21]:


# READ A NUMBER
# ADD ONLY EVEN NUMS BETWEEN 1 TO 10
# INPUT = 4
# OUTPUT = 2+4=6


# In[1]:


n= int(input("enter a number"))
i = 1
sum = 0
while i <= n:
    if i % 2 == 0:
        sum = sum + i
    i = i+1
print(sum)        


# In[4]:


# Number as Number -- 123
# Print the digits of given number : 3 2 1
n = int(input("enter a number"))
while n!=0:
    r =n%10 
    print(r,end ='')
    n = n // 10    


# In[ ]:


## FUNCIONAL PROGRAMMING
* Simple
* Easy Read
* Lengthy programmes divides into sub programmes.
* syntax : def   name of the fucntion(<parameters>):
* Statement
* return


# In[ ]:


# Read a number -- 1234
# Output -- 6(2+4)
def addEvenDigits(n):
    sum= 0
    while n!=0:
        r = n % 10
        if r % 2 ==0:
            sum =sum + r
            n = n//10        
    return sum
addEvenDigits(1234)   
output: 6


# In[ ]:


n= 2,3,4
print(n)


# In[ ]:


n=1+2**3/4*5
print(n) 


# In[ ]:


# Read a number -- 19528
# Print the large digit print the number
def PrintLarge(n):
    large = 0
    while n!= 0:
        r = n % 10
        if large < r:
            large = r
            n= n // 10
        return large
PrintLarge(19528)
ouput: 9


# In[ ]:


# Read a number Input
# Output reverse of the given number
# 123 -- 321
def ReverseNumber(n):
    return
ReverseNumber(123)


# In[23]:


def reversenumber(n):    
    rev = 0
    while n !=0:
        r = n%10
        rev = rev * 10 + r
        n = n // 10    
    return rev
reversenumber(123)


# In[47]:


# Input
# 123 -- 321 -- no
# 121 -- 121 -- yes
def isPalindrome(n):
    rev = 0
    buffer = n
    while n!=0:
        r=n%10
        rev=rev *10 + r
        n=n // 10
        if buffer == rev:
            return"Yes"
        else:
            return"No"
print(isPalindrome(123))
print(isPalindrome(658))
                


# In[11]:


# Function to print N natural numbers using loop
def printnaturalnumbers(n):
    for x in range(1,n+1):
        print(x,end=" ")
    return
printnaturalnumbers(10)


# In[18]:


# Function to print between two limits
# Input(15,25)
# Output(15,16,17,18....24)
def printseries(lb,ub):
    for x in range(lb,ub):
        print(x,end=" ")
    return
printseries(15,26)


# In[29]:


# Function to print Alternate Numbers
# Intput(200,205)
# Output(201,203,205)
def alternatenumbers(lb,ub):
    for x in range(lb,ub,2):
        print(x,end=" ")
    return
alternatenumbers(200,220)


# In[33]:


# Function to print Series in reverse
# input(5,15)
# output(15,13,11,9,7)
def reverserange(start,end):
    for x in range(end,start,-2):
        print(x,end=" ")
    return
reverserange(5,15)


# img<src jpg.1

# * Problem name
# * Algorithm
# * Sample Input and Output
# * Flowchart 
# * Python Code

# In[3]:


# Given number is prime or not 
def isprime(n):
    flag = True
    for i in range(2,n//2+1):
        if n% i == 0:
            flag = False
            return flag
        return flag
isprime(11)  


# In[24]:


# Function to find prime numbers count from 1 to N
# n=10 --4{2,3,5,7}
def primecount(n):
    cnt = 0
    for a in range(2,n+1):
        k = 0
        for i in range(2,a//2+1):
            if a%i ==0:
                k=k+1
        if(k<=0):      
            cnt=cnt+1
    return cnt
primecount(10)


# In[30]:


# Yes-Individual digit sum factorial sum is same as original number
# example :-
# 145 -- Yes (5!+4!+1! = 145)
# 123 -- No (3!+2!+1! = 9)
def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact
def digitfactsum(n):
    sum = 0
    buffer = n
    while n != 0 :
        r = n% 10
        sum += factorial(r)
        n = n // 10
    if sum == buffer:
        return "Yes"
    else:
        return "No"
    return 
print(digitfactsum(145))
print(digitfactsum(123))


# In[36]:


# Function to return the count of palindrome number two limits
# Input : 1 10
# Output : 9(1,2,3,4,5,6,7,8,9)


# Onput : 11 100
# Output: 9(11,22,33,44......,99)
def ispalindrome(n):
    rev = 0
    buffer = n
    while n!= 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    if rev == buffer:
        return True
    else:
        return False
    return
def countpalindrome(lb,ub):
    cnt = 0
    while lb !=ub:
        # Implement
        if ispalindrome(lb) == True:
            cnt = cnt + 1
        lb = lb + 1
    return cnt
countpalindrome(1,10)


# In[26]:


# Function to generate the Perfect numbers in a given range
# Perfect Number :sum of all its factors same as original number
#Ex: 6 --1 2 3 (1+2+3)
# i/p : 1  10
#o/p : 6

def factorsList(n):
    sum= 0
    for i in range(1,n//2+1):
        if n%i==0:
            sum=sum+i
        
    return sum
def isPerfect(n):
    if factorsList(n) ==n:
        return True
    return False
def generatePerfect(lb,ub):
    for x in range(lb,ub+1):
        if isPerfect(x):
            print(x,end =" ")
    print()
    return
generatePerfect(1,10)
generatePerfect(1,10000)


# In[43]:


s1 = 'python'
print(s1[0])
print(s1[1])
print(s1[2])
print(s1[3])
print(s1[-2])        
print(s1[len(s1)-1])
print(s1[len(s1)-1])


# In[72]:


print(s1[0:2])
print(s1[:2])
print(s1[:3])
print(s1[:-2])
print(s1[-3:])
print(s1[1:-1])
print(s1[len(s1)//2])
print(s1[-1::-1])
print(s1[-1:3:-1])
print(s1[::2]) 
print(s1[::3])
print(s1[-1:2:-1])


# In[84]:


def ispalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
    return
print(ispalindrome("python"))
print(ispalindrome("gamag"))


# In[1]:


def reversestring(str):
    return str[-1::-1]
reversestring("programming")


# In[3]:


ord('A')


# In[38]:


# ASCII
# A-Z : 65-90
# a-z : 97-122
# 0-9 : 48-57
# space: 32
def printupper(x):
    for i in range(len(x)):
        if ord(x[i]) >= 65 and ord(x[i]) <= 90:
            print(x[i])
    return 
printupper("pYThon")


# In[11]:


ord('n')


# In[13]:


ord('4')


# In[63]:


ord('X')


# In[ ]:


# Function to print "samecount" if the count of
# upper and lower case is same
# print "programming" if not same
# example : pyTHon -- 2 TH (uppercase) -- samecount
                   -- 4 pyon (lower case)
          : PyThoN -- 3 PTN (uppercase)
                   -- 3 yho (lowercase)


# In[66]:


ord('a')


# In[67]:


# Function to print "Python" if the count of
# Upper and lower case is same
# Print "Programming" if not same
# ex: PyThOn ---3 P T O (upper case)
#              3 y h n (lower case)
#PytHon --P H (2)
#       --y t o n(4) -Programming


def findCount(str):
    cntUpper =0
    cntLower =0
    for x in range(len(str)):
        if ord(str[x]) >=65 and ord(str[x])<=90:
            cntUpper=cntUpper+1
        elif ord(str[x]) >=97 and ord(str[x])<=122:
            cntLower=cntLower+1
    if cntUpper == cntLower:
        return "SameCount"
    else:
        return "Programming"
    return
print(findCount('PyThOn'))  #SameCount
print(findCount('PYTHon'))  #Programming


# In[68]:


# Extract digits from given string
# Example:
# Input : Appl1icat8ion89
# Output : 1 8 8 9


# In[69]:


# Function to return the sum of digits
# Input : Appli1cat8ion89
# Output : 26(1+8+8+9)
def sumofdigits(str):
    sum = 0
    for x in range(len(str)):
        if ord(str[x]) >= 48 and ord(str[x]) <=57:
            sum=sum + (ord(str[x])-48)
    return sum
sumofdigits('Appli1cat8ion89')        


# In[70]:


# Sum of even digits
def sumofevendigits(str):
    sum = 0
    for x in range(len(str)):
        if ord(str[x]) >= 48 and ord(str[x]) <=57:
            if(ord(str[x])-48) % 2 == 0:   
                sum=sum + (ord(str[x])-48)
    return sum
sumofevendigits('Appli1cat8ion89') 


# In[83]:


def worduppercase(s):
    spaceCnt = 0
    for x in range(len(s)):
        if ord(s[x]) == 32:
            spaceCnt += 1 # spaceCent = spaceCent + 1
        if spaceCnt == 1:
            if ord(s[x]) >=65 and ord(s[x]) <=90:
                print(s[x],end="")
            elif ord(s[x]) >=97 and ord(s[x]) <=122:
                print(chr(ord(s[x])-32),end="")
        if spaceCnt == 2:
            break
    return
worduppercase("Python Made Easy") 


# In[2]:


x = 'gitam engineering college'
print(x[len(x)::-5])


# # Day objectives
# * Python data structures
#  * Lists
#  * Tuples
#  * Dictionaries
# * Basic Program sets on data structures
# * advanced problem set
# * contact application(dictionary object)
# 
# # Data structures
# * To store ,search and Sort the data
# 
# 
# ## pyhton data structures
# ### lists
# * It is one of the common data structures supports by python,the list items are separated by comma operator and enclosed in square brackets
# * example:
#   * list1 = [1,6,2,18,9]
#   * list2 = ["gitam",12,12,15.5,"hyderabad"]
#   
# 

# In[5]:


lst = [1,8,16,9,2]
print(lst)
print(lst[0])
print(lst[1])
print(lst[-1])
print(lst[-2])
print(lst[2])
print(lst[1:])


# In[9]:


# Update the list item values using index(Direct referencing)
li = ["Gitam","Python",1989,2002]
print(li)
li[2] = 2019
print(li)


# In[11]:


# basic list opertaions
lst1 = [1,9,6,18,2]
print(len(lst1))
print(lst1*2)
print(len(lst1))
print(9 in lst1)
print(15 in lst1)


# In[15]:


# basic list opertaions
lst1 = [1,9,6,18,2]
print(len(lst1))
print(lst1*2)
print(len(lst1))
print(9 in lst1)
print(15 in lst1)
for x in range(len(lst1)):
    print(lst1[x],end=' ')


# In[17]:


# Function of the list
lst1
print(min(lst1))
print(max(lst1))
print(sum(lst1))
print(sum(lst1)//len(lst1))
print(sum(lst1[1::2])/len(lst1[1::2]))


# In[ ]:


lst1
lst1.append(24)
lst1
lst1.insert(2,56)
lst1
lst1.count(18)
lst1.index(56)
lst1.sort()
lst1
lst.pop()
lst1
lst1.pop(1)
lst2 = [123,23,45]
lst1.extend(lst2)
lst1
lst1.reverse()
lst1.remove(123)
lst1


# In[42]:


li = [1,9,8,2,6,3]
print(li[-1::-2])


# In[44]:


li = [1,9,8,2,6,3]
print(li[-1:2:-2])


# In[46]:


li = [1,9,8,2,6,3]
print(li[-1:0:-2])


# In[48]:


li = [1,9,8,2,6,3]
print(li[-1:2:-2])


# In[58]:


# Function to find the second large item from the list
# input :   [1,19,6,2,8,18,3]
# output :  18
def secondlarge(li):
    li.sort()
    return li[-2]
def genericlarge(li,n):
    li.sort()
    return li[-n]
li= [1,19,6,2,8,18,3]
genericlarge(li,4)


# In[60]:


# Function to find the least item from the list
# input : [1,19,6,2,8,18,3]
# output : 2
def secondleast(li):
    li.sort()
    return li[1]
def genericleast(li,n):
    li.sort()
    return li[n-1]
li = [1,19,6,2,8,18,3]
genericleast(li,4)


# ### Linear search
# - Linear search algorithm can be applied on duplicate and unique list
#   - Unique list : All items of the list are appeared as only one
#   - Duplicate list : The items of the list can be appeared more than one
# - Linear search algorithm can be applied on sorted list or unsorted list  

# In[63]:


# Function to search the data in a list
# Search is found then return the index if not return -1
def linearsearch1(li,taritem):
    for x in range(len(li)):
        if li[x] == taritem:
            return x
        return -1
li = [1,19,6,2,8,18,3]
linearsearch1(li,225)


# In[82]:


# Function
# Input : [1,5,9,6,5,15,1,2,5],key=5 # Duplicate
# Output : 1 4 8
def linearsearch2(li,taritem):
    for x in range(len(li)):
        if li[x] == taritem:
            print(x,end=" ")
    return 

li = [1,5,9,6,5,15,1,2,5]
linearsearch2(li,5)          


# In[89]:


lst = ['n','b']
print(lst)


# In[99]:


# Function
# Input : List
# Output : Formatted Output
# Test cases :
# [1,6,9,4,16,19,22] --1 9 19 22
def linearsearch6(li):
    # Implement the logic
    for x in range(len(li)):
        if x == 0 or x == len(li) - 1:
            print(li[x],end= " ")
        elif li[x-1] % 2 == 0 and li[x+1] % 2 == 0:
            print(li[x],end=" ")
    return
li = [1,6,9,4,16,19,22]
linearsearch6(li) # 1 9 19 22 


# In[92]:


# Function
# i/p : list
#o/p : seq of characters
# Test case
# [1,5,9,6,5,15,1,2,5],tar=5 --!! !!!!! !!!!!!!!!

def linearSearch3(li,tarItem):
    # Implement the logic
    for x in range(len(li)):
        if li[x] == tarItem:
            j=0
            while j!=x+1:
                print("!",end=" ")
                j=j+1
            print(end=" ")
    return
li = [1,5,9,6,5,15,1,2,5]
linearSearch3(li,5)


# In[94]:


# Function
# i/p: List
# o/p: Formatted
# Test case:
# [12,2,45,9,18,15,36] --60
#A list item which is perfectly multiple of 3 and 5

def linearSearch4(li):
    sum=0
    for x in range(len(li)):
        if li[x] %3 ==0 and li[x] % 5==0 :
            sum += li[x] #sum=sum + li[x]
    return sum
li= [12,2,45,9,18,15,36]
linearSearch4(li)


# In[100]:



# Function
#i/p:list
#o/p:formatted o/p
#test case
#[1,2,3,4,5] --[1,3,8,15,5]
#[6,5,2,8,2] --[6,12,40,4,2]

#1.print first and last as it is because first number does not have previous and last-
 #-does not have next number
#2. need to multiply the previous and next number

def linearSearch5(li):
    for x in range(len(li)):
        if x ==0 or x == len(li) -1:
            print(li[x],end=" ")
        else:
            print(li[x-1]*li[x+1],end=" ")
    return
li =[1,2,3,4,5]
linearSearch5(li)


# ### Number to List
# * Input as Number
# * Expected output will be List

# In[105]:


# Function for Conversion - Number to List
# Input -- Number
# Output -- List
# Test Cases:-
# 14569 -- [1,4,5,6,9]
# 1990 -- [1,9,9,0]
def numberslistconversion(n):
    li = []
    while n != 0:
        r = n % 10
        li.append(r)
        n=n//10
    li.reverse()
    return li
numberslistconversion(14569)#[1,4,5,6,9]


# In[107]:


# Function to count the occurences of a character in a string
# "Python Programming", p-->2
# "Python Programming", m-->2
def countCharOccurances(s,c):
    cnt=0
    for ch in s:
        if ch == c:
            cnt+=1
    return cnt
def countCharOccurances1(s,c): #both functions gives the same output
    return s.count(c)
countCharOccurances("Python Programming",'m')


# In[109]:


# Function to convert the string to list
# test case
# "1,2,3,4,5,6" -- [1,2,3,4,5,6]
def stringtolistconversion(s):
    li = s.split()
    numberslist = []
    for i in li:
        numberslist.append(int(i))
    return numberslist
s = "1 2 3 4 5 6"
stringtolistconversion(s) # [1,2,3,4,5,6]


# ### Sorting Algorithms:
# - Bubble Sort
# - Selection Sort
# - Insertion Sort

# ## Bubble Sort:-
# - This algorithm compares the adj elemets,if the first element is greater
# - Than second element then it is required to swap the elements

# In[110]:


# Function to represent the Bubble sort
def bubblesort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1],li[j]
    return li
li =[19,1,25,6,18,3]
bubblesort(li)


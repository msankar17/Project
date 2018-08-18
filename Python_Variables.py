# This program will help you understand 
#  Variable types in python 2(Num,Str) simple(tuple,list,dict) and 3 compund data types
#   1. Numbers - Integer, Float, Long, Complex
#   2. "String" - Group of characters, indeed like a character array
#   3. (Tuple) -Sequence of any kind data types, data values immutable
#   4. [List] -Sequence of any kind data types, data values can be modified
#   5. {Dictionary} - Seuqence of Key values
# Variable assignments and accessing
# Data type conversions

#Understanding data types & Variable assignment
#----------------------------------------------
vn1 =5 #1.a = Number - Integer
vn2 =5.45 #1.b = Number - Float
#vn3 = 51924351L #1.c = Number - Long
vn4 = 5+1j #1.d = Number - Complex

vs1='String bounded by single quotes'
vs2="String bounded by double quotes"
vs3="""String bounded by triple quotes
which can span across multiple lines"""

vl1=[vn1,vn2,vn4,vs1]
vt1=(vn1,vn2,vn4,vs1)
vd1={"int":vn1,"Float":vn2,"Complex":vn4,'string':vs1,5:7} # Dictionary can have string or integer key and any allowable python type for value
ml1=ml2=5 #You can assign a value to multiple variables at the same time
ml3,ml4=6,7 #You can assign mulitple values to multiple variables at the same time

# Variable assignment and accessing
#----------------------------------
print(ml2) #Normal printing of a Number
print("String concatenated with a number from a variable",ml2) 

print("Prints values from the character array between the indexes - ", vs3[3:7]) 
t1="Sentence 1";t2="sentence 2";t3=t1+t2 # Assign concatenated string to another variable
print(t3) 


print("Tuple index based access",vt1[1:3]) # Access values in a tupe with zero based index.
#vt1[1]="new value" # will throw an error in Python, as tuple cant be modified. Its read only

print("List index based access",vl1[2:]) # Access values in a tupe with zero based index.
vl1[1]="new value"; print("Modified List value -", vl1[1]) # This will work, as list can be modified. 

print("Dictionary access by key ",vd1["Complex"])
print("Print all values in doctionary ",vd1.values())

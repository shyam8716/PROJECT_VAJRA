#Basic if-else questions:
#Write a python program that checks if a number is positive/negative/zero.
a=int(input("enter a value:"))
if a==0:
    print(a,":value is zero")
elif a>0:
        print(a,":value is positive")
elif a<0:
        print(a,":value is negative")
else:
    pass
#Write a program that checks wheather a given number is even/odd.
b=int(input("enter b value:"))
if b%2==0:
      print(b,":value is even")
elif b%1==0:
      print(b,":value is odd")
else:
      pass
#Write a program to determine if a person is eligible to vote (age must be 18 or above).
c=int(input("enter c value:"))
if c>=18:
      print(c,":you are elgible for vote")
elif c==15:
      print(c,":you want to take permission from your parents/guardian")
else:
      print(c,":you are not elgible for vote")
#Write a program that asks the user for a password. If the password is "Python123", print "Access granted", otherwise print "Access denied".
d=str(input("enter d value:"))
print("user name:",d)
e=str(input("enter e value:"))
if e=="python123":
      print("access granted")
else:
      print("access denied")
#If-elif-else statements
#Write a program that checks if a given year is a leap year or not.
f=int(input("enter f value:"))
if  f%400==0:
      print(f,"is a leap year")
elif f%400!=400:
      print(f," is a non leap year")
else:
      print(f,"none of the above")
# Write a program that asks the user to enter marks and assigns grades as follows:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
g=int(input("enter g value:"))
if g<=100 and g==90:
      print(g,"A-TOPPER")
elif g<=80 and g==89:
      print(g,"B-BELOW TOPPER")
elif g<=70 and g==79:
      print(g,"C-AVERGE")
elif g<=60 and g==69:
      print(g,"D-BELOW AVERAGE")
elif g>60:
      print(g,"E-POOR")
else:
      print(g,"F-VERY POOR")

# Write a Python program that takes a temperature input in Celsius and categorizes it as:
# Below 0°C: "Freezing"
# 0-15°C: "Cold"
# 16-30°C: "Warm"
# Above 30°C: "Hot"
h=float(input("enter h value:"))
if  h<0:
      print(h,":Freezing")
elif  h<=15 and h==0:
      print(h,":Cold")
elif h<=30 and h==16:
      print(h, ":Warm")
elif h>30 and h<100:
      print(h,":Hot")
else:
      print(h,":neutral")
# Write a program to calculate BMI using:
# BMI = weight / height²
# BMI < 18.5 → Underweight
# 18.5–24.9 → Normal
# 25–29.9 → Overweight
# 30 or above → Obese
weight=float(input("enter weight value:"))
height=float(input("enter height value:"))
BMI=weight/height*height
if BMI<18.5:
      print(BMI,":UNDERWEIGHT")
elif BMI<=24.9 and BMI<=18.5:
      print(BMI,":NORMAL")
elif BMI<=29.9 and BMI<=25:
      print(BMI,":OVERWEIGHT")
elif BMI>=30:
      print(BMI,":OBESE")
else:
      print(BMI,":VERY OVER OBESR")
#Nested If Questions:
# Write a program that takes three numbers as input and finds the largest among them using nested if statements.
i=int(input("enter i value:"))
j=int(input("enter j value:"))
k=int(input("enter k value:"))
if i>k and i>j:
      print(i,":the largest number")
elif j>k and j>i:
      print(j,":the largest number")
elif k>i and k>j:
      print(k,"the largest number")
else:
      print(":all are equal")
# Write a Python program to check if a person is eligible for a loan. The conditions are:
# Age must be 21 or older
# Monthly salary must be at least $2000
# If salary is below $3000, a guarantor is required
l=str(input("enter l value:"))
m=int(input("enter m value:"))
m1=int(input("enter m1 value:"))
if m>=21 and m1>=2000:
      print(m,": is elgible to take a loan")
      print(m1,":monthly is also elgible for loan")
      print(l,"your loan has been successful")
else:
      print(l,":salary is below $3000, a guarantor is required")
#Logical Operators Questions:
# Write a Python program that checks if a number is divisible by both 3 and 5.
n=int(input("enter n value:"))
if n%3==0 and n%5==0:
      print(n,": is divisible by 3 and 5")
else:
      print(n,"is not divisible by  both 3 and 5")
#Write a program that asks the user for their username and password. If both match the predefined values, print "Login successful"; otherwise, print "Invalid credentials".
user_name="R.Megha Shyam"
pass_word="Shyamu@345"
o=str(input("enter o value:"))
p=str(input("enter p value:"))
if o==user_name and p==pass_word:
      print(o,":user name\n",p,":pass word\n","Login successful")
else:
      print ("Invalid credentials")
#Write a program that checks if a triangle is valid based on the sum of its three angles (should be 180 degrees).
q=int(input("enter q value:"))
r=int(input("enter r value:"))
s=int(input("enter s value:"))
t=q+r+s
if t==180:
      print(t,"triangle is valid based on the sum of its three angles")
else:
      print(t,"triangle is not valid based on the sum of its three angles")
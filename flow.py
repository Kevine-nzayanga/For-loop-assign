# Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50. 
def print_even_numbers():
    i = 0
    while i <= 50:
        if i % 2 == 0:
            print(i)
        i += 1
        continue
print_even_numbers()    
    

# Write a function that takes an integer argument and prints "Prime"
# if the number is prime, and "Not prime" if the number is not prime.
def prime(num):
   if num==1:
      print(f'{num} is not a prime number')
   elif num>1:
      for i in (2,num):
         if num%i==0:
            print(f'{num} is not a prime number')
            break
      else: print(num,'is prime number')

prime(11)      


# Write a function that takes a list of integers as input and prints 
# the sum of all the even numbers in the list.
def sum(nums):
   sum=0
   for x in nums:
      sum+=x
   print(sum)
sum([2,6,8])      

# Write a function that takes any two integers as input, and prints
# the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def inclusive(x,y):
   sum=0
   for a in (x,(y+1)):
      if a%3==0:
         sum+=a
   print(a) 

inclusive(3,9)         
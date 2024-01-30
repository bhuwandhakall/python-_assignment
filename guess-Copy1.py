#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
primes = find_primes(start, end)
print("Prime numbers within the range: ", primes)


# In[1]:


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
primes = find_primes(start, end)
print("Prime numbers within the range: ", primes)


# In[1]:


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
primes = find_primes(start, end)
print("Prime numbers within the range: ", primes)


# In[1]:


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
primes = find_primes(start, end)
print("Prime numbers within the range: ", primes)


# In[ ]:





# In[3]:


def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")


# In[5]:


def generate_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

n = int(input("Enter the number of terms: "))
fibonacci = generate_fibonacci(n)
print("Fibonacci sequence: ", fibonacci)


# In[ ]:


import random

def guess_number():
    number = random.randint(1, 100)
    tries = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        tries += 1
        if guess == number:
            print("Congratulations! You guessed the correct number in", tries, "tries.")
            break
        elif guess > number:
            print("The number is lower.")
        else:
            print("The number is higher.")

guess_number()


# In[ ]:





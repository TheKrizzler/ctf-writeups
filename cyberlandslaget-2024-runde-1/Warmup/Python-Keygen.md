# Challenge
>Prove your code comprehension skills by cracking this key validator!

Author: petterroea

This challenge provides three python scripts in which the goal is to find the value of a variable that makes "gyldig(variable)" return true.

# Solution
## Challenge 1
This first challenge has a bunch of functions that perform various mathematical operations, and the "gyldig()" function only returns true if the result of all these functions is exactly correct.
I could dissect each function and analyze them to figure out the number myself but i would rather have python do it for me, so i simply bruteforced the number after copy-pasting the functions into my own program.
This script prints the number that makes the "gyldig()" function return true.
```
def a(x):
    return x + 5

def b(x):
    return x * 67

def c(x):
    return x % 100

def d(x):
    return x % 2 == 0

def e(x):
    return x // 4

def f(x, y):
    return x % y

def gyldig(tall):
    tall = int(tall)

    return c(f(b(a(tall)), e(tall))) == 13 and d(tall)

for i in range(1,1000): # <- Bruteforce
    try:
        if gyldig(i):
            print(i)
            break
    except:
        continue

> 56 # <- First number in loop which made gyldig() return true
```
## Challenge 2
Challenge 2 provides the following script:
```
def gyldig(verdi):
    a = 0
    b = 0
    for c in verdi:
        if c == '9':
            return False

        if c.isupper():
            a += 1
        
        b += ord(c)

        if c == 'a':
            return False

    return a == 5 and b == 500 and len(verdi) == 10
```
By just looking at it, we can see that "verdi" has to be a string because the function uses the ".isupper()" method on it.
"a" is the amount of capital letters in the string which must be 5, "b" is the sum of ord() of all characters which must be 500, and the string has to be ten characters long.
The hardest part of this challenge is that any combination of only regular letters will cause b > 500. This can be avoided using other characters such as newlines or spaces.  

Lets start the string with 5 newline characters.
```
"\n\n\n\n\n"
```
ord("\n") returns 10, which means that with our current string, b would be equal to 50. The remaining five characters must be capital letters, and the ord() of those five must equal 450.
We can divide 450 by 5 to find out approximately what ord() of each remaining character must be. Luckily for us, 450/5=90, and chr(90) is equal to capital Z.
Therefore, we can fill the remaining five spaces with capital Z's.  

gyldig("\n\n\n\n\nZZZZZ") == True
## Challenge 3
Challenge 3 provides this script:
```
import base64

def gyldig(verdi):
    a = base64.b64decode(verdi).decode("ascii")
    b = a[0:5] + a[-5:-3]
    c = a[7:-10]
    d = a[6] + c[:2] + b
    return d == "hei sveis!"
```
We can see that this function takes a base64 encoded string as parameter, as the parameter is decoded before it is analyzed by the function.
Therefore, we don't really need to worry about the base64 too much. We can just worry about the string, and encode it before we pass it to the function.  

While we could analyze the function to find out exactly where each character has to be in the string, i would rather find a quicker solution. I will modify the function to return the value of "d".
Now i will encode the following string and pass it to the function:  
```
"abcdefghijklmnopqrstuvwxyz"  
```
Now we can see where each character is placed, and simply replace each character of the test-string with whatever character is supposed to go in its place.
Here is the modified function and its output:
```
import base64

def gyldig(verdi):
    a = base64.b64decode(verdi).decode("ascii")
    b = a[0:5] + a[-5:-3]
    c = a[7:-10]
    d = a[6] + c[:2] + b
    return d

print(gyldig(base64.b64encode(b"abcdefghijklmnopqrstuvwxyz").decode()))       # ".decode()" is here to convert the output of ".b64encode" from bytes to string.

> ghiabcdevw # <- Output of modified gyldig(verdi)
```
Now to make the function return "hei sveis!" from the original function, we just swap out the letters of the test-string.
Since the output starts with a "g", we will replace g in the test-string with an "h" (the first letter of "hei sveis!"). Lets do this for all the letters so we end up with this altered version of the test-string:
```
" sveifheijklmnopqrstus!xyz"    # Note: First character is a space.
```
Now we just encode this string to base64, and we have our answer:
```
>>>answer = "IHN2ZWlmaGVpamtsbW5vcHFyc3R1cyF4eXo="
>>>gyldig(base64.b64encode(answer).decode())
True
```

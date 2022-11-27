print("Hello world!") #If I omit one quote, the desired text is not output.
print(1/2) 
print(type(1/2))
print("01") #print(01)->SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
1/(2/3)
print("2 2")

#print(2++2) #2+2
#print(2--2) #2+2
print(2+-2) #2-2
print(2-+2) #2-2

print("\n Exercise 1 \n 1. In a print statement, what happens if you leave out one of the parentheses, or both? \n - It is not printed because it is not in perfect shape. \n 2. If you are trying to print a string, what happens if you leave out one of the quotation marks, or both? \n - same answer with number 1 \n 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2? \n - It mean 2+(+2). ex) 2+-3=2+(-3) \n 4. In math notation, leading zeros are ok, as in 02. What happens if you try this in Python? \n - leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers \n 5. What happens if you have two values with no operator between them? \n - invalid syntax")

mile = 1.61
minute = 60
print("\n Exercise 1.2. Start the Python interpreter and use it as a calculator. \n 1. How many seconds are there in 42 minutes 42 seconds? \n -", minute*42+42) #42minute 42second = 42.7minute, 0.77hour
print("2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile. \n - ", 10/mile) 
print("3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? \n - ", (10/mile)/0.77, "mile/sec, ", (10/mile)/42.7, "mile/min") 
print("What is your average speed in miles per hour? \n - ", (10/mile)/0.77, "mile/hour")
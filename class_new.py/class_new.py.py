from math import sqrt


def calculate(): 
    numbers =[]
    numbers = input("Please type two numbers in one line: ")
    j =0

    for i in range(len(numbers)): 
       if numbers[i] == " ": 
            first = int(numbers[:i])
            second =int(numbers [i:])
            sum_numbers = first + second
            diff = first - second
            
            print("The sum of two numbers is ", sum_numbers, ", The difference of numbers is ", diff )
       j = j+1
       i = i+1
 
#calculate()


#2 Print even numbers between 4 and 30 
def prin_evens():
    odd_numbers = []
    for i in range (4,30):
        if i%2==0: 
            odd_numbers.append(i)
    print(odd_numbers)

#2 Find distance between two poins 
def distance (): 
   x1 = float(input())
   x2 = float(input())
   y1 = float(input())
   y2 = float(input())
   return float(sqrt((pow((x2-x1),2)+pow((y2-y1),2))))


ude
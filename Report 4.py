# Variable
number=0
square=0
odd_number=1

# Input
number = int(input("Enter an integer number between 1 and 100: "))
  
# Process And Output
if 1> number or number > 100:
    print("Input number should be between 1 and 100.")
else:

    print("Square of number", number, "=", end=" ")

    for i in range(number):
        square =square + odd_number
        odd_number =odd_number + 2
        if i < number - 1 :
            print(odd_number - 2, "+", end=" ")
        else:
            print(odd_number - 2, "=", square)
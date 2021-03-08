# fibonacci.py - program that asks an input from the user and returns the fibonacci sequence
# from that inputted number.

# fibonacci function, returns the fibonacci sequence for the given number
def fibonacci(i):
    # set variables
    first = 0
    second = 1
    count = 1
    # if given number is 0, sequence returns 0
    if i == 0:
        print(first)
    # if given number is one, add first + second = 0+1 = 1
    elif i == 1:
        print(first+second)
    # if given number is above one, begin loop to reach the given number while doing the fibonacci sum
    else:
        while count < i:
            # fibonacci sequence, sum part
            fibsum = first + second
            # setting the numbers for the next iteration of the sequence
            first = second
            second = fibsum
            # increment for iteration through loop
            count += 1
        # print result
        print(fibsum)


# main
uInput = int(input("Enter a number: \n"))
# fibonacci sequence cannot occur with a negative number
if uInput < 0:
    print("Error, invalid number")
else:
	# if input =< 0, run fibonacci sequence
    fibonacci(uInput)
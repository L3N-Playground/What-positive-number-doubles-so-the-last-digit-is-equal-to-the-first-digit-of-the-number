#What positive number doubles so the last digit is equal to the first digit of the number?

import time

time_start = time.time()
index_total_numbers = 0

#give a range of numbers
for index_start in range(0,1000):

    #doubles the number of index_start
    index_doubles = index_start * 2

    #return the last digit of index_start as integer
    index_start_last_digit = int(str(index_start)[(len((str(index_start)))-1):])
    #return the first digit of index_doubles as integer
    index_doubles_first_digit = int(str(index_doubles)[0])

    #compares last digit of doubles with first digit of number
    if (index_start_last_digit == index_doubles_first_digit):
        print(index_start,index_doubles)
        index_total_numbers += 1

#output of time required for the programm to finish and total numbers
print("time required: ", time.time() - time_start, "\ntotal numbers found:", index_total_numbers)



import time

def sum_of_range_w_for_loop(N):
    # Complexity O(n)
    # The program execution time condition is not met
    sum = 0
    for i in range(1, N+1):
        sum += i
    return sum

def sum_of_range(N):
    # Complexity O(1)
    if N == 1:
        return 1
    elif N % 2 == 0:
        return (1 + N) * N // 2
    else:
        return (2 + N) * (N-1) // 2 + 1

def calculate_sum():
    while True:
        try:
            while True:
                N = int(input("Enter a positive integer N <= 10^25:\n"))
		        
                if N <= 0 or N > 10 ** 25:
                    print("The number does not meet the specified requirements")
                else:
                    break
            break
        except ValueError:
            print("Incorrect number format")

    start = time.time()

    print("The sum of numbers from 1 to {} is equal to {}".format(N, sum_of_range(N)))   

    print("Program execution time - {} seconds".format(time.time()-start))
	
if __name__ == "__main__":
    calculate_sum()
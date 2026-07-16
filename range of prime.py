# Define the range limits
start = 20
end = 80

print(f"Prime numbers between {start} and {end}:")

# Loop through each number in the range
for num in range(start, end + 1):
    # Prime numbers must be greater than 1
    if num > 1:
        # Check for any factors from 2 up to num - 1
        for i in range(2, num):
            if num % i == 0:
                break  # Not a prime, stop checking
        else:
            # This executes only if the loop finished without hitting 'break'
            print(num, end=" ")


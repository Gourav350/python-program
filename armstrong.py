# Armstrong Number Checker in Python

# Take input from user
num = int(input("Enter a number: "))

# Copy the number for later comparison
temp = num

# Find the number of digits
order = len(str(num))

# Initialize sum
sum_of_powers = 0

# Extract each digit and raise it to the power of 'order'
while temp > 0:
    digit = temp % 10  # Get last digit
    sum_of_powers += digit ** order  # Add digit^order to sum
    temp //= 10  # Remove last digit

# Check if Armstrong
if num == sum_of_powers:
    print(num, "is an Armstrong number ✅")
else:
    print(num, "is NOT an Armstrong number ❌")

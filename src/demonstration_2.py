"""
Given an integer value `n`, write a function that will return a list of the string representation of numbers from 1 to `n`.

However, there are a few additional rules to follow:

- For multiples of three, it should output "Lambda" instead of the number.
- For multiples of five, it should output "School" instead of the number.
- For numbers which are multiples of three and five, it should output "LambdaSchool" instead of the number.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Lambda",
    "4",
    "School",
    "Lambda",
    "7",
    "8",
    "Lambda",
    "School",
    "11",
    "Lambda",
    "13",
    "14",
    "LambdaSchool"
]
"""
def lambda_school(n):
    # Your code here
    output = []

    for number in range(1, n):
        if number % 3 == 0 and number % 5 == 0:
            output.append("lambdaschool")
        elif number % 5 == 0: 
            output.append("School")
        elif number % 3 == 0: 
            output.append("Lambda")
        else:
            output.append(str(number))
    print(output)
    return output

lambda_school(20)

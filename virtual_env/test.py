import argparse

import random
import string

# Function to generate a random string of length n
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
    return result_str

# Create the parser
parser = argparse.ArgumentParser(description="This is my program description")

# Add the parameters
parser.add_argument('-s', '--source', type=str, help='The source parameter for the script')
parser.add_argument('-t', '--target', type=str, help='The target parameter for the script')

# Parse the arguments
args = parser.parse_args()

if not args.source:
    print("No source parameter provided.")
if not args.target:
    print("No target parameter provided.")

# Use the parameter source in your code

concatenated_target = args.target + "_" + generate_random_string(6)

print("The provided source parameter is:", args.source)
print("The provided target parameter is:", concatenated_target)
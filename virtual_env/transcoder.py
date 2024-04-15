import ffmpeg
import argparse
import random
import string
import os

# Function to transcode an mp4 file to an m3u8 file
def transcode_mp4_to_m3u8(input_file, output_file):
  (
    ffmpeg.
    input(input_file).
    output(output_file, format='hls', hls_time=10, hls_list_size=0).
    run()
  )

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

# Define the input and output folders
input_folder = "video_content/source/"

# Create the output folder if it doesn't exist
output_folder = "video_content/output/" + args.target
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Print the parameters
print("The provided source parameter is:", args.source)
print("The provided target parameter is:", concatenated_target)

# ========================================================================
'''
Call the function to transcode the mp4 file to m3u8

Examples:

$ python transcoder.py -s video_001 -t content_001
$ python transcoder.py -s video_002 -t content_002
$ python transcoder.py -s video_003 -t content_003
$ python transcoder.py -s video_004 -t content_004
'''
# ========================================================================
if __name__ == '__main__':
  # format the source and target parameters
  input_file  = input_folder + args.source + ".mp4"
  output_file = output_folder + "/" + concatenated_target +  ".m3u8"
  
  # call the function to transcode the mp4 file to m3u8
  transcode_mp4_to_m3u8(input_file, output_file)
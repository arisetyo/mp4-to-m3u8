import ffmpeg
import argparse
import random
import string
import os

# the path to the batch folder
BATCH_FOLDER = "video_content/agora_batch_1"

# Function to transcode an mp4 file to an m3u8 file
def transcode_mp4_to_m3u8(input_file, output_file):
  (
    ffmpeg.
    input(input_file).
    output(output_file, format='hls', hls_time=10, hls_list_size=0).
    run()
  )

# Function to generate a random string of length n
# DEPRECATED use the source name instead
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
    return result_str

# Create the parser
parser = argparse.ArgumentParser(description="This is my program description")

# Add the parameters
parser.add_argument('-s', '--source',   type=str, help='The source parameter for the script')
parser.add_argument('-t', '--target',   type=str, help='The target parameter for the script')
parser.add_argument('-p', '--playlist', type=str, help='The batch parameter for the script')

# Parse the arguments
args = parser.parse_args()

if not args.source:
    print("No source parameter provided.")
# DEPRECATED
# if no target specified, use the source name
'''
if not args.target:
    print("No target parameter provided.")
'''
if not args.target:
   # Use the parameter source in your code
  target_name = args.source
else:
  target_name = args.target

# source name
source_name = args.source
# playlist shortcode / LP
lp_folder = args.playlist

# Define the input and output folders
input_folder  = BATCH_FOLDER + "/source/" + lp_folder + "/"

# Create the output folder if it doesn't exist
output_folder = BATCH_FOLDER + "/output/" + lp_folder + "/" + target_name
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Print the parameters
print("The provided source parameter is:", source_name)
print("The provided target parameter is:", target_name)
print("The provided playlist parameter is:", lp_folder)

# ========================================================================
'''
Call the function to transcode the mp4 file to m3u8

Examples:

$ python transcoder.py -p lp340906 -s lu477186

'''
# ========================================================================
if __name__ == '__main__':
  # format the source and target parameters
  input_file  = input_folder + source_name + ".mp4"
  # each video will broken down so that's why we create a folder that uses the source name as a folder name
  output_file = output_folder + "/" + target_name +  ".m3u8"
  
  # call the function to transcode the mp4 file to m3u8
  transcode_mp4_to_m3u8(input_file, output_file)
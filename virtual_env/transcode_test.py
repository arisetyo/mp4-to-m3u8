import os
import subprocess

def transcode_mp4_to_m3u8(input_file, output_file):
  # Create output directory if it doesn't exist
  output_dir = os.path.dirname(output_file)
  os.makedirs(output_dir, exist_ok=True)

  if os.path.isfile(input_file):
    # Run FFmpeg command to transcode MP4 to M3U8
    ffmpeg_cmd = f'ffmpeg -i {input_file} -c:v libx264 -c:a aac -hls_time 10 -hls_list_size 0 -hls_segment_filename {output_file} {output_file}.m3u8'
    subprocess.run(ffmpeg_cmd, shell=True)


# Example usage
input_file  = 'virtual_env/video_content/source/input.mp4'
output_file = 'virtual_env/video_content/output'

transcode_mp4_to_m3u8(input_file, output_file)
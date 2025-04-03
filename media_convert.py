import os
import sys
import subprocess
import datetime
import json
from utils import find_media_files, get_output_dir, conversion_log, MEDIA_EXTENSIONS, IMAGE_EXTENSIONS, is_image


def convert_file(input_path, output_format):
    if output_format not in MEDIA_EXTENSIONS + IMAGE_EXTENSIONS:
        print(f'Error: {output_format} is not a supported extension')
        sys.exit(1)
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    orig_name = os.path.splitext(os.path.basename(input_path))[0] #getting the files original name
    output_dir = get_output_dir()
    output_path = os.path.join(output_dir, f'{timestamp}-{orig_name}.{output_format}')


    try:
        if is_image(input_path):
            tool_used = "ImageMagick"
            subprocess.run(['magick', input_path, output_path], check=True, capture_output=True)
        else:
            tool_used = "FFmpeg"
            subprocess.run(['ffmpeg', '-i', input_path, output_path, '-y'], check=True, capture_output=True)

        conversion_log(timestamp, input_path, output_format, output_path, tool_used)
        print(f'Conversion ended successfully')

    except subprocess.CalledProcessError:
        print(f'Failed converting file: {input_path}')

def main():
    if len(sys.argv) < 3:
        print('Usage: python media_convert.py <input_directory_path> <output_format>')
        sys.exit(1)

    input_dir = sys.argv[1]
    output_format = sys.argv[2]
    output_dir = get_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    media_files = find_media_files(input_dir)

    if not media_files:
        print(f'No files to convert in: {input_dir}')
        sys.exit(0)

    for file in media_files:
        convert_file(file, output_format)

if __name__ == '__main__':
    main()
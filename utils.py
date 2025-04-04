import json
import os
import imghdr

#MEDIA_EXTENSIONS = ('.mp4', '.avi', '.mov', '.mkv', '.mp3', '.wav', '.flac')
#IMAGE_EXTENSIONS = ('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'ico', 'svg', 'heic')

def is_image(file_path):
    return imghdr.what(file_path) is not None

def find_media_files(dir_path):
    file_list = []

    for root, _, files in os.walk(dir_path):
        for file in files:
            #if file.lower().endswith(MEDIA_EXTENSIONS + IMAGE_EXTENSIONS):
            file_list.append(os.path.join(root, file))

    return file_list

def get_output_dir():
    return os.getenv("CONVERTED_DIR", os.path.join(os.getcwd(), 'converted_files'))

'''def is_image(file_path):
    return file_path.lower().endswith(IMAGE_EXTENSIONS)'''

def conversion_log(timestamp, input_file, output_ext, output_file, tool_used):
    log_file = os.path.join(get_output_dir(), 'history.json')

    entry = {
        'timestamp': timestamp,
        'input_file': input_file,
        'output_ext': output_ext,
        'output_file': output_file,
        'tool_used': tool_used
    }

    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as f:
            entries = json.load(f)
    else:
        entries = []

    entries.append(entry)

    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=4)

    print("History saved to log")
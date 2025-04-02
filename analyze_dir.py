import sys
import json
import subprocess
import os
from collections import Counter


def analyze_dir(directory_path):
    results = []
    total_chars = total_words = total_lines = 0
    global_char_counter = Counter()
    global_word_counter = Counter()

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            process = subprocess.run([sys.executable, "analyze_file.py", file_path], capture_output=True, text=True) #sys.executable ensures we use the same python interpreter, it returns the path to it
            try:
                file_result = json.loads(process.stdout)
                results.append(file_result)
                total_chars += file_result["char_count"]
                total_words += file_result["word_count"]
                total_lines += file_result["line_count"]
                global_char_counter.update(file_result["most_common_char"])
                global_word_counter.update(file_result["most_common_word"])
            except json.JSONDecodeError:
                continue

    most_common_char = global_char_counter.most_common(1)[0][0] if global_char_counter else None
    most_common_word = global_word_counter.most_common(1)[0][0] if global_word_counter else None

    summary = {
        "total_files": len(results),
        "total_chars": total_chars,
        "total_words": total_words,
        "total_lines": total_lines,
        "most_common_char": most_common_char,
        "most_common_word": most_common_word
    }

    print(json.dumps(summary, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_dir.py <directory_path>")
        sys.exit(1)

    analyze_dir(sys.argv[1])

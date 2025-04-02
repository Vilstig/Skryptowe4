import sys
import json
from collections import Counter

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        return

    lines = content.splitlines()
    words = content.split()
    word_count = len(words)
    line_count = len(lines)

    char_counter = Counter(c for c in content if not c.isspace())
    word_counter = Counter(words)

    char_count = char_counter.total() if char_counter else 0
    most_common_char = char_counter.most_common(1)[0][0] if char_counter else None
    most_common_word = word_counter.most_common(1)[0][0] if word_counter else None

    result = {
        "file_path": file_path,
        "char_count": char_count,
        "word_count": word_count,
        "line_count": line_count,
        "most_common_char": most_common_char,
        "most_common_word": most_common_word
    }

    print(json.dumps(result, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_file.py <file_path>")
        sys.exit(1)
    analyze_file(sys.argv[1])

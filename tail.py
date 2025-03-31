import argparse
import os
import sys
import time
from collections import deque

def tail(stream, lines):
    last_10_lines = deque(stream, lines)
    for line in last_10_lines:
        print(line, end="")

def follow(filename):
    with open(filename, "r", encoding="utf-8") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line:
                print(line, end="")
            else:
                time.sleep(0.5)


def main():
    parser = argparse.ArgumentParser(description="Wyświetla ostatnie n linii z pliku lub wejścia standardowego.")
    parser.add_argument("--lines", type=int, default=10, help="Liczba linii do wyświetlenia")
    parser.add_argument("--follow", action="store_true", help="Śledź zmiany w pliku na żywo")
    parser.add_argument("file", nargs="?", help="Ścieżka do pliku (opcjonalnie)")
    args = parser.parse_args()

    if args.file:
        if os.path.isfile(args.file):
            with open(args.file, "r", encoding="utf-8") as f:
                tail(f, args.lines)
            if args.follow:
                follow(args.file)
        else:
            print(f"Error: File '{args.file}' not found.", file=sys.stderr)
            sys.exit(1)
    elif not sys.stdin.isatty():
        tail(sys.stdin, args.lines)
    else:
        print("Error: No input provided. Please provide a file or use stdin.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

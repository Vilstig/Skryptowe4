import os
import sys


def list_path_dirs():
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    for directory in path_dirs:
        print(directory)


def list_path_exec():
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)

    for directory in path_dirs:
        if os.path.isdir(directory):
            exec = [f for f in os.listdir(directory) if f.lower().endswith(".exe")]
            print(f"{directory}")

            for exe in exec:
                print(f"\t{exe}")
            print()


def main():
    if len(sys.argv) != 2:
        print("Usage: python print_path.py list_dirs | list_exec")
        sys.exit(1)

    if sys.argv[1] == "list_dirs":
        list_path_dirs()
    elif sys.argv[1] == "list_exec":
        list_path_exec()
    else:
        print("Unknown parameter. Use list_dirs or list_exec")
        sys.exit(1)


if __name__ == "__main__":
    main()

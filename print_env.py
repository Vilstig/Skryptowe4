import os
import sys

env_vars = sorted(os.environ.items())

if len(sys.argv) == 1:
    for key, value in env_vars:
        print(f"{key} = {value}")
else:
    filters = sys.argv[1:]

    for key, value in env_vars:
        if any(f.lower() in key.lower() for f in filters):
            print(f"{key} = {value}")

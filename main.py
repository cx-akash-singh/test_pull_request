#password: password
#password: 2nf@1234
password: password
password: password

import os
import sys

def is_valid_path(path):
    # Implement your own validation logic here
    # For example, check if the path is within a certain directory
    allowed_directory = '/path/to/allowed/directory'
    absolute_path = os.path.abspath(path)
    return absolute_path.startswith(os.path.abspath(allowed_directory))

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if is_valid_path(arg):
            try:
                os.remove(arg)
                print(f"Successfully removed {arg}")
            except Exception as e:
                print(f"Error removing file {arg}: {e}")
        else:
            print(f"Invalid file path: {arg}")


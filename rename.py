import os
import argparse
import sys
import re

class bcolors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=str, help="the folder you want to modify [whitespace] into [-]!")
    args = parser.parse_args()

    confirm = input("[*] {color}WARNING{end}: This will rename all your folders (turn whitespaces into -) and filenames under {color}{0}{end}!(And is {color}NOT{end} reversible!!!!!!)\n[*] Are you sure to continue? (press c to continue) ".format(args.folder, color=bcolors.WARNING, end=bcolors.ENDC))

    if confirm != "c":
        print("[-] Exit.")
        sys.exit(0)
    
    print("[*] Start renaming")
    list_ = list(os.walk(args.folder, topdown=False))

    # Bottom-up traversal
    for dir_path, dir_names, file_names in list_:
        for f in file_names:
            modified_f = f.replace(" ", "-")

            original_path = os.path.join(dir_path, f)
            modified_path = os.path.join(dir_path, modified_f)

            os.rename(original_path, modified_path)

        for dir_name in dir_names:
            modified_dir = dir_name.replace(" ", "-")

            original_dir_path = os.path.join(dir_path, dir_name)
            modified_dir_path = os.path.join(dir_path, modified_dir)

            os.rename(original_dir_path, modified_dir_path)

    # Rename the root folder
    modified_root_folder = os.path.basename(os.path.normpath(args.folder)).replace(" ", "-")
    # Note: Parent path will not be modified!
    root_parent = os.path.dirname(os.path.normpath(args.folder))
    os.rename(args.folder, os.path.join(root_parent, modified_root_folder))

    print("[*] End renaming")

if __name__ == "__main__":
    main()

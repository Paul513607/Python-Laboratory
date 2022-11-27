import os
import re


def get_file_matches(root_dir, regex_string):
    regex = re.compile(regex_string)
    matches = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            count_match = 0
            if regex.search(file):
                count_match += 1
            fd = open(os.path.join(root, file), "r")
            if regex.search(fd.read()):
                count_match += 1
            if count_match > 0:
                filename = os.path.join(root, file)
                if count_match == 2:
                    filename = ">>" + filename
                matches.append(filename)
        for mdir in dirs:
            if regex.search(mdir):
                matches.append(os.path.join(root, mdir))
    return matches

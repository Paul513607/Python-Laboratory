import os


def find_text_in_target(target, to_search, callback):
    list_of_files = []
    if os.path.isfile(target):
        try:
            fd = open(target, 'r')
            if to_search in fd.read():
                list_of_files.append(target)
            fd.close()
        except IOError as e:
            callback(e)
    elif os.path.isdir(target):
        for (root, dirs, files) in os.walk(target):
            for file_name in files:
                try:
                    fd = open(os.path.join(root, file_name), 'r')
                    if to_search in fd.read():
                        list_of_files.append(os.path.join(root, file_name))
                    fd.close()
                except IOError as e:
                    callback(e)
    if len(list_of_files) == 0:
        raise ValueError(f"Text {to_search} not found in {target}.")
    return list_of_files

import os


def return_information(my_path):
    if os.path.isfile(my_path):
        try:
            fd = open(my_path, 'r')
            text = fd.read()[:-20]
            fd.close()
            return text
        except IOError as e:
            print(e)
    elif os.path.isdir(my_path):
        extension_dict = {}
        for (root, dirs, files) in os.walk(my_path):
            for file_name in files:
                if file_name.find('.'):
                    file_extension = file_name.split('.')[-1]
                    extension_dict[file_extension] = 1 if file_extension not in extension_dict \
                        else extension_dict[file_extension] + 1
        return extension_dict
    return None

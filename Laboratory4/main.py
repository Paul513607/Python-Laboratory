import ex1, ex2, ex3, ex4, ex5, ex6, ex7, ex8

if __name__ == '__main__':
    try:
        print("ex1: ", ex1.list_extensions('.'))
    except Exception as e:
        print(e)

    try:
        print("ex2: ", ex2.write_filepaths_that_start_with_A('./data', './data/data.txt'))
    except Exception as e:
        print(e)

    try:
        print("ex3: ", ex3.return_information('.'))
        print("ex3: ", ex3.return_information('./data/biden.txt'))
    except Exception as e:
        print(e)

    try:
        print("ex4: ", ex4.list_unique_extensions())
    except Exception as e:
        print(e)

    try:
        print("ex5: ", ex5.find_text_in_target('./data', 'import'))
    except Exception as e:
        print(e)

    try:
        print("ex6: ", ex6.find_text_in_target('./data', 'import', print))
    except Exception as e:
        print(e)

    try:
        print("ex7: ", ex7.get_dict_for_file('./data/my-file.txt.txt'))
    except Exception as e:
        print(e)

    try:
        print("ex8: ", ex8.get_all_files_absolute_paths('.'))
        # x = 1
    except Exception as e:
        print(e)

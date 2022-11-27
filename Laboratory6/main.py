from ex1 import extract_words
from ex2 import get_matches_with_length_x
from ex3 import get_substrings_matching_at_least_one_regex
from ex4 import get_xml_matches
from ex5 import get_xml_matches_v2
from ex6 import censor_vowels_at_start_and_end_of_words
from ex7 import validate_cnp
from ex8 import get_file_matches

if __name__ == '__main__':
    print("ex1: ", extract_words("Hello0, world!"))
    print("\nex2: ", get_matches_with_length_x(r'[a-zA-z0-9]+', "Hello0, world!", 5))
    print("\nex3: ", get_substrings_matching_at_least_one_regex("Hello0, world!", r',', r'[a-z]+'))
    print("\nex4: ", get_xml_matches("./test.html", attrs={"type": "hidden", "name": "area"}))
    print("\nex5: ", get_xml_matches_v2("./test.html", attrs={"type": "hidden", "name": "area"}))
    print("\nex6: ", censor_vowels_at_start_and_end_of_words("Ana are mere."))
    print("\nex7: ", validate_cnp("6221101018683"))
    print("\nex8: ", get_file_matches("./test", "^[A-Z][a-z]*\s+.*\s+\d+\s+.*.py$"))

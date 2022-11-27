import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
import ex8
import ex9

if __name__ == '__main__':
    print("ex1: ", ex1.set_operations({1, 2, 3}, {2, 3, 4}))
    print("\nex2: ", ex2.get_occurences("Ana has apples."))
    print("\nex3: ")
    ex3.compare_dictionaries(
        {
            1: 1,
            2: [1, 2, 3, 4],
            3: {1, 5, 3},
            4: "a",
            6: {
                1: "7",
                2: [1, 2, 5, 4],
            }
        },
        {
            1: 2,
            2: [1, 2, 3, 5],
            3: {1, 2, 3},
            5: "b",
            6: {
                1: 1,
                2: [1, 2, 3, 4],
            }
        })
    print("\nex4: ", ex4.build_xml_element("a", "Hello there", {"href": "http://python.org", "_class": "my-link",
                                                              "id": "someid"}))
    print("\nex5: ", ex5.validate_dict({"key1": "come inside, it's too cold out", "key3": "this is not valid"},
                                     ("key1", "", "inside", "")))
    print("\nex6: ", ex6.get_uniques_and_duplicates([1, 2, 3, 1, 4, 7, 2, 5, 4]))
    print("\nex7: ", ex7.operate_on_sets({1, 2}, {2, 3}, {1, 3}))
    print("\nex8: ", ex8.loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    print("\nex9: ", ex9.my_function(1, 2, 3, 4, x=1, y=2, z=3, t=5))

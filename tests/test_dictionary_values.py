import unittest
from gradescope_utils.autograder_utils.decorators import visibility, partial_credit
from BaseClass import BaseClass

# TODO: create test parameters
test_params = [
    ({}, 'tada'),
    ({'ax': 1, 'by': 2, 'cz': 3}, 'b'),
    ({'apple': 1, 'banana': 2, 'carrot': 3}, 'dog'),
]


max_score = len(test_params)

function_name = "get_dictionary_value" # TODO

# TODO:  name the class according to the function name being tested
class GetDictionaryValue_Test(BaseClass):
    @partial_credit(max_score)
    @visibility('visible')
    def test1(self, set_score=None):
        """get_dictionary_value(options, option)""" # TODO

        student_module = self.student_functions
        total_score = max_score

        for param in test_params:
            if not self.handle_test_print_return_value(param, function_name, "", student_module):
                total_score -= 1
                print("Your function output does not match what's expected\nfor the following input:\n{}".format(param))

        set_score(total_score)
        if total_score == max_score:
            print("Congratulations! You passed this test.")

if __name__ == '__main__':
    unittest.main()


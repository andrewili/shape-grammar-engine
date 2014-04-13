#   rule_steps_model.py

import labeled_shape


class Model(object):
    def __init__(self):
        empty_lshape = labeled_shape.LabeledShape.new_empty()
        self.lshapes = {
            'a': empty_lshape,
            'b': empty_lshape,
            'a_minus_b': empty_lshape,
            'b_minus_a': empty_lshape,
            'c': empty_lshape,
            'c_prime': empty_lshape
        }

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_steps_model_test.txt')

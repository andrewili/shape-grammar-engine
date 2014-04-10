#   rule_steps_model.py

import labeled_shape


class Model(object):
    def __init__(self):
        empty_lshape = labeled_shape.LabeledShape.new_empty()
        self.lshape_a = empty_lshape
        self.lshape_b = empty_lshape
        self.lshape_a_minus_b = empty_lshape
        self.lshape_b_minus_a = empty_lshape
        self.lshapes = {
            'a': self.lshape_a,
            'b': self.lshape_b,
            'a_minus_b': self.lshape_a_minus_b,
            'b_minus_a': self.lshape_b_minus_a
        }

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_steps_model_test.txt')

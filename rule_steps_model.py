#   rule_steps_model.py

import labeled_shape


class Model(object):
    def __init__(self):
        empty_lshape = labeled_shape.LabeledShape.new_empty()
        self.lshape_a = empty_lshape
        self.lshape_b = empty_lshape
        self.lshape_a_minus_b = empty_lshape
        self.lshape_b_minus_a = empty_lshape

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/rule_steps_model_test.txt')

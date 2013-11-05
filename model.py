#   model.py
#   2013-09-18

import sg_labeled_shape


class Model(object):
    def __init__(self):
        self.lshape_a = sg_labeled_shape.SGLabeledShape.new_empty()
        self.lshape_b = sg_labeled_shape.SGLabeledShape.new_empty()
        self.lshape_c = sg_labeled_shape.SGLabeledShape.new_empty()


if __name__ == '__main__':
    import doctest
    doctest.testfile('model_test.txt')

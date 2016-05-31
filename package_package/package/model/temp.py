temp.py


    @classmethod                                ##  2016-02-20 08:58
    def _find_next_shapes_one_rule(rule, current_shape):
        """Receives:
            rule            Rule
            current_shape   Shape
        Finds the next shapes, if any, by applying the rule to the shape. 
        Returns:
            next_shapes     [Shape]. A list of shapes. The list may be empty
        """
        r       = rule
        a       = r.left_shape
        c       = current_shape
        ds      = next_shapes = None

        if _is_a_labeled_point(a):
            ds = _find_next_shapes_from_labeled_point(r, c)
        else if _forms_a_triangle(a):
            ds = _find_next_shapes_from_point_triple(r, c)
        else:
            _report_no_next_shapes()
            ds = []
        return ds
        
    @classmethod
    def _is_a_labeled_point(shape):
        """Receives:
            shape           Shape
        Returns:
            value           boolean. True if the shape consists of a single 
                            labeled point. False otherwise
        """
        value = None
        return value

    @classmethod                                ##  2016-02-20 10:32
    def _find_next_shapes_from_labeled_point(rule, current_shape):
        """Receives:
            rule            Rule. The left shape consists of one labeled point
            current_shape   Shape
        Finds the shapes obtained by applying the rule to the current shape. 
        Returns:
            next_shapes     [Shape]. A list, possibly empty, of shapes
        """
        r = rule
        a = r.left_shape
        c = current_shape
        ds = next_shapes = []

        ts = _find_transformations_of_labeled_point(a, c)
        if ts:
            ds = _find_next_shapes_under_transformations(ts, r, c)
        else:
            _report_no_next_shapes()
            ds = []
        return ds

    @classmethod
    def _forms_a_triangle(shape):
        """Receives:
            shape           Shape
        Returns:
            value           boolean. True if the shape contains at least 3 
                            significant points forming a triangle. False 
                            otherwise
        """
        value = None
        return value

    @classmethod                                ##  2016-02-20 11:35
    def _find_next_shapes_from_point_triple(rule, current_shape):
        """Receives:
            rule            Rule. The left shape contains at least 3 
                            significant points forming a triangle. A 
                            significant point is a labeled point, the end 
                            point of a line, or the intersection of lines
            current_shape   Shape. As for the left shape above
        Finds the next shapes obtained by applying the rule to the current 
        shape. Returns:
            next_shapes     [Shape]. A list, possibly empty, of shapes

        """
        r = rule
        a = r.left_shape
        c = current_shape
        ds = next_shapes = []

        ts = _find_transformations_of_point_triples(a, c)
        if ts == []:
            _report_no_next_shapes()
        else:
            ds = _find_next_shapes_under_transformations(ts, r, c)
        return ds

    @classmethod                                ##  2016-02-20 11:50
    def _find_transformations_of_point_triples(left_shape, current_shape):
        """Receives:
            left_shape          Shape. A shape consisting of lines or labeled 
                                points defining at least 3 significant points
            current_shape       Shape. As for the left shape above
        Returns:
            transformations     [Matrix]. A list, possibly empty, of 
                                transformations t such that t(a) <= c
        """
        a = left_shape
        c = current_shape
        ts = transformations = []

        a_triple = _get_triple(a)
        c_triples = _get_triples(c)
        for c_triple in c_triples:
            t = _get_transformation_of_triples(a_triple, c_triple)
            if t:
                ts.append(t)
            else:
                pass
        return ts

    @classmethod                                ##  2016-02-20 23:58
    def _get_triple(shape):
        """Receives:
            shape               Shape. A shape consisting of lines or labeled 
                                points defining at least 3 significant points
        Returns:
            triple              (Point, Point, Point)
        """

        return triple

    @classmethod                                ##  2016-02-20 12:00
    def _find_next_shapes_under_transformations(
        transformations, rule, current_shape
    ):
        """Receives:
            transformations     [Matrix]. A list of transformations t such 
                                that t(a) <= c
            rule                Rule. A rule a -> b such that t(a) <= c
            current_shape       Shape
        Returns:
            next_shapes         [Shape]. A list of shapes produced by applying 
                                the rule under all the transformations
        """
        a = rule.left_shape
        b = rule.right_shape
        c = current_shape
        ts = transformations
        ds = next_shapes = []

        for t in ts:
            ta = _find_transformation(t, a)
            tb = _find_transformation(t, b)
            d = (c - ta) + tb
            ds.append(d)
        return ds

    ####


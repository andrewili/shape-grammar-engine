class Engine(object):
    def __init__(self):
        pass

    @classmethod
    def find_next_shapes_multiple_rules(cls, current_shape, rules):
        """Receives:
            current_shape   LabeledShape
            rules           [Rule]. A list of rules
        Returns:
            next_shapes_multiple_rules
                            [LabeledShape]. A list of all labeled shapes 
                            gotten by applying all transformations of all 
                            rules to the current labeled shape. May be empty
        """
        c       = current_shape
        r       = rule
        rr      = rules
        dd_r    = next_shapes_one_rule = None
        dd_rr   = next_shapes_multiple_rules = []

        for r in rr:
            dd_r = cls.find_next_shapes_one_rule(c, r)
            dd_rr.extend(dd_r)

        next_shapes_multiple_rules = dd_rr
        return next_shapes_multiple_rules

    @classmethod
    def find_next_shapes_one_rule(cls, shape, rule):
        """Receives:
            shape           LabeledShape
            rule            Rule
        Finds the labeled shapes gotten by applying all transformations of the 
        rule to the current shape. Returns:
            next_shapes     [LabeledShape]. May be empty
        """
        c       = shape
        r       = rule
        a       = rule.left_shape
        b       = rule.right_shape
        d       = next_shape = None
        dd      = next_shapes = None
        t       = transformation = None
        tt      = transformations = None

        tt = cls._find_transformations(c, a)
        dd = []
        for t in tt:
            d = cls._find_next_shape(c, r, t)
            dd.append(d)

        next_shapes = dd
        return next_shapes

    @classmethod
    def _find_transformations(cls, current_shape, left_shape):
        """Receives:
            current_shape   LabeledShape
            left_shape      LabeledShape
        Calculates the transformations under which the left shape is a part of 
        the current shape. Returns:
            transformations [Matrix]. A list of transformations. May be empty
        """
        a       = left_shape
        c       = current_shape
        tt      = transformations = None

        if a.is_labeled_point():
            tt = cls._find_transformations_of_labeled_point(a, c)
        else if a.contains_a_noncollinear_triple():
            tt = cls._find_transformations_by_point_triple(a, c)
        else:
            tt = []

        transformations = tt
        return transformations

    @classmethod
    def _find_transformations_of_labeled_point(
        cls, current_shape, left_shape
    ):
        """Receives:
            current_shape   LabeledShape
            left_shape      LabeledShape. A labeled shape consisting of a 
                            labeled point
        Finds the transformations (actually translations) under which the left 
        shape (i.e., the labeled point) is a part of the current shape. 
        Returns:
            transformations [Matrix]. A list of (translation) matrices. May be 
                            empty
        """
        a       = left_shape
        c       = current_shape
        tt      = transformations = None
        a_lp    = a.best_labeled_point
        c_lpp   = c.labeled_points

        tt = []
        for c_lp in c_lpp:
            t = cls._calculate_translation(a_lp, c_lp)
            tt.append(t)

        transformations = tt
        return transformations

    @classmethod
    def _calculate_translation(cls, lpoint_1, lpoint_2):
        """Receives:
            lpoint_1        Labeled Point. The source point
            lpoint_2        Labeled Point. The target point
        Calculates the translation that moves lp1 to lp2. Returns:
            translation     Matrix
        """
        p1      = lpoint_1.point
        p2      = lpoint_2.point
        t       = translation = None

        translation = p2 - p1
        return translation

    @classmethod
    def _find_transformations_by_point_triple(
        cls, lshape_1, lshape_2
    ):
        """Receives:
            lshape_1        LabeledShape. The source shape. Contains a 
                            noncollinear point triple
            lshape_2        LabeledShape. The target shape. Contains a 
                            noncollinear point triple
        Calculates the transformations under which shape 1 is a part of 
        shape 2. Returns:
            transformations [Matrix]. A list of matrices. May be empty
        """
        trp_1   = lshape_1.best_point_triple
        trp_2   = point_triple_in_lshape_2 = None
        trpp_2  = lshape_2.point_triples
        t       = transformation = None
        tt      = transformations = []

        for trp_2 in trpp_2:
            t = cls._find_transformation_if_any(trp_1, trp_2)
            if t:
                tt.append(t)

        transformations = tt
        return transformations

    @classmethod
    def _find_transformation_if_any(cls, triple_1, triple_2):
        """Receives:
            triple_1        (Point, Point, Point). The source triple
            triple_2        (Point, Point, Point). The target triple
        Calculates the transformation, if any, that takes triple_1 to 
        triple_2. Returns:
            transformation  Matrix, if there is a transformation. Otherwise 
                            None
        """
        tri1    = Triad.new(triple_1)
        tri2    = Triad.new(triple_2)

        if not tri1.is_similar_to(tri2):
            return_value = None
        else:
            transformation = cls._find_transformation(cls, tri1, tri2)
            return_value = transformation
        return return_value

    @classmethod
    def _find_transformation(cls, triad_1, triad_2):
        """Receives:
            triad_1         Triad. The source triad
            triad_2         Triad. The target triad
        Finds the transformation that takes triad_1 to triad_2. Returns:
            transformation  Matrix
        """
        tri1    = triad_1
        tri2    = triad_2
        t1      = cls._find_translation_to_origin(tri1)
        t2      = cls._find_translation_to_origin(tri2)
        t2_inv  = t2.inverse()
        r       = cls._find_rotation(tri1, tri2)
        s       = cls._find_scaling(tri1, tri2)

        transformation = t2_inv * s * r * t1
        return transformation

    @classmethod
    def _find_translation_to_origin(cls, tri1):
        """Receives:
            tri1        Triad
        Finds the translation of the reference vertex to the origin. Returns:
            translation Matrix
        """
        v       = tri1.reference_vertex
        o       = origin = Point.new(0, 0, 0)

        translation = o - v
        return translation

    @classmethod
    def _find_rotation(cls, tri1, tri2):
        """Receives:
            tri1            Triad
            tri2            Triad
        Finds the rotation that takes the reference vector of tri1 to the 
        reference vector of tri2. Clockwise positive. Returns:
            rotation        Matrix
        """
        b1      = tri1.reference_vector.bearing
        b2      = tri2.reference_vector.bearing
        db      = delta_bearing

        db = b2 - b1
        
        rotation = _get_rotation_from_angle(db)
        return rotation

    @classmethod
    def _find_scaling(cls, tri1, tri2):
        """Receives:
            tri1            Triad
            tri2            Triad
        Finds the scaling that takes tri1 to tri2, using the reference vertex 
        as the origin. Returns:
            scaling         Matrix
        """
        l1      = tri1.reference_vector.length
        l2      = tri2.reference_vector.length
        r       = ratio

        r = l2 / l1
        if tri2.is_a_reflection_of(tri1):
            r = -r

        scaling = _get_scaling_from_ratio(r)
        return scaling


    @classmethod
    def _find_next_shape(
        cls, current_shape, rule, transformation
    ):
        """Receives:
            current_shape   LabeledShape
            rule            Rule
            transformation  Matrix
        Applies, under transformation, the rule to the current shape. Returns: 
            next_shape      LabeledShape. May be empty
        """
        a       = rule.left_shape
        b       = rule.right_shape
        c       = current_shape
        d       = next_shape = None
        t       = transformation
        ta      = cls._transform_shape(t, a)
        tb      = cls._transform_shape(t, b)

        d = (c - ta) + tb
        
        next_shape = d
        return next_shape

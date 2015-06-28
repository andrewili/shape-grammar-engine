import rhinoscriptsyntax as rs

class Nakata(object):
    def __init__(self):
        self.class_name = 'Nakata'
        self.zigzag = self._define_zigzag_block()
        self.zigzag_side = 16
        self.zigzag_half_side = self.zigzag_side / 2
        self.prototile_side = self.zigzag_side * 2
        self.prototile_gap_x = 4
        self.prototile_gap_y = 4
        self.prototile_center_center_x = (
            self.prototile_side + self.prototile_gap_x)
        self.prototile_center_center_y = (
            self.prototile_side + self.prototile_gap_y)

    def _define_zigzag_block(self):
        """Defines a zigzag block. Returns:
            name_out        str. The name of the zigzag block
        """
        zigzag_guids = self._draw_zigzag()
        base_point = (8, 8, 0)
        name_in = 'zigzag'
        delete_input = True
        name_out = rs.AddBlock(
            zigzag_guids, base_point, name_in, delete_input)
        return name_out

    def _draw_zigzag(self):
        """Draws a zigzag. Returns:
            line_guids      [guid, ...]. A list of the guids of the lines in 
                            the zigzag
        """
        p1 = (0, 8, 0)
        p2 = (4, 5, 0)
        p3 = (8, 0, 0)
        p4 = (8, 16, 0)
        p5 = (12, 11, 0)
        p6 = (16, 8, 0)
        lines = [
            (p1, p4),
            (p1, p2),
            (p2, p5),
            (p5, p6),
            (p3, p6)]
        line_guids = []
        for line in lines:
            tail, head = line
            line_guid = rs.AddLine(tail, head)
            line_guids.append(line_guid)
        return line_guids

    def draw_prototiles(self):
        """Draws a matrix of prototiles
        """
        n_cells_y, n_cells_x = 16, 16
        for cell_iy in range(n_cells_y):
            for cell_ix in range(n_cells_x):
                t_quad = self._get_t_quad(cell_ix, cell_iy)
                p = self._get_point(cell_ix, cell_iy)
                self._draw_prototile(p, t_quad)

    def _get_t_quad(self, ix, iy):
        """Receives:
            ix              int. 0 <= ix <= 15. The index of (t0, t1)
            iy              int. 0 <= iy <= 15. The index of (t2, t3)
        Returns:
            t_quad          (int, int, int, int). A quadruple of 
                            transformations t, 0 <= t <= 3
        """
        method_name = '_get_t_quad'
        try:
            if not (
                0 <= ix <= 15 and
                0 <= iy <= 15
            ):
                raise ValueError
        except ValueError:
            message = "At least one of the parameters is out of range"
            print("%s.%s\n    %s" % (self.class_name, method_name, message))
            return_value = None
        else:
            base = 4
            t3 = iy % base
            t2 = ((iy - t3) / base) % base
            t1 = ix % base
            t0 = ((ix - t1) / base) % base
            t_quad = (t0, t1, t2, t3)
            return_value = t_quad
        finally:
            return return_value

    def _get_point(self, ix, iy):
        """Receives:
            ix              int. The x-index of a cell
            iy              int. The y-index of a cell
        Returns:
            p               (num, num, num). The coordinates of the center of 
                            the cell (ix, iy)
        """
        # center_center_x = self.prototile_side + self.prototile_gap_x
        # center_center_y = self.prototile_side + self.prototile_gap_y
        x = (self.prototile_center_center_x * ix) + self.zigzag_side
        y = (self.prototile_center_center_y * iy) + self.zigzag_side
        # x = (center_center_x * ix) + self.zigzag_side
        # y = (center_center_y * iy) + self.zigzag_side
        z = 0
        return (x, y, z)

    def _draw_prototile(self, p, t_quad):
        """Receives:
            p               Point3d
            t_quad          (int, int, int, int). A quadruple of 
                            transformations t, 0 <= t <= 3
        Draws, at the position (x, y), the prototile composed of the 4 zigzags 
        under the 4 transformations of t_quad
        """
        t0, t1, t2, t3 = t_quad
        half_side = self.zigzag_half_side
        p0 = rs.PointAdd(p, (-half_side, half_side, 0))
        p1 = rs.PointAdd(p, (half_side, half_side, 0))
        p2 = rs.PointAdd(p, (-half_side, -half_side, 0))
        p3 = rs.PointAdd(p, (half_side, -half_side, 0))
        self._insert_zigzag(p0, t0)
        self._insert_zigzag(p1, t1)
        self._insert_zigzag(p2, t2)
        self._insert_zigzag(p3, t3)

    def _insert_zigzag(self, p, t):
        """Receives:
            p               Point3d
            t               int: {0 | 1 | 2 | 3}. A transformation, where 
                                0: identity
                                1: (vertical) reflection
                                2: (90 degree) rotation
                                3: reflection and rotation as above
        Inserts a zigzag block at point p under transformation t
        """
        insertion_point = p
        reflect_no = [1, 1, 1]
        reflect_yes = [-1, 1, 1]
        rotate_no = 0
        rotate_yes = 90
        if t == 0:
            scale = reflect_no
            angle = rotate_no
        elif t == 1:
            scale = reflect_yes
            angle = rotate_no
        elif t == 2:
            scale = reflect_no
            angle = rotate_yes
        elif t == 3:
            scale = reflect_yes
            angle = rotate_yes
        else:
            pass
        rs.InsertBlock(self.zigzag, insertion_point, scale, angle)



    # def show_prototiles(self):
        # """Draws an n x m matrix of prototiles
        # """
        # n, m = 16, 16
        # i, j = 0, 0
        # for i in range(n):
        #     for j in range(m):
        #         xi, yj = i * offset_x, j * offset_y
        #         transformation_ij = self._get_transformation(i, j)
        #         self.draw_quartet_at_place(xi, yj, transformation_ij)

    # def _get_transformation(self, i, j):
        # """Receives:
        #     i               int. The x-index of the matrix cell
        #     j               int. The y-index of the matrix cell
        # Returns:
        #     (t1, t2, t3, t4)
        #                     A 4-tuple of the transformations of the 4 zigzags, 
        #                     transformation: (reflection, rotation)
        # """
        # return transformation_ij

    # def draw_quartet_at_place(self, x, y, transformations):
        # """Receives:
        #     x               Point3D. The x-value of the base point
        #     y               Point3D. The y-value of the base point
        #     transformations (xform, xform, xform, xform)
        # Draws a quartet of zigzags with the specified transformations
        # """
        # pass


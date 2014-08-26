#   make-grid.py

import rhinoscriptsyntax as rs

def draw_grid():
    """Prompts for the number of cells and the length of each side.
    Draws the grid, with labels
    But first, 4 x 4 cells, 10 units on a side
    """
    nx_cells = 5
    ny_cells = 5
    dx_cell = 10
    dy_cell = 10
    dx_grid = dx_cell * nx_cells
    dy_grid = dy_cell * ny_cells

    def make_points():
        points = []
        for ix in range(1, nx_cells + 1):
            for iy in range(1, ny_cells + 1):
                point = [dx_cell * ix, dy_cell * iy, 0]
                points.append(point)
        return points

    points = make_points()

    def draw_hor_lines():
        for i in range(nx_cells + 1):
            y = dy_cell * i
            p1 = [0, y, 0]
            p2 = [dx_grid, y, 0]
            rs.AddLine(p1, p2)

    def draw_vert_lines():
        for i in range(ny_cells + 1):
            x = dx_cell * i
            p1 = [x, 0, 0]
            p2 = [x, dy_grid, 0]
            rs.AddLine(p1, p2)

    def draw_hor_labels(points):
        offset_x, offset_y, offset_z = -1, 1, 0
        for p in points:
            x, y, z = p
            p_offset = [
                x + offset_x, 
                y + offset_y, 
                z + offset_z]
            rs.AddTextDot('a', p_offset)

    def draw_vert_labels(points):
        offset_x, offset_y, offset_z = -1, -1, 0
        for p in points:
            x, y, z = p
            p_offset = [
                x + offset_x, 
                y + offset_y, 
                z + offset_z]
            rs.AddTextDot('a', p_offset)

    draw_hor_lines()
    draw_vert_lines()
    draw_hor_labels(points)
    draw_vert_labels(points)


draw_grid()
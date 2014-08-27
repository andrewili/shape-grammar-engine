#   draw_grid_w_markers.py

import rhinoscriptsyntax as rs

def draw_grid_w_markers():
    """Draws a grid of 4 x 4 cells, 10 units on a side. Uses (graphic markers,
    not labels.
    """
    nx_cells = 5
    ny_cells = 5
    dx_cell = 10
    dy_cell = 10

    dx_grid = dx_cell * nx_cells
    dy_grid = dy_cell * ny_cells

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

    def make_hor_points():
        hor_points = [
            [dx_cell * ix, dy_cell * iy, 0] \
                for ix in range(1, nx_cells + 1) \
                for iy in range(1, ny_cells)]
        return hor_points

    def make_vert_points():
        vert_points = [
            [dx_cell * ix, dy_cell * iy, 0] \
                for ix in range(1, nx_cells) \
                for iy in range(1, ny_cells + 1)]
        return vert_points

    def draw_hor_markers():
        points = make_hor_points()
        offset_x, offset_y, offset_z = -2, 1, 0
        for p0 in points:
            x, y, z = p0
            p1 = [
                x + offset_x,
                y + offset_y,
                z + offset_z
            ]
            rs.AddLine(p0, p1)

    def draw_vert_markers():
        points = make_vert_points()
        offset_x, offset_y, offset_z = -1, -2, 0
        for p0 in points:
            x, y, z = p0
            p1 = [
                x + offset_x, 
                y + offset_y, 
                z + offset_z]
            rs.AddLine(p0, p1)

    draw_hor_lines()
    draw_vert_lines()
    draw_hor_markers()
    draw_vert_markers()

draw_grid_w_markers()

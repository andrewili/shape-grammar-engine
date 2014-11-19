#   draw_lpoint.py

import rhinoscriptsyntax as rs

def draw_lpoint():
    text = rs.GetString('Enter the label text')
    point = rs.GetPoint('Select the point')
    label = draw_label(text, point)
    point_marker = draw_point_marker(point)
    make_group([label, point_marker])

    # prompt_for_label = 'Enter the label'
    # text = rs.GetString(prompt_for_label)
    # prompt_for_point = 'Select the point'
    # point = rs.GetPoint(prompt_for_point)
    # height = 2
    # lpoint = rs.AddText(text, point, height)
    # radius = 0.5
    # sphere = rs.AddSphere(point, radius)
    # group = rs.AddGroup()
    # rs.AddObjectsToGroup([lpoint, sphere], group)

def draw_label(text, point):
    height = 2
    label = rs.AddText(text, point, height)
    return label

def draw_point_marker(point):
    radius = 0.5
    point_marker = rs.AddSphere(point, radius)
    return point_marker

def make_group(guids):
    group = rs.AddGroup()
    rs.AddObjectsToGroup(guids, group)

if __name__ == '__main__':
    draw_lpoint()

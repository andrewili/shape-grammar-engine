#   play_text.py

import draw_lpoint
import array
import rhinoscriptsyntax as rs

def play_text():
    draw_lpoint.draw_lpoint()
    annotation = rs.GetObject('Select object', rs.filter.annotation)
    point = rs.TextObjectPoint(annotation)
    label = rs.TextObjectText(annotation)
    print('object type: %s' % type(point))
    point_type = type(point)
    if point_type == list:
        print('point type is list')
    elif point_type == tuple:
        print('point type is tuple')
    elif point_type == array.array:
        print('point type is array')
    # elif point_type == Point:
    #     print('point type is Point')
    else:
        print('point type is something else')
    print('len(point): %i' % len(point))
    x, y, z = point[0], point[1], point[2]
    print('coords: (%s, %s, %s)' % (x, y, z))
    print('point: %s' % point)
    print('label: %s' % label)
    
if __name__ == '__main__':
    play_text()
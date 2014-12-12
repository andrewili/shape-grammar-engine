#   get_guids.py

import rhinoscriptsyntax as rs

def get_guids():
    message = 'Select objects, including frame'
    guids = rs.GetObjects(message)
    return guids

def get_guids_on_layer(layer_name):
    guids = rs.ObjectsByLayer(layer_name)
    return guids

def print_info(guid):
    curve = 4
    block = 4096
    object_type = rs.ObjectType(guid)
    if object_type == curve:
        string = get_curve_info(guid)
    elif object_type == block:
        string = get_block_info(guid)
    print(string)

def get_curve_info(guid):
    curve_string = 'curve'
    return curve_string

def get_block_info(guid):
    insertion_point = rs.BlockInstanceInsertPoint(guid)
    block_string = 'block: insertion point: %s' % insertion_point
    return block_string

# guids = get_guids()
# for guid in guids:
#     print_info(guid)

left_guids = get_guids_on_layer('left')
for guid in left_guids:
    print_info(guid)

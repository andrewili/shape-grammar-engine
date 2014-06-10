import rhinoscriptsyntax as rs

selected_objects = rs.GetObjects(
    'Select objects', rs.filter.curve + rs.filter.textdot)
print(type(selected_objects))
print('number of objects: %i' % len(selected_objects))
for object in selected_objects:
    object_type = rs.ObjectType(object)
    print('type: %s' % object_type)
#   test_text.py

import rhinoscriptsyntax as rs

def test_text():
    draw_lpoint()
    prompt = 'Select some objects, OK?'
    guids = rs.GetObjects(prompt)
    print('Number of objects: %i' % len(guids))
    for guid in guids:
        if rs.IsText(guid):
            text = rs.TextObjectText(guid)
            print('object is text: %s' % text)
        else:
            print('object not text')
    
def draw_lpoint():
    prompt_for_label = 'Enter the label'
    text = rs.GetString(prompt_for_label)
    prompt_for_point = 'Select the point'
    point = rs.GetPoint(prompt_for_point)
    height = 2
    lpoint = rs.AddText(text, point, height)
    radius = 0.5
    sphere = rs.AddSphere(point, radius)
    group = rs.AddGroup()
    rs.AddObjectsToGroup([lpoint, sphere], group)
    
if __name__ == '__main__':
    test_text()

from package.scripts import grammar as g
import rhinoscriptsyntax as rs

def clear_groups():
    groups = rs.GroupNames()
    if not groups:
        print('No groups to clear')
        groups = []
    for group in groups:
        group_deleted = rs.DeleteGroup(group)
        print('%s deleted: %s' % (group, group_deleted))

g.Grammar.clear_all()
clear_groups()
print('Number of groups (GroupCount): %i' % rs.GroupCount())
        ##  GroupCount seems to show the past, not the present
print('Groups: %s' % rs.GroupNames())
        ##  GroupNames appears to show the present
names = rs.GroupNames()
if not names:
    names = []
n_names = len(names)
print('Number of groups(len(GroupNames)): %i' % n_names)
group = 'kilroy'
group_out = rs.AddGroup(group)
print('New group: %s' % group_out)
print('Groups: %s' % rs.GroupNames())
print('%s is a group: %s' % (group_out, rs.IsGroup(group_out)))
print('%s is empty: %s' % (group_out, rs.IsGroupEmpty(group_out)))
        ##  IsGroupEmpty appears to return IsGroupNonEmpty
p1, p2 = (0, 0, 0), (20, 20, 0)
line = rs.AddLine(p1, p2)
rs.AddObjectToGroup(line, group)
print('line added to %s' % group_out)
print('%s is empty: %s' % (group_out, rs.IsGroupEmpty(group_out)))

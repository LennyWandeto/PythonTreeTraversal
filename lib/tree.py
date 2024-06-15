class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    allnodes = [self.root]
    while allnodes:
      node = allnodes.pop()
      if node['id'] == id:
        return node
      allnodes = allnodes + node['children']
    return None
    pass

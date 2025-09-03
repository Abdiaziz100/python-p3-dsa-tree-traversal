class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if self.root is None:
            return None
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.get('id') == id:
                return node
            for child in reversed(node.get('children', [])):
                stack.append(child)
        return None
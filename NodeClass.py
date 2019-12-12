class Node:
    total_number_of_levels = 0
    def __init__(self, parent, is_child, key, level):
        self.parent = parent
        self.is_child = is_child
        self.key = key
        self.level = level
        if(level > Node.total_number_of_levels):
            Node.total_number_of_levels = level
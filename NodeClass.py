class Node:
    total_number_of_levels = 0
    def __init__(self, parent, is_child, key, level, is_rectangle, number_of_children = 0, posX = 0):
        self.parent = parent
        self.is_child = is_child
        self.key = key
        self.level = level
        self.number_of_children = 0
        self.posX = 0
        self.is_rectangle = is_rectangle
        if(level > Node.total_number_of_levels):
            Node.total_number_of_levels = level
from NodeClass import Node
import networkx as nx
import matplotlib.pyplot as plt
import functools
def cmp(node1, node2):
    if node1.level < node2.level:
        return -1
    elif node1.level > node2.level:
        return 1
    else:
        if node1.parent <= node2.parent:
            return -1
        else:
            return 1
def draw(nodes):
    y_step = -2
    x_step = 1
    level_pos = []
    max_level = 0
    for i in range (len(nodes)):
        if nodes[i].level > max_level:
            max_level = nodes[i].level
        print(nodes[i].key)
    # nodes = sorted(nodes, key=functools.cmp_to_key(cmp))
    for i in range(max_level + 1):
        level_pos.append([-50,y_step * i])
    G=nx.Graph()
    counter = 0
    for node in nodes:
        if node.is_rectangle == 0:
            shape = "o"
        else:
            shape = "s"
        if node.parent != -1:
            x = nodes[node.parent].posX + nodes[node.parent].number_of_children - 1
            nodes[node.parent].number_of_children += 1
        else:
            x = 0
        pos = (max(x, level_pos[node.level][0]), level_pos[node.level][1])
        node.posX = max(x, level_pos[node.level][0])
        level_pos[node.level][0] = max(x, level_pos[node.level][0]) + x_step
        G.add_node(counter, s = shape, pos = pos, label  = node.key)
        if node.parent >= 0:
            G.add_edge(counter, node.parent)
        counter = counter + 1


    # visited = [0 * len(nodes)]
    # nodes_added = 0
    # node_no = 0
    # while nodes_added < len(nodes):
    #     node_no = counter
    #     while nodes[counter].parent != -1:
    #         if visited[nodes[counter].parent] == 0:
    #             counter = nodes[counter].parent
    #         else:
    #             break
    #     node = nodes[counter]
    #     visited[counter] = 1

    #     if node.is_rectangle == 0:
    #         shape = "o"
    #     else:
    #         shape = "s"
    #     if node.parent != -1:
    #         x = nodes[node.parent].posX + nodes[node.parent].number_of_children - 1
    #         nodes[node.parent].number_of_children += 1
    #     else:
    #         x = 0
    #     pos = (max(x, level_pos[node.level][0]), level_pos[node.level][1])
    #     node.posX = max(x, level_pos[node.level][0])
    #     level_pos[node.level][0] = max(x, level_pos[node.level][0]) + x_step
    #     G.add_node(nodes_added, s = shape, pos = pos, label  = node.key)
    #     if node.parent >= 0:
    #         G.add_edge(nodes_added, node.parent)

    #     nodes_added += 1
    #     if visited[node_no] == 0:
    #         counter = node_no
    #     else:
    #         counter = node_no + 1
    pos = {}
    shape = {}
    label = {}
    pos = nx.get_node_attributes(G,"pos")
    shape = nx.get_node_attributes(G,"s")
    label = nx.get_node_attributes(G,"label")
    # print(G.nodes)
    nx.draw(G, pos,node_shape = "s", nodelist = [sNode[0] for sNode in filter(lambda x: x[1]["s"]=="s",G.nodes(data = True))], node_color="k", node_size = 900)
    nx.draw(G, pos,node_shape = "o", nodelist = [sNode[0] for sNode in filter(lambda x: x[1]["s"]=="o",G.nodes(data = True))], node_color = "k", node_size = 900)
    nx.draw_networkx_labels(G,pos,labels=label,font_size=8,font_color='r', font_weight="bold")
    plt.show()
# nodes = []
# nodes.append(Node(-1, -1, "read\n(x)", 1, 1))          #0
# nodes.append(Node(0, 0, "if", 1, 1))                   #1
# nodes.append(Node(1, 1, "op\n(<)", 2, 0))              #2
# nodes.append(Node(2, 1, "const\n(0)", 3, 0))           #3
# nodes.append(Node(2, 1, "id\n(x)", 3, 0))              #4
# nodes.append(Node(1, 1, "assign\n(fact)", 2, 1))       #5
# nodes.append(Node(5, 1, "const\n(1)", 3, 0))           #6
# nodes.append(Node(5, 0, "repeat", 2, 1))               #7
# nodes.append(Node(7, 1, "assign\n(fact)", 3, 1))       #8
# nodes.append(Node(8, 1, "op\n(*)", 4, 0))              #9
# nodes.append(Node(9, 1, "id\n(fact)", 5, 0))           #10
# nodes.append(Node(9, 1, "id\n(x)", 5, 0))              #11
# nodes.append(Node(8, 0, "assign\n(x)", 3, 1))          #12
# nodes.append(Node(12, 1, "op\n(-)", 4, 0))             #13
# nodes.append(Node(13, 1, "id\n(x)", 5, 0))             #14
# nodes.append(Node(13, 1, "const\n(1)", 5, 0))          #15
# nodes.append(Node(7, 1, "op\n(=)", 3, 0))              #16
# nodes.append(Node(16, 1, "id\n(x)", 4, 0))             #17
# nodes.append(Node(16, 1, "const\n(0)", 4, 0))          #18
# nodes.append(Node(7, 0, "write", 2, 1))                #19
# nodes.append(Node(19, 1, "id\n(fact)", 3, 0))          #20
# draw(nodes)
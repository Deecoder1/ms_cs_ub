import sys

for line in sys.stdin:
    line = line.strip().split('\t')

    node, distance = line[0], line[1]
    # Set neighbours variable only if the node has some
    if len(line) > 2 and line[2] != "0":
        neighbours = line[2]
    else:
        neighbours = 0

    # Propagate computed path at previous step, or set beginning of path
    if len(line) == 4:
        path = line[3]
    else:
        path = node


    try:
        distance = int(distance)
    except Exception as ex:
        # Skip node
        continue

    # Print complete node to keep the graph structure for future iterations
    print '%s\t%s\t%s\t%s' % (node, distance, neighbours, path)

    # If the node has no childs, there is nothing left to do.
    if neighbours!= 0:
        neighbour_buff = neighbours.strip()
        neighbours = neighbour_buff.split(',')

        # For each neighbor, print its updated distance to the source node
        for neighbour in neighbours:
            child_node, child_distance = neighbour.strip().split(':', 1)

            try:
                child_distance = int(child_distance)
            except Exception as e:
                continue

            child_distance += distance
            child_path = '{}>{}'.format(path, str(child_node))

            print '%s\t%s\t%s' % (child_node, child_distance, child_path)
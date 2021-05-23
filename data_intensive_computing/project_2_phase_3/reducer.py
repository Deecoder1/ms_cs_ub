#!/usr/bin/python

import sys

current_dist, current_node, current_path, current_neighbours = None, None, None, 0

for line in sys.stdin:
    line = line.strip().split('\t')

    if len(line) < 3:
        # Line wrongly formatted, abort.
        continue

    node, distance = line[0], line[1]
    if len(line) == 3:
        # The line corresponds to a "child" distance update information.
        path, neighbours = line[2], 0
    if len(line) == 4:
        # Else, it's a complete node.
        path = line[3]
        if line[2] != "0":
            neighbours = line[2]
        else :
            neighbours = 0


    try:
        distance = int(distance)
    except Exception as e:
        continue

    # For each node, collect all distance updates. If a new distance is smaller
    # than the current one, update the node distance and the path

    if current_node == node:
        # If one of the parents of the node provides a quicker path, choose it
        if distance < current_dist:
            current_dist, current_path = distance, path
        # Don't assume that the full node line will come first : update neigh-
        # bour info as soon as it is available
        if neighbours != 0:
            current_neighbours = neighbours
    else:
        # We change nodes, so we output the result of the reduce process for the
        # last one
        if current_node:
            print '%s\t%s\t%s\t%s' % (current_node, current_dist, current_neighbours, current_path)
        current_node, current_dist, current_path, current_neighbours = node, distance, path, neighbours

if current_node == node:
    print '%s\t%s\t%s\t%s' % (current_node, current_dist, current_neighbours, current_path)
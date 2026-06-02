def print_list(start):
    curr = start
    visited = []   # list of (id, node) to preserve insertion order
    visited_ids = set()
    prev = None

    while curr:
        if id(curr) in visited_ids:
            # Print all nodes first
            print(" -> ".join(str(node.val) for _, node in visited))
            # Then print the cycle statement
            print(f"Cycle detected: Node {prev.val} -> Node {curr.val} (links back)")
            return
        visited_ids.add(id(curr))
        visited.append((id(curr), curr))
        prev = curr
        curr = curr.next

    # No cycle — normal list
    print(" -> ".join(str(node.val) for _, node in visited) + " -> None")



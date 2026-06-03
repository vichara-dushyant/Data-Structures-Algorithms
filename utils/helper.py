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


def print_dll(start):
    """Print a doubly linked list with bidirectional arrows.

    Output format:  None <-> 2 <-> 3 <-> 4 <-> None

    Also detects cycles (via next pointers) and verifies that every
    node's prev pointer is consistent with the traversal order.
    """
    curr = start
    visited = []        # list of (id, node) to preserve insertion order
    visited_ids = set()
    prev = None

    while curr:
        if id(curr) in visited_ids:
            # Print the nodes collected so far, then report the cycle
            print("None <-> " + " <-> ".join(str(node.val) for _, node in visited))
            print(f"Cycle detected: Node {prev.val} -> Node {curr.val} (links back)")
            return

        # Verify the prev pointer is consistent
        if curr.prev is not prev:
            expected = prev.val if prev else None
            actual   = curr.prev.val if curr.prev else None
            print(f"Warning: Node {curr.val}.prev expected {expected}, got {actual}")

        visited_ids.add(id(curr))
        visited.append((id(curr), curr))
        prev = curr
        curr = curr.next

    # No cycle — normal doubly linked list
    print("None <-> " + " <-> ".join(str(node.val) for _, node in visited) + " <-> None")


class MinHeapWithPosition:
    """
    A min-heap data structure that maintains the positions of elements.

    Attributes:
        positions (dict): A dictionary that maps elements to their positions in the heap.
        heap (list): The underlying list representing the min-heap.

    Methods:
        __init__(self, array=None): Initializes a new instance of the MinHeapWithPosition class.
        is_empty(self): Checks if the heap is empty.
        build_heap(self, array): Builds the min-heap from the given array.
        pop(self): Removes and returns the element with the minimum priority from the heap.
        push(self, node): Inserts a new element into the heap.
        update(self, node, new_priority): Updates the priority of an existing element in the heap.
        swap(self, idx_a, idx_b, array): Swaps two elements in the heap.
        sift_down(self, current_idx, end_idx, heap): Restores the heap property by sifting down an element.
        sift_up(self, current_idx, heap): Restores the heap property by sifting up an element.
    """

    def __init__(self, array=None) -> None:
        """
        Initializes a new instance of the MinHeapWithPosition class.

        Args:
            array (list, optional): The initial array to build the heap from. Defaults to None.
        """
        if array is None:
            array = []
        self.positions = {node[1]: idx for idx, node in enumerate(array)}
        self.heap = self.build_heap(array)

    def is_empty(self):
        """
        Checks if the heap is empty.

        Returns:
            bool: True if the heap is empty, False otherwise.
        """
        return len(self.heap) == 0

    def build_heap(self, array):
        """
        Builds the min-heap from the given array.

        Args:
            array (list): The array to build the heap from.

        Returns:
            list: The built min-heap.
        """
        first_parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(idx, len(array) - 1, array)
        return array

    def pop(self):
        """
        Removes and returns the element with the minimum priority from the heap.

        Returns:
            tuple: The element with the minimum priority.
        """
        if self.is_empty():
            return

        self.swap(len(self.heap) - 1, 0, self.heap)
        node = self.heap.pop()
        del self.positions[node[1]]
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return node

    def push(self, node):
        """
        Inserts a new element into the heap.

        Args:
            node (tuple): The element to insert into the heap.
        """
        self.heap.append(node)
        self.positions[node[1]] = len(self.heap) - 1
        self.sift_up(len(self.heap) - 1, self.heap)

    def update(self, node, new_priority):
        """
        Updates the priority of an existing element in the heap.

        Args:
            node (tuple): The element to update.
            new_priority: The new priority value.
        """
        node_idx = self.positions[node]
        self.heap[node_idx] = (new_priority, node)
        self.sift_up(node_idx, self.heap)
        self.sift_down(node_idx, len(self.heap) - 1, self.heap)

    def swap(self, idx_a, idx_b, array):
        """
        Swaps two elements in the heap.

        Args:
            idx_a (int): The index of the first element.
            idx_b (int): The index of the second element.
            array (list): The heap array.
        """
        _, node_a = array[idx_a]
        _, node_b = array[idx_b]
        self.positions[node_a] = idx_b
        self.positions[node_b] = idx_a
        array[idx_a], array[idx_b] = array[idx_b], array[idx_a]

    def sift_down(self, current_idx, end_idx, heap):
        """
        Restores the heap property by sifting down an element.

        Args:
            current_idx (int): The index of the element to sift down.
            end_idx (int): The index of the last element in the heap.
            heap (list): The heap array.
        """
        child_one_idx = 2 * current_idx + 1
        while child_one_idx <= end_idx:
            child_two_idx = 2 * current_idx + 2 if 2 * current_idx + 2 <= end_idx else -1

            # Determine which child has a smaller priority
            if child_two_idx != -1 and heap[child_two_idx][0] < heap[child_one_idx][0]:
                child_to_sift_idx = child_two_idx
            else:
                child_to_sift_idx = child_one_idx

            # Swap parent and smallest child if necessary
            if heap[current_idx][0] > heap[child_to_sift_idx][0]:
                self.swap(current_idx, child_to_sift_idx, heap)
            else:
                return

            current_idx = child_to_sift_idx
            child_one_idx = 2 * current_idx + 1

    def sift_up(self, current_idx, heap):
        """
        Restores the heap property by sifting up an element.

        Args:
            current_idx (int): The index of the element to sift up.
            heap (list): The heap array.
        """
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2

            # Swap if the parent has a larger priority
            if heap[current_idx][0] < heap[parent_idx][0]:
                self.swap(current_idx, parent_idx, heap)
                current_idx = parent_idx
            else:
                break


def get_neighbours(node, grid) -> list:
    """
    Returns a list of neighboring nodes for a given node in a grid.

    Args:
        node (tuple): The coordinates of the node in the grid.
        grid (list): The grid represented as a 2D list.

    Returns:
        list: A list of neighboring nodes.
    """

    neighbours = []
    x, y = node
    grid_y_max, grid_x_max = len(grid) - 1, len(grid[0]) - 1

    # down
    if y + 1 <= grid_y_max:
        neighbours.append((x, y+1))

    # up
    if y - 1 >= 0:
        neighbours.append((x, y-1))

    # left
    if x - 1 >= 0:
        neighbours.append((x-1, y))

    # right
    if x + 1 <= grid_x_max:
        neighbours.append((x+1, y))

    return neighbours


def get_node_value(node, grid) -> int:
    """Returns the value of a node in the grid."""
    return grid[node[0]][node[1]]


def aStarAlgorithm(startRow, startCol, endRow, endCol, grid):
    """
    Applies the A* algorithm to find the shortest path from the start node to the end node in a grid.
    1's are walls, 0's are empty spaces.

    Args:
        startRow (int): The row index of the start node.
        startCol (int): The column index of the start node.
        endRow (int): The row index of the end node.
        endCol (int): The column index of the end node.
        grid (list[list[int]]): The grid represented as a 2D list, where each element represents a node and its value represents its type (0 for empty, 1 for wall).

    Returns:
        list[tuple[int, int]]: The shortest path from the start node to the end node as a list of node coordinates (row, col). If no path is found, an empty list is returned.
    """

    def h(node) -> float:  # heuristic function
        # return abs(node[0]-endRow) + abs(node[1]-endCol)
        return abs(node[0] - endRow) + abs(node[1] - endCol)

    # node: tuple(row, col)
    start = (startRow, startCol)
    goal = (endRow, endCol)

    # queue: min heap (f[n], n(x,y))
    queue = [(h(start), start)]
    queue = MinHeapWithPosition(queue)

    # open: dict[node]: (f, g, h, node, path)
    open = {
        start: (h(start), 0, h(start), start, [start])
    }

    visited = set()

    while not queue.is_empty():

        _, node = queue.pop()
        cur_path = open[node][-1]
        cur_g = open[node][1]

        del open[node]

        if node == goal:
            return cur_path

        if node in visited:
            continue

        if get_node_value(node, grid) == 1:
            visited.add(node)
            continue

        visited.add(node)

        neighbours = get_neighbours(node, grid)

        for neighbour in neighbours:

            if neighbour in visited:
                continue

            if get_node_value(neighbour, grid) == 1:  # walls
                visited.add(neighbour)
                continue

            te_g = cur_g + 1
            te_h = h(neighbour)
            te_f = te_g + te_h
            te_path = cur_path + [neighbour]

            if neighbour in open:
                ex_f, _, _, _, _ = open[neighbour]

                if te_f < ex_f:  # found a better pathway, update frontiers
                    open[neighbour] = (te_f, te_g, te_h, neighbour, te_path)
                    queue.update(neighbour, te_f)

            else:  # add to frontiers
                open[neighbour] = (te_f, te_g, te_h, neighbour, te_path)
                queue.push((te_f, neighbour))

    return []

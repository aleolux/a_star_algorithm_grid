import unittest
from main import MinHeapWithPosition
from main import aStarAlgorithm

class MinHeapWithPositionTests(unittest.TestCase):
    def test_empty_heap(self):
        heap = MinHeapWithPosition()
        self.assertTrue(heap.is_empty())

    def test_build_heap(self):
        array = [(3, 'A'), (2, 'B'), (1, 'C')]
        heap = MinHeapWithPosition(array)
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.pop(), (1, 'C'))
        self.assertEqual(heap.pop(), (2, 'B'))
        self.assertEqual(heap.pop(), (3, 'A'))
        self.assertTrue(heap.is_empty())

    def test_push(self):
        heap = MinHeapWithPosition()
        heap.push((3, 'A'))
        heap.push((2, 'B'))
        heap.push((1, 'C'))
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.pop(), (1, 'C'))
        self.assertEqual(heap.pop(), (2, 'B'))
        self.assertEqual(heap.pop(), (3, 'A'))
        self.assertTrue(heap.is_empty())

    def test_update(self):
        heap = MinHeapWithPosition([(3, 'A'), (2, 'B'), (1, 'C')])
        heap.update('B', 0)
        self.assertEqual(heap.pop(), (0, 'B'))
        self.assertEqual(heap.pop(), (1, 'C'))
        self.assertEqual(heap.pop(), (3, 'A'))
        self.assertTrue(heap.is_empty())

class AStarAlgorithmTests(unittest.TestCase):
    def test_shortest_path_found(self):
        startRow = 1
        startCol = 8
        endRow = 1
        endCol = 1
        grid = [
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        expected_path = [
            (1, 8),
            (2, 8),
            (3, 8),
            (4, 8),
            (5, 8),
            (6, 8),
            (7, 8),
            (8, 8),
            (9, 8),
            (9, 7),
            (9, 6),
            (9, 5),
            (9, 4),
            (9, 3),
            (9, 2),
            (9, 1),
            (8, 1),
            (7, 1),
            (6, 1),
            (5, 1),
            (4, 1),
            (3, 1),
            (2, 1),
            (1, 1)
        ]
        path = aStarAlgorithm(startRow, startCol, endRow, endCol, grid)
        self.assertEqual(path, expected_path)

    def test_no_path_found(self):
        startRow = 1
        startCol = 8
        endRow = 0
        endCol = 0
        grid = [
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        ]
        expected_path = []
        path = aStarAlgorithm(startRow, startCol, endRow, endCol, grid)
        self.assertEqual(path, expected_path)

if __name__ == '__main__':
    unittest.main()
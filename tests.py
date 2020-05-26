from sort import heapsort, quicksort, insertion_sort, reverse, add_integers, counting_sort, radix_sort
import unittest

class TestSort(unittest.TestCase):
    def test_heap_sort(self):
        x = [4, 8, 2, 1, 0]
        self.assertEqual(heapsort(x)[::-1], [0, 1, 2, 4, 8])

    def test_quicksort(self):
        x = [4, 8, 2, 1, 0]
        self.assertEqual(quicksort(x), [0, 1, 2, 4, 8])

    def test_counting_sort(self):
        x = [4, 8, 2, 1, 0]
        self.assertEqual(counting_sort(x, 0, 8), [0, 1, 2, 4, 8])

    def test_radix_sort(self):
        a = [1,9,5,3]
        b = [0, 5]
        with self.assertRaises(ValueError):
            radix_sort([a,b])
        
        a = [1,9,5,3]
        b = [1,9,7,2]
        c = [2,0,0,2]
        d = [2,1,2,2]
        e = [0,1,2,2]
        f = [0,0,3,9]
        out = radix_sort([f, b, c, a, d, e])
        self.assertEqual(out, [(0, 0, 0, 2), (0, 0, 2, 2), (1, 1, 2, 2), (1, 1, 3, 2), (2, 9, 5, 3), (2, 9, 7, 9)])

    def test_insertion_sort(self):
        x = [4, 8, 2, 1, 0]
        self.assertEqual(insertion_sort(x), [0, 1, 2, 4, 8])

    def test_merge_sort(self):
        x = [4, 8, 2, 1, 0]
        self.assertEqual(insertion_sort(x), [0, 1, 2, 4, 8])

    def test_reverse(self):
        x = [4, 8, 2, 1, 0]
        self.assertEqual(reverse(x), [0, 1, 2, 8, 4])

    def test_add_integers(self):
        a = [7, 4, 5, 3]
        b = [6, 4, 3, 2]
        self.assertEqual(add_integers(a, b), [1, 3, 8, 8, 5])

if __name__ == '__main__':
    unittest.main()
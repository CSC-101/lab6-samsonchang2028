import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort1(self):
        books = [data.Book(['Terry Pratchett'],'Good Omens'),data.Book(['Homer'],'Iliad'),data.Book(['Homer'],'Odyssey')]
        results = lab6.selection_sort_books(books)
        expected = [data.Book(['Terry Pratchett'],'Good Omens'),data.Book(['Homer'],'Iliad'),data.Book(['Homer'],'Odyssey')]
        self.assertEqual(expected,results)
    def test_selection_sort2(self):
        books = [data.Book(['JK Rowling'],'Harry Potter'),data.Book(['Homer'],'Iliad'),data.Book(['James Stewart'],'Calculus')]
        results = lab6.selection_sort_books(books)
        expected = [data.Book(['James Stewart'],'Calculus'),data.Book(['JK Rowling'],'Harry Potter'),data.Book(['Homer'],'Iliad')]
        self.assertEqual(expected,results)
    # Part 2
    def test_swap_case(self):
        words ='California'
        results = lab6.swap_case(words)
        expected = 'cALIFORNIA'
        self.assertEqual(expected,results)
    def test_swap_case2(self):
        words ='Cal Poly San Luis Obispo'
        results = lab6.swap_case(words)
        expected = 'cAL pOLY sAN lUIS oBISPO'
        self.assertEqual(expected,results)
    # Part 3
    def test_str_translate_1(self):
        phrase = 'california'
        old = 'i'
        new = 'a'
        results = lab6.str_translate(phrase,old,new)
        expected = 'calafornaa'
        self.assertEqual(expected,results)
    def test_str_translate_2(self):
        phrase = 'seventeen'
        old = 'e'
        new = 'a'
        results = lab6.str_translate(phrase,old,new)
        expected = 'savantaan'
        self.assertEqual(expected,results)
    # Part 4
    def test_histogram_letters(self):
        para = 'Lorem ipsum odor amet, consectetuer adipiscing elit. Cubilia laoreet senectus lorem iaculis placerat hac tristique quis?'
        results = lab6.histogram_letters(para)
        expected = {'L': 1, 'o': 6, 'r': 7, 'e': 13, 'm': 4, ' ': 15, 'i': 12, 'p': 3, 's': 8, 'u': 7, 'd': 2, 'a': 8, 't': 9, ',': 1, 'c': 7, 'n': 3, 'g': 1, 'l': 6, '.': 1, 'C': 1, 'b': 1, 'h': 1, 'q': 2, '?': 1}
        self.assertEqual(results, expected)
    def test_histogram_letters(self):
        para = 'The quick brown fox jumps over the lazy dog'
        results = lab6.histogram_letters(para)
        expected = {'T': 1, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 't': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()

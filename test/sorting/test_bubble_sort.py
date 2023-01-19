
import random
import unittest
from parameterized import parameterized

from src.sorting.bubble_sort import bubble_sort
from test.helpers import is_sorted_asc

class BubbleSortTest(unittest.TestCase):

  def test_bubble_sort_should_do_nothing_when_array_is_empty(self):
    # arrange
    vec = []

    # act
    result = bubble_sort(vec)

    # assert
    self.assertEqual(0, len(result))

  @parameterized.expand([
    (1, ), (2, ), (4, ), (8, ), (16, ), (32, ), (64, ), (128, ), (256, ), (512, ), (1024, ), (2048, ), (4096, )
  ])
  def test_bubble_sort_should_sort_when_array_has_one_element(self, vec_count):
    # arrange    
    vec = list(range(vec_count))
    random.shuffle(vec)

    # act
    result = bubble_sort(vec)

    # assert
    self.assertEqual(vec_count, len(result))
    self.assertTrue(is_sorted_asc(result))



import random
import unittest
from parameterized import parameterized
from src.enums.sorting_order import SortingOrder

from src.sorting.bubble_sort import bubble_sort
from test.helpers.PersonTest import PersonTest
from test.helpers.sorting import is_person_test_sorted_asc, is_person_test_sorted_desc, is_sorted_asc, is_sorted_desc

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
  def test_bubble_sort_should_sort_asc_when_array_is_not_empty_and_sorting_is_default(self, vec_count):
    # arrange    
    vec = list(range(vec_count))
    random.shuffle(vec)

    # act
    result = bubble_sort(vec)

    # assert
    self.assertEqual(vec_count, len(result))
    self.assertTrue(is_sorted_asc(result))

  @parameterized.expand([
    (1, ), (2, ), (4, ), (8, ), (16, ), (32, ), (64, ), (128, ), (256, ), (512, ), (1024, ), (2048, ), (4096, )
  ])
  def test_bubble_sort_should_sort_asc_when_array_is_not_empty_and_sorting_is_ascending(self, vec_count):
    # arrange    
    vec = list(range(vec_count))
    random.shuffle(vec)

    # act
    result = bubble_sort(vec, SortingOrder.Ascending)

    # assert
    self.assertEqual(vec_count, len(result))
    self.assertTrue(is_sorted_asc(result))

  @parameterized.expand([
    (1, ), (2, ), (4, ), (8, ), (16, ), (32, ), (64, ), (128, ), (256, ), (512, ), (1024, ), (2048, ), (4096, )
  ])
  def test_bubble_sort_should_sort_desc_when_array_is_not_empty_and_sorting_is_descending(self, vec_count):
    # arrange    
    vec = list(range(vec_count))
    random.shuffle(vec)

    # act
    result = bubble_sort(vec, SortingOrder.Descending)

    # assert
    self.assertEqual(vec_count, len(result))
    self.assertTrue(is_sorted_desc(result))

@parameterized.expand([
    (1, ), (2, ), (4, ), (8, ), (16, ), (32, ), (64, ), (128, ), (256, ), (512, ), (1024, ), (2048, ), (4096, )
  ])
def test_bubble_sort_should_sort_complex_object_asc_when_array_is_not_empty_and_sorting_is_ascending(self, vec_count):
    # arrange    
    vec = []
    for i in range(vec_count):
      vec.append(PersonTest(i))
    random.shuffle(vec)

    # act
    result = bubble_sort(vec, SortingOrder.Ascending, lambda a, b : a.age - b.age)

    # assert
    self.assertEqual(vec_count, len(result))
    self.assertTrue(is_person_test_sorted_asc(result))

@parameterized.expand([
    (1, ), (2, ), (4, ), (8, ), (16, ), (32, ), (64, ), (128, ), (256, ), (512, ), (1024, ), (2048, ), (4096, )
  ])
def test_bubble_sort_should_sort_complex_object_desc_when_array_is_not_empty_and_sorting_is_descending(self, vec_count):
    # arrange    
    vec = []
    for i in range(vec_count):
      vec.append(PersonTest(i))
    random.shuffle(vec)

    # act
    result = bubble_sort(vec, SortingOrder.Descending, lambda a, b : a.age - b.age)

    # assert
    self.assertEqual(vec_count, len(result))
    self.assertTrue(is_person_test_sorted_desc(result))


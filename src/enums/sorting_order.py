
from enum import Enum

SortingOrder = Enum('SortingOrder', ['Ascending', 'Descending'])

def is_ordered(sorting_order):
  if sorting_order == SortingOrder.Ascending:
    return lambda x : x < 0
  elif sorting_order == SortingOrder.Descending:
    return lambda x : x > 0
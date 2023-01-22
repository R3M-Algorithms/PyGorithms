
from src.enums.sorting_order import SortingOrder, is_ordered

def bubble_sort(elems : list[any], sorting_order = SortingOrder.Ascending, comparison = lambda a, b : a - b) -> list[any]:
  result = elems.copy()
  ordered = is_ordered(sorting_order)
  
  swapped = True
  while swapped:
    swapped = False
    for i in range(1, len(result)):    
      comp_result = comparison(result[i - 1], result[i])
      if not ordered(comp_result):
        result[i], result[i - 1] = result[i - 1], result[i]
        swapped = True

  return result


from src.enums.sorting_order import SortingOrder, is_ordered

def bubble_sort(elems : list[any], sorting_order = SortingOrder.Ascending, comparison = lambda a, b : a - b) -> list[any]:
  result = elems.copy()
  ordered = is_ordered(sorting_order)  
  for i in range(len(result)):
    for j in range(i, len(result)):
      comp_result = comparison(result[i], result[j])
      if not ordered(comp_result):
        result[i], result[j] = result[j], result[i]

  return result


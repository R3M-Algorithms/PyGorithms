
def bubble_sort(elems : list[any]):
  result = elems.copy()
  should_continue = True
  while should_continue:
    should_continue = False
    for i in range(1, len(result)):
      if result[i] < result[i - 1]:
        result[i], result[i - 1] = result[i - 1], result[i]
        should_continue = True
  return result

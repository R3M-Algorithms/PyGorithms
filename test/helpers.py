
def is_sorted_asc(x):
  return [(x[k+1]-x[k])>0 for k in range(len(x)-1)].count(True) == len(x)-1

def is_sorted_desc(x):
  return [(x[k+1]-x[k])<0 for k in range(len(x)-1)].count(True) == len(x)-1
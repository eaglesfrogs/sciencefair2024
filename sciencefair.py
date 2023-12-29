import random
from copy import copy

list_1000_random=list(range(1000))
random.shuffle(list_1000_random)
list_1000_sorted=list(range(1000))
list_1000_backwards=list(reversed(list(range(1000))))
list_1m_random=list(range(1000000))
random.shuffle(list_1m_random)

def selection_sort(list_2_sort):
  # loops through every element in the list
  for i in range(len(list_2_sort)):

    # minvalue is the current lowest value's index
    minvalue = i

    # detects if i (the current starting index) is higher than j (the index that is being checked)
    for j in range(i+1,len(list_2_sort)):
      if list_2_sort[minvalue] > list_2_sort[j]:
        minvalue = j

    # swaps the two variables
    list_2_sort[i], list_2_sort[minvalue] = list_2_sort[minvalue], list_2_sort[i]

  return list_2_sort


def insertion_sort (list_2_sort):
  print(list_2_sort)

def merge_sort (list_2_sort):
  pass

selection_sort(copy(list_1000_random))
insertion_sort(copy(list_1000_random))
merge_sort(copy(list_1000_random))

import random
from copy import copy
from time import time_ns

list_1000_random=list(range(1000))
random.shuffle(list_1000_random)
list_1000_sorted=list(range(1000))
list_1000_backwards=list(reversed(list(range(1000))))
list_10000_random=list(range(10000))
random.shuffle(list_10000_random)
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
  # loops through every element in the list starting at the second element
  for i in range(1,len(list_2_sort)):
    key = list_2_sort[i]  # saves the value that we want to compare
    j = i - 1  # gets the index of the prior element

    # works backwards through the list comparing key to each element and swapping if the new element is greater
    while j >= 0 and key < list_2_sort[j]:
      list_2_sort[j + 1] = list_2_sort[j]
      j = j - 1

    #sets key to the right position
    list_2_sort[j + 1]=key

  return list_2_sort


def merge_sort (list_2_sort):
  if len(list_2_sort) > 1:
    mid = len(list_2_sort) // 2
    arrayL = list_2_sort[:mid]
    arrayR = list_2_sort[mid:]

    merge_sort(arrayL)
    merge_sort(arrayR)

    l=r=i=0
    while l < len(arrayL) and r < len(arrayR):
      if arrayL[l] <= arrayR[r]:
        list_2_sort[i] = arrayL[l]
        l += 1
      else:
        list_2_sort[i] = arrayR[r]
        r += 1
      i += 1

    while l < len(arrayL):
      list_2_sort[i] = arrayL[l]
      l += 1
      i += 1

    while r < len(arrayR):
      list_2_sort[i] = arrayR[r]
      r += 1
      i += 1


def timer(algorithm, list_2_sort):
  start_time = time_ns()
  algorithm(list_2_sort)
  end_time = time_ns()

  return (end_time - start_time) / 1000000

print(f"selection_sort for 1000_random took {timer(selection_sort, copy(list_1000_random))} ms")
print(f"selection_sort for 1000_sorted took {timer(selection_sort, copy(list_1000_sorted))} ms")
print(f"selection_sort for 1000_backwards took {timer(selection_sort, copy(list_1000_backwards))} ms")
print(f"selection_sort for 10000_random took {timer(selection_sort, copy(list_10000_random))} ms")

print(f"insertion_sort for 1000_random took {timer(insertion_sort, copy(list_1000_random))} ms")
print(f"insertion_sort for 1000_sorted took {timer(insertion_sort, copy(list_1000_sorted))} ms")
print(f"insertion_sort for 1000_backwards took {timer(insertion_sort, copy(list_1000_backwards))} ms")
print(f"insertion_sort for 10000_random took {timer(insertion_sort, copy(list_10000_random))} ms")

print(f"merge_sort for 1000_random took {timer(merge_sort, copy(list_1000_random))} ms")
print(f"merge_sort for 1000_sorted took {timer(merge_sort, copy(list_1000_sorted))} ms")
print(f"merge_sort for 1000_backwards took {timer(merge_sort, copy(list_1000_backwards))} ms")
print(f"merge_sort for 10000_random took {timer(merge_sort, copy(list_10000_random))} ms")
print(f"merge_sort for 1m_random took {timer(merge_sort, copy(list_1m_random))} ms")

# selection_sort for 1000_random took 89.509 ms
# selection_sort for 1000_sorted took 90.5586 ms
# selection_sort for 1000_backwards took 119.5152 ms
# selection_sort for 10000_random took 9095.6953 ms
# insertion_sort for 1000_random took 114.6127 ms
# insertion_sort for 1000_sorted took 0.0 ms
# insertion_sort for 1000_backwards took 202.5795 ms
# insertion_sort for 10000_random took 10536.9768 ms
# merge_sort for 1000_random took 9.0006 ms
# merge_sort for 1000_sorted took 7.9985 ms
# merge_sort for 1000_backwards took 7.9987 ms
# merge_sort for 10000_random took 108.1764 ms
# merge_sort for 1m_random took 16190.6376 ms

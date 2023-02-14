cisla = [3, 5, 8, 0, 4, 2, 0, 7, 6, 2, 0, 5]

# uloha 15 -> k-te maximum 
import sys

n_max = int(sys.argv[1])
unsorted_list = [int(x) for x in sys.argv[2:]]
sorted_list = []

while unsorted_list: # nebo len(unsorted_list) > 0
  maximum = unsorted_list[0]
  for item in unsorted_list:
    if item > maximum:
      maximum = item
  sorted_list.append(maximum)
  unsorted_list.remove(maximum)

print(sorted_list[n_max-1])

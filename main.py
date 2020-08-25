def find_pivot_index(input_list):
  # List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index
  start = 0
  end = len(input_list)
  minimum_index = 0
  while start < end-1:
    if end - start % 2 == 0:
      pivot = int((end - start) / 2) + start
    else:
      pivot = int((end - start + 1) / 2) + start
    if input_list[pivot] < input_list[minimum_index]:
      end = pivot
      minimum_index = pivot
    else:
      start = pivot
  return minimum_index
  pass

print(find_pivot_index([7,8,9,0,1,2,3,4,5,6]))
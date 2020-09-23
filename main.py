numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selection_sort(arr):
  for x in range(len(arr)):
    for y in range(len(arr)):
      if arr[x] < arr[y]:
        arr[x], arr[y] = arr[y], arr[x]

selection_sort(numbers)

print(numbers)
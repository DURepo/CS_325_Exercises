def foo(arr, start, end):
  if(start < end):
    middle = (start+end)//2
    foo(arr, start, middle)
    foo(arr, middle+1, end)
  else:
    arr[start] = 2 * arr[start]

if __name__ == '__main__':
  arr = [1,2,3,4,5,6,7]
  foo(arr, 0, 6)

  for i in range(0, 7):
    print(arr[i])

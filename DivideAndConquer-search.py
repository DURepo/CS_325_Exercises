
def _binary_search(numList, start, end, x):
    if (start <= end):
        middle = (start + end) // 2
        if (a[middle] == x):
            return middle

        if (a[middle] > x):
            return _binary_search(a, start, middle - 1, x)

        if (a[middle] < x):
            return _binary_search(a, middle + 1, end, x)

    return -1  # not found


def search(numList, key):
    return _binary_search(numList, 0, len(numList)-1, key)


if __name__ == '__main__':
  a = [1,3,4,5,6,7,8,9]
  result = search(a, 9)
  print(result)

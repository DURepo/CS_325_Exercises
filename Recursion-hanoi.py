def hanoi(n, source, temp, target):
    if n > 0:
        # move n-1 disks from source to temp:
        hanoi(n - 1, source, target, temp)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move n-1 disks from temp to target
        hanoi(n - 1, temp, source, target)


source = [5, 4, 3, 2, 1]
target = []
temp = []
hanoi(len(source), source, temp, target)

print( source, temp, target)

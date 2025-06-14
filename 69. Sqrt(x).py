'''Calculate the round square root.
   Binary search o(log n)'''

def mysqrt(x):

    # Handle edge cases
    if x == 0 or x == 1:
        return x

    left, right = 1, x

    while left <= right:
        mid = (left+right)//2
        sqrt = mid*mid

        if sqrt == x:
            return x
        elif sqrt > x:
            right = mid -1  #
        else:
            left = mid + 1  #

    return right

x = int(input())
result = mysqrt(x)
print(result)

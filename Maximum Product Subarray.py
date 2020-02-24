def maxProduct(nums):
    imax = nums[0]
    imin = nums[0]
    tru_max = nums[0]
    for x in nums[1:]:
        if x < 0:
            temp = imax
            imax = imin
            imin = temp
        imax = max(x, x * imax)
        imin = min(x, x * imin)
        tru_max = max(imax, tru_max)
    return tru_max


if __name__ == '__main__':
    print(maxProduct([2, 3, -2, 4]))

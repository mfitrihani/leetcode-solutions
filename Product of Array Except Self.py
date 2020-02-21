def productExceptSelf(nums):
    left_product = [1]
    right_product = [1]*len(nums)
    index = 0
    while index < len(nums) - 1:
        left_product.append(left_product[index]*nums[index])
        index += 1
    index = len(nums) - 2
    while index >= 0:
        right_product[index] = right_product[index + 1] * nums[index + 1]
        index -= 1
    index = 0
    product = []
    while index < len(nums):
        product.append(left_product[index]*right_product[index])
        index += 1
    return product


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))

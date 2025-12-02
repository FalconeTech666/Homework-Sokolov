'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным 
    - элементы значения которого является 
            четными - умножить на 2 
            нечетным - умножить на 3

Использовать map и lambda.
'''

nums = [1,2,3,4,5,6,7,8,9]

nums1 = nums.copy()
nums2 = nums.copy()
nums3 = nums.copy()

nums1 = list(map(lambda x: x**2, nums1))
print(nums1)

nums2 = list(map(lambda x: x+3 if x%2==0 else x, nums2))
print(nums2)

nums3 = list(map(lambda x: x*2 if x%2==0 else x*3, nums3))
print(nums3)

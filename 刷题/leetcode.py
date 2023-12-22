'''力扣--1
    给定一个整数数组 nums 和一个整数目标值 target,
    请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
'''

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]
#             return None
        
        

'''
    力扣--3--滑动窗口--双指针
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
'''

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:           #s是str类型
#        # 检查输入的条件
#         if len(s) == 0:
#             return 0


#         # 定义窗口边界   可变长度的窗口,定义两个边界
#         winStart = 0  # 窗口左边
#         winEnd = 0  #  窗口右边

#         # 定义窗口的状态
#         # 小技巧: 如果是最长就把初始状态定为0,  如果是最短就把初始状态定为比较大的数
#         maxLen = 0

#         # 开始搜寻(迭代)
#         for winEnd in range(len(s)):    #从右边的窗口开始迭代
#             # 进窗口
#             if s[winEnd] not in s[winStart:winEnd]:  # 判断字符是否在窗口里面  (不在里面)
#                 maxLen = max(maxLen,winEnd - winStart + 1)
#                 continue  # 跳入下一个循环
            
#             # 缩减窗口   把左边界推进,确保窗口内字符不包括s[winEnd]
#             winStart = winStart + s[winStart:winEnd].index(s[winEnd]) + 1
#         return maxLen



'''
    力扣--4
    给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
    请你找出并返回这两个正序数组的 中位数 。
'''

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums1.extend(nums2)
#         numa = sorted(nums1)

#         x = len(numa)//2
#         if len(numa)%2 == 0:
#             return (float(numa[x]) + float(numa[x-1]))/2
#         else:
#             return numa[x]



'''
    力扣--6--二维矩阵--困难
    将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x = 0
        f = -1
        if numRows == 1 or numRows >= len(s):
            return s
        else:
            # 打印行数  这三个字符串代表每一行
            li = [''for x in range(numRows)]        # 等价于 li = list(''for x in range(3))
            for i in s:
                li[x] += i       #先分配第一列
                if x == 0 or x == numRows - 1 :         # 实现Z字循环
                    f = -f                             
                x += f                                       
            return ''.join(li)  
                                                 
                                                         
                                                       
        
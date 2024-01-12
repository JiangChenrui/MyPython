# 
# 最长公共子序列
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

def max_com_str(text1, text2):
    if not text1 or not text2:
        return 0
    dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[-1][-1]

# 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


def max_length(l:list):
    start=0
    cur=0
    nex=1
    max_len=0
    length=0
    while start<len(l):
        if nex<len(l):
            if l[cur]<=l[nex]:
                length+=1
                cur=nex
                nex+=1
            else:
                cur=cur+1
                nex=cur+1
        else:
            start=start+1
            cur=start
            nex=cur+1
        if length>max_len:
            max_len=length
    return max_len

print(lengthOfLIS([5, 2, 6, 9, 4, 1]))
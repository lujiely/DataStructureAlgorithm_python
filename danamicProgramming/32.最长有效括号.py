#coding:utf-8
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

[32] 最长有效括号
'''

class Solution():
    def longestValidParenthese(self, s):
        stack, res = [-1], 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                res = max(res, i - stack[-1])
        return res


if __name__ == '__main__':
    solu = Solution()
    s = "(()"
    s = ")()())("
    s = ")()())"
    res = solu.longestValidParenthese(s)
    print(res)

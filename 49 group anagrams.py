"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]



"""
import collections


def groupAnagrams(strs):
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        ans[tuple(count)].append(s)   # python , list cannot be the key, use tuple to group the list

    return ans.values()
"""

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # maximum possible idle time: ()frequence_max - 1) * cooling period <in example 1 , thats 2>
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        f_max = frequencies.pop()
        idle_time = (f_max-1)*n

        while frequencies and idle_time > 0:

            idle_time -= min(f_max-1, frequencies.pop())

        idle_time = max(0, idle_time)
        return idle_time+len(tasks)

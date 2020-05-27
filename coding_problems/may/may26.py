from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Min heap
        '''
        c = Counter(tasks)
        heap = [-v for v in c.values()]
        heapq.heapify(heap)
        queue = deque()
        currTime = 0

        while heap or queue:
            if heap:
                coolDownTask = heapq.heappop(heap) + 1
                if coolDownTask:
                    queue.append((coolDownTask, currTime + n))

            if queue and queue[0][1] == currTime:
                heapq.heappush(heap, queue.popleft()[0])

            currTime += 1

        return currTime

    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Calculating Idle slots
        '''
        c = Counter(tasks)
        maxCount = noMax = 0
        for v in c.values():
            if v > maxCount:
                maxCount = v
                noMax = 1
            elif v == maxCount:
                noMax += 1

        return max(len(tasks), (maxCount - 1) * (n + 1) + noMax)


def main():
    s = Solution()
    print(s.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2))
    print(s.leastInterval(['A', 'A', 'B', 'A'], 2))

if __name__ == '__main__':
    main()

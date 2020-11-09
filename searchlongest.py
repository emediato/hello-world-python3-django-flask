"""Given an arbitrary unweighted rooted tree which consists of N nodes.

The goal of the problem is to find largest distance between two nodes in a tree.

Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree).

The nodes will be numbered 0 through N - 1.

The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be root node.



Problem Constraints

1 <= N <= 40000


Input Format

First and only argument is an integer array A of size N.


Output Format

Return a single integer denoting the largest distance between two nodes in a tree.


Example Input

Input 1:

 A = [-1, 0, 0, 0, 3]



Example Output

Output 1:

 3



Example Explanation

Explanation 1:

 node 0 is the root and the whole tree looks like this:
          0
       /  |  \
      1   2   3
               \
                4

 One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3.
"""
class SolutionFASTEST:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        c=0
        m=0

        x=[0]*len(A)

        for i in range(len(A)-1,0,-1):
            c=max(c,x[A[i]]+x[i]+1)
            x[A[i]]=max(x[A[i]],x[i]+1)

        return c
import heapq
import resource
import sys

# Will segfault without this line.
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        children = {}
        root = None
        for i, x in enumerate(A):
            if x == -1:
                root = i
            else:
                if x in children:
                    children[x] += [i]
                else:
                    children[x] = [i]

        largest_dist = 0

        for k,v in self.dfs(root, children, 0, {}).items():
            largest_dist = max(self.largest_dist_from_paths(v), largest_dist)

        return largest_dist

    def largest_dist_from_paths(self, paths):
        paths += [0, 0]
        a, b = heapq.heappop(paths), heapq.heappop(paths)
        return -1 * (a + b)

    def dfs(self, root, children, path_len, paths):
        paths[root] = [0]

        if root not in children: return paths

        for child in children[root]:
            paths = self.dfs(child, children, path_len + 1, paths)
            heapq.heappush(paths[root], min(paths[child]) - 1)

        return paths



class SolutionLightweight:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        dist = [-1] * n

        # find the farthest node from 0 (an arbitrary) node
        dist[0] = 0
        done = False
        while not done:
            done = True
            for i in range(n):

                if dist[i] == -1: # update child
                    done = False
                    if A[i] != -1 and dist[A[i]] != -1:
                            dist[i] = dist[A[i]] + 1
                else: # update parent
                    if A[i] != -1 and dist[A[i]] == -1:
                        done = False
                        dist[A[i]] = dist[i] + 1

        index, max_dist = 0, dist[0]
        for i in range(n):
            if dist[i] > max_dist:
                index = i
                max_dist = dist[i]

        # find maximum distance from max dist, an end point
        dist = [-1] * n
        dist[index] = 0
        while A[index] != -1: # non root, go to parents
            dist[A[index]] = dist[index] + 1
            index = A[index]

        # update the rest
        done = False
        while not done:
            done = True
            for i in range(n):
                if dist[i] == -1: # update child
                    done = False
                    if A[i] != -1 and dist[A[i]] != -1:
                            dist[i] = dist[A[i]] + 1
                else: # update parent
                    if A[i] != -1 and dist[A[i]] == -1:
                        done = False
                        dist[A[i]] = dist[i] + 1

        return max(dist)

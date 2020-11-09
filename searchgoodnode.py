"""
Problem Description

Given a tree with N nodes labelled from 1 to N.

Each node is either good or bad denoted by binary array A of size N where if A[i] is 1 then ithnode is good else if A[i] is 0 then ith node is bad.

Also the given tree is rooted at node 1 and you need to tell the number of root to leaf paths in the tree that contain not more than C good nodes.

NOTE:

    Each edge in the tree is bi-directional.



Problem Constraints

2 <= N <= 105

A[i] = 0 or A[i] = 1

0 <= C <= N



Input Format

First argument is an binary integer array A of size N.

Second argument is a 2-D array B of size (N-1) x 2 denoting the edge of the tree.

Third argument is an integer C.



Output Format

Return an integer denoting the number of root to leaf paths in the tree that contain not more than C good nodes.
"""
from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        tree = self.build_tree(B)
        return self.count_good_paths(A, tree, 1, 0, C)

    def build_tree(self, B):
        tree = defaultdict(set)
        for edge in B:
            tree[min(edge)].add(max(edge))
        return tree

    def count_good_paths(self, A, tree, node, cur_count, C):
        if A[node-1]:
            cur_count += 1
        if cur_count > C:
            return 0
        if node not in tree:
            return 1
        good_paths = 0
        for child in tree[node]:
            good_paths+=self.count_good_paths(A, tree, child, cur_count, C)
        return good_paths


class SolutionLight:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n=len(A)
        g=[[] for i in range(n+1)]

        for item in B:
            u,v=item[0],item[1]
            g[u].append(v)
            g[v].append(u)


        s=[(1,A[0])]
        vis=[0]*(n+1)
        vis[1]=1
        count=0
        while s:
            item=s.pop()
            x=item[0]
            val=item[1]
            flag=1
            for node in g[x]:
                if  vis[node]==0:
                    flag=0
                    if val+A[node-1]<=C:
                        vis[node]=1
                        s.append((node,val+A[node-1]))

            if flag and val<=C:
                count+=1

        return count

#SolutionEDITORIAL



maxn=100009
cnt=0
ans=0
adj=[]
def ini():
    global maxn,adj,cnt,ans
    ans=0
    cnt=0
    adj=[[] for i in range(maxn)]
def dfs(u,p,A,C):
    global adj,cnt,ans
    if(A[u-1]):
        cnt+=1
    isLeaf=1
    for node in adj[u]:
        if(node==p):
            continue
        isLeaf=0
        dfs(node,u,A,C)
    if(isLeaf and cnt<=C):
        ans+=1
    if(A[u-1]):
        cnt-=1
    return
class SolutionEDITORIAL:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        global maxn,adj,cnt,ans
        ini()
        for edge in B:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        dfs(1,0,A,C)
        return ans

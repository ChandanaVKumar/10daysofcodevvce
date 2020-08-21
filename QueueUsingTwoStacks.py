n = int(input())
q = []

for i in range(n):
    query = [int(i) for i in input().split()]
    if query[0] == 1:
        q.append(query[1])
    if query[0] == 2:
        q.pop(0)
    if query[0] == 3:
        print(q[0])

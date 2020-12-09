import sys
data = [conv := (lambda ln : (int(ln))) (line) for line in open("data.txt", 'r').readlines()]

#part 1
#Probably possible to condense this into an one-liner
preambule = 25
match = lambda lst, f, s, N : 0 if lst[f] + lst[s] == lst[N] else lst[N] if f==N-2 else match(lst, f+1, f+2, N) if s == N-1 else match(lst, f, s+1, N)
res1 = sum(match(data, i-preambule, i-preambule+1, i)for i in range(preambule, len(data)))
print(res1)

#part2
#This one only works for "example.txt" - "data.txt" is quite big and the numbers are also big - I thinks it runs out of memory, because this is a recursive lambda
sys.setrecursionlimit(5000)     #yeah this is probably why it doesnt work
sublist = lambda f,c : data[f:c+1] if sum(data[f:c+1]) == res1 else sublist(f+1, f+2) if sum(data[f:c+1]) > res1 else sublist(f, c+1)
t = sublist(0, 1)
print(str(max(t) + min(t)))
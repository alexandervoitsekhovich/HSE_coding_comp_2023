n = int(input()) - 1
input()
playlist = set(input().split())
for i in range(n):
    input()
    playlist = playlist & set(input().split())


playlist = tuple(playlist)
print(len(playlist))
print(*sorted(playlist))

import collections
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
item = list(map(int, input().split()))
plug = set()
item_counter = collections.Counter(item).most_common()
item_dict = dict()
for i in range(len(item_counter)):
    item_dict[item_counter[i][0]] = item_counter[i][1]

ans = 0
for use in item:
    if len(plug) == n and use not in plug:
        # compare = 101
        to_remove = 0
        for i in plug:
            if compare > item_dict[i]:
                compare = item_dict[i]
                to_remove = i
        plug.remove(to_remove)
        ans += 1
        print(to_remove)
        plug.add(use)
        item_dict[use] -= 1
    else:
        plug.add(use)
        item_dict[use] -= 1

    print(plug)

print(ans)




# ans = 0
# for use in item:
#     if len(plug) <= n:
#         plug.add(use)

#     else:
#         to_remove = 0
#         for i in plug:


# else:
#     print(ans)    
# def miniMaxSum(arr):
#     # Write your code here
#     arr.sort()
#     print(arr)
#     min = 0
#     max = 0
#     # for i in list[:-1]:
#     #     min += i
#     # for i in list[1:]:
#     #     max += i
#     print(f"{min} {max}")
#
# arr = [1, 5, 2, 3, 4, 5]
# miniMaxSum(arr)


#
# def lonelyinteger(a):
#     # Write your code here
#     # integer = a.sort()
#     a.sort()
#     for i in range(len(a)):
#         if a[i] not in a[i+1:] and a[i] not in a[:i]:
#             lon = a[i]
#     return lon


#
# a = [34, 95, 34, 64, 45, 95, 16, 80, 80, 75, 3, 25, 75, 25, 31, 3, 64, 16, 31]
#
# print(lonelyinteger(a))



#
#
# def equalizeArray(arr):
#     # arr.sort()
#     print(arr)
#     list1 = {}
#     # list[0] = arr[0]
#     for i in arr:
#         if i in list1:
#             list1[i] += 1
#         else:
#             list1[i] = 1
#     n = list(list1.values())
#     n.sort()
#
#     print(sum(n[:-1]))
#     print(list1)
#
#
#
# a  = [3, 3, 2, 1, 3]
# print(sum(a[:-1]))
# equalizeArray(a)





a = [[2,6], [1,7]]
r_q = 4
c_q = 4
n = 8
r_q_s = r_q -1
c_q_e = c_q +1
while r_q_s >= n and c_q_e <= n:
    print("=============")
    if [r_q_s, c_q_e] not in a:
        print("not blocked")
        print([r_q_s, c_q_e])

    else:
        print("blocked")
        print([r_q_s, c_q_e])
        break
    r_q_s -= 1
    c_q_e += 1


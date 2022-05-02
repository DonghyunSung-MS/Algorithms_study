# def find_pair_and_erase(s):
#     ns = []
#     idx = 0

#     flag = False
#     while idx < len(s)-1:
#         if s[idx] == s[idx + 1]:
#             flag = True
#             idx = idx + 2
#         else:
#             ns.append(s[idx])
#             idx += 1

#     if idx == len(s)-1: # last element
#         ns.append(s[idx])

#     return ns, flag


# def solution(s):
#     s = list(s)

#     flag = True
#     while len(s) > 0 and flag:
#         s, flag = find_pair_and_erase(s)

#     return int(flag)

# 위풀이는 여러번 돌 수 있다 O(N + ....)
# 예를 들어 abcdefkkfedcba 가운데서부터 살아지기때문에
#

# 한번에 풀기위해서 즉 O(N) 으로 하기 위해 stack을 이용한다.
# stack = [abcdefkk]
# stack = [abcdeff]
# stack = [abcdee]
# ...

def solution(s):
    stack = []

    for i, ele in enumerate(s):
        if len(stack) == 0:
            stack.append(ele)
            continue

        if stack[-1] == ele:
            stack.pop()
        else:
            stack.append(ele)

    if len(stack) == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    solution("cdcd")
    solution("baabaa")
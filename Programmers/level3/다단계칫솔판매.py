from collections import defaultdict

upper_dict = {}
sell_earning = defaultdict(int)


def dfs(node, money):
    global sell_earning
    if money < 1:
        return
    if node =="-":
        return

    fee = int(money * 0.1)
    sell_earning[node] += money - fee
    dfs(upper_dict[node], fee)


def solution(enroll, referral, seller, amount):
    global upper_dict, sell_earning

    for node, parent in zip(enroll, referral):
        upper_dict[node] = parent
        

    for name, amount in zip(seller, amount):
        dfs(name, amount * 100)

    answer = [sell_earning[node] for node in enroll]
    return answer


if __name__ == "__main__":
    print(
        solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10],
        
    )
    )

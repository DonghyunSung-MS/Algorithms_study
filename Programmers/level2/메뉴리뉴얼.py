


def combinations(lst, n):
     
    if n == 0:
        return ['']
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        for p in combinations(remLst, n-1):
            l.append(m+p)
             
    return l

def count_orders(comb):
    x = dict()
    for key in comb:
        if key in x.keys():
            x[key] += 1
        else:
            x[key] = 1
    return x

def get_max_order(x):
    # can be multiple also have more than 2 people
    max_num_ords = max(x.values())
    print(max_num_ords)
    ans = []
    if max_num_ords < 2:
        return ans
    
    for key, value in x.items():
        if value == max_num_ords:
            ans.append(key)
            
    return ans
    
    
    
        
if __name__ =="__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    courses = [2,3,4]

    full_ans = []
    for num_menu in courses:
        course_candidates_per_num_menu = []
        for order in orders:
            tmp = combinations(order, num_menu)
            course_candidates_per_num_menu += tmp
        
        out_dict = count_orders(course_candidates_per_num_menu)
        print(get_max_order(out_dict))
    
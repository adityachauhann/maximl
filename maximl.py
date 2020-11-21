from collections import defaultdict   
 
def find_sub_string(str): 
    str_siz = len(str) 
    dist_count = len(set([input for input in str]))
    input = 0
    a = 0
    a_ind = -1
    b = 9999999999
    count = defaultdict(lambda: 0) 
    for i in range(str_siz): 
        count[str[i]] += 1
        if count[str[i]] == 1: 
            input += 1
        if input == dist_count: 
            while count[str[a]] > 1: 
                if count[str[a]] > 1: 
                    count[str[a]] -= 1
                a += 1
            siz = i - a + 1
            if b > siz: 
                b = siz 
                a_ind = a 
    z = str[a_ind: a_ind + b] 
    return(len(z))
str1 = input()
print(find_sub_string(str1))
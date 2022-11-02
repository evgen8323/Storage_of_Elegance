f = open('input.txt', 'r')

def make_dict(s):
    s_dict = {}
    for c in s:
        if c not in s_dict:
            s_dict[c] = 0
        s_dict[c] += 1
    return s_dict

def match_dicts(dict1, dict2):
    matches = 0
    for c in dict1:
        if c in dict2 and dict1[c] == dict2[c]:
            matches += 1
    return matches

def modify_dict(s_dict, w_dict, sym, m):
    ans = 0
    if sym not in s_dict:
        s_dict[sym] = 0
    if sym in w_dict and s_dict[sym] == w_dict[sym]:
        ans = -1
    s_dict[sym] += m
    if sym in w_dict and s_dict[sym] == w_dict[sym]:
        ans = 1
    return ans
    
    
len_w, len_s = map(int, f.readline().split())
w = f.readline().strip()
s = f.readline().strip()

w_dict = make_dict(w)
s_dict = make_dict(s[:len_w])
matching_letters = match_dicts(w_dict, s_dict)
occurrences = 0
if matching_letters == len_w:
    occurrences += 1
for i in range(len_w, len_s):
    matching_letters += modify_dict(s_dict, w_dict, s[i - len_w], -1)
    matching_letters += modify_dict(s_dict, w_dict, s[i], 1)
    if matching_letters == len(w_dict):
        occurrences += 1
        
print(occurrences)

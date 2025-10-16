def build_lps(p: str):
    lps = [0]*len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = lps[j-1]
        if p[i] == p[j]:
            j += 1
            lps[i] = j
    return lps

def kmp_search(s: str, p: str):
    if not p: return list(range(len(s)+1))  # 约定：空串匹配所有位置
    lps = build_lps(p)
    j, res = 0, []
    for i, ch in enumerate(s):
        while j > 0 and ch != p[j]:
            j = lps[j-1]
        if ch == p[j]:
            j += 1
            if j == len(p):
                res.append(i - len(p) + 1)
                j = lps[j-1]
    return res

# 示例
print(kmp_search("ababcabcacbab", "abcac"))  # -> [5]
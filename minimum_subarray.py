from collections import defaultdict

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    target_count = defaultdict(int)
    for ch in t:
        target_count[ch] += 1

    required = len(target_count) 
    formed = 0
    window_count = defaultdict(int)

    l, r = 0, 0
    ans = (float("inf"), None, None)

    while r < len(s):
        ch = s[r]
        window_count[ch] += 1

        if ch in target_count and window_count[ch] == target_count[ch]:
            formed += 1

        while l <= r and formed == required:
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

       
            left_char = s[l]
            window_count[left_char] -= 1
            if left_char in target_count and window_count[left_char] < target_count[left_char]:
                formed -= 1
            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]


print(min_window("ADOBECODEBANC", "ABC"))  

# 953. Verifying an Alien Dictionary
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
import heapq
from collections import defaultdict
def alien(words,order):
    dic = defaultdict(int)
    for wo in range(len(order)):
        dic[order[wo]] += wo
    # heap = []
    # for index,word in dic.items():
    #     heapq.heappush(heap,(index,word))
    for i in range(len(words)-1):
        for j in range(len(words[i])):
            if j >= len(words[i+1]):
                return False
            elif (words[i][j] != words[i+1][j]):
                first_l = dic[words[i][j]]
                second_l = dic[words[i+1][j]]
                if second_l < first_l:
                    return False
                else: break
    return True
    

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(alien(words,order))
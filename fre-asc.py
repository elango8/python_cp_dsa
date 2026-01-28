from collections import defaultdict
class Solution():
    def sortByFreq(self,arr):
        de = defaultdict(int)
        for i in arr:
            de[i] +=1
        sorting = sorted(de.items(),key=lambda x:(x[1],x[0]),reverse=True)
        result = []
        for woe,fre in sorting:
            result.extend([woe] * fre)
        return result

    # def fre_asc(self,list):
    #     de = defaultdict(int)
    #     for i in list:
    #         de[i] +=1
    #     sorting = sorted(de.items(),key=lambda x:(x[1],-x[0]))
    #     result = []
    #     for woe,fre in sorting:
    #         result.extend([woe] * fre)
    #     return result
        
my = Solution()
#print(my.sortByFreq(([9, 9, 9, 2, 5]))) #[9, 9, 9, 2, 5]
print(my.sortByFreq(([5, 5, 4, 6, 4]))) # [4, 4, 5, 5, 6]+
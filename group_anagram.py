class Solution:
    def groupAnagrams(self, strs):
        result = []
        for word in strs:
            found = False
            for group in result:
                if self.isAnagram(group[0], word):
                    group.append(word)
                    found = True
                    break  
            if not found:
                result.append([word])
        return result

    def isAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False
        count = [0] * 26
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True
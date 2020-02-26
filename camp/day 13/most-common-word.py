#https://leetcode.com/problems/most-common-word
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
               
        def checker(paragraph,banned):
            for i in paragraph:
                if i not in banned:
                    if i in dictionary:
                        dictionary[i] += 1
                    else:
                        dictionary[i] = 1
        for i in ("!?',;."):
            paragraph = paragraph.split(i)
            paragraph = " ".join(paragraph)

        dictionary = {}
        
        paragraph   = paragraph.split()
            

        for i in range(len(paragraph)):
            if paragraph[i].isalpha():
                paragraph[i] = paragraph[i].lower()
            else:
                paragraph[i] =  paragraph[i][:-1].lower()

        banned = set(banned)

        checker(paragraph,banned)

        freq = sorted((value, key) for (key,value) in dictionary.items())

        return freq[-1][1]

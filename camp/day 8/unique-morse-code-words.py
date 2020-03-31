#https://leetcode.com/contest/weekly-contest-77/problems/unique-morse-code-words/
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        print(len(morseCode))
        uniqueMorseRep = set()
        for word in words:
            morseRep = ""
            for letter in word:
                morseRep += morseCode[ord(letter)-97]
            uniqueMorseRep.add(morseRep)
        return len(uniqueMorseRep)

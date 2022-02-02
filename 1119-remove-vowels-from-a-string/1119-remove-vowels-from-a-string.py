class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = filter(lambda x: x not in vowels, s)
        return ''.join(ans)
        
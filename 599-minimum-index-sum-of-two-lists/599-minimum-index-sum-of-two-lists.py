from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapp = defaultdict(list)        
        i = 0
        summ = float('inf')
        answer = []
        
        while i < len(list1):
            word = list1[i]
            mapp[word].append(i)
            i += 1
        
        i = 0
        while i < len(list2):
            word = list2[i]
            mapp[word].append(i)
            i += 1
                            
        for key, value in mapp.items():
            cur_sum = sum(value)
            if len(value) == 2:
                if cur_sum < summ:
                    answer = []
                    answer.append(key)
                    summ = cur_sum
                elif cur_sum == summ:
                    answer.append(key)
        
        return answer
                                
        

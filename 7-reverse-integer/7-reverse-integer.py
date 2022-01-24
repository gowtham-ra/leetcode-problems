class Solution:
    def reverse(self, x: int) -> int:
            if not x:
                return 0

            answer = ""
            number = abs(x)

            while number > 0:
                answer += str(number % 10)
                number //= 10

            if x < 0:
                answer = -int(answer)
            else:
                answer = int(answer)
            
            if answer > (2**31 - 1) or answer < (-2**31):
                answer = 0

            return answer
class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for x in range(n):
            if (x+1)%3 == 0 and (x+1)%5 == 0:
                answer.append("FizzBuzz")  
            elif (x+1)%3 == 0:
                answer.append("Fizz")  
            elif (x+1)%5 == 0:
                answer.append("Buzz")  
            else:
                answer.append(str(x+1))   
        return answer

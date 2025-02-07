class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        result = [""] * n

        for i in range(len(result)):
            if (i + 1) % 15 == 0:
                result[i] = "FizzBuzz"
            elif (i + 1) % 3 == 0:
                result[i] = "Fizz"
            elif (i + 1) % 5 == 0:
                result[i] = "Buzz"
            else:
                result[i] = str(i + 1)

        return result

class MyMath:
    def get_king(self, num):
        kings = []
        for i in range(1, num):
            if num % i == 0:
                kings.append(i)
        return kings

    def get_queen(self, num):
        queens = sum(self.get_king(num))
        if queens == num:
            return queens


n = int(input("숫자를 입력하시오> "))
numbers = []
mymath = MyMath()
for num in range(1, n+1):
    if mymath.get_queen(num):
        numbers.append(num)

print(numbers)


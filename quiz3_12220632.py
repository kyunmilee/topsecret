
list1 = []
a = 0
cnt = 0
for a in range(7):
    list1.append(input())
    cnt += 1
    if "" in list1:
        break
i = 0
you = list1[0]
while i < cnt//2:
    if list1[1] == "+":
        you = float(you) + float(list1[2])
    elif list1[1] == "-":
        you = float(you) - float(list1[2])
    elif list1[1] == "*":
        you = float(you) * float(list1[2])
    elif list1[1] == "/":
        you = float(you) / float(list1[2])

    del list1[0:2]
    i += 1


you3="{:.2f}".format(you)
you2="{:g}".format(float(you3))
print("계산 결과는", you2, "입니다.")


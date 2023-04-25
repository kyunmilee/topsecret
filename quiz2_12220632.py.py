str1=input("계산식을 입력하시오")
if  "+" in str1:
    list1=str1.split("+")
    you=float(list1[0])+float(list1[1])
elif "-" in str1:
    list1=str1.split("-")
    you=float(list1[0])-float(list1[1])
elif "*" in str1:
    list1=str1.split("*")
    you=float(list1[0])*float(list1[1])
elif "/" in str1:
    list1=str1.split("/")
    you=float(list1[0])/float(list1[1])

you3="{:.2f}".format(you)
you2="{:g}".format(float(you3))
print("결과", you2, "입니다.")
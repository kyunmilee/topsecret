

print("간단한 데이터베이스 검색 기능 구현")
print("[데이터 검색]")

dictioary1 = {
    "name" : "철수", "age" : 21, "score" : 4.3
}
dictioary2 = {
    "name" :"영희", "age" : 16, "score" : 3.1
}
dictioary3 = {
    "name" :"민수", "age" : 24, "score" : 3.9
}
dictioary4 = {
    "name" : "길동", "age" : 29, "score" : 4.1
}

word=input("검색할 데이터의 이름을 입력하세요 >")

if dictioary1["name"] == word:
    print(dictioary1)
elif dictioary2["name"] == word:
    print(dictioary2)
elif dictioary3["name"] == word:
    print(dictioary3)
elif dictioary4["name"] == word:
    print(dictioary4)
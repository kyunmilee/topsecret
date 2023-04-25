databases = [{"name": "철수", "age": 21, "score": 4.3},
{"name": "영희", "age": 16, "score": 3.1},
{"name": "민수", "age": 24, "score": 3.9},
{"name": "길동", "age": 29, "score": 4.1}]

num = len(databases)

while True:
    print("메뉴 \n 1.데이터 추가 \n 2.데이터 검색\n 3.데이터 삭제")
    thing = int(input("메뉴를 선택하세요>"))
    if thing == 1:
        print("[데이터 추가]")
        a = input("추가할 데이터의 이름을 입력하세요>")
        b = int(input("추가할 데이터의 나이를 입력하세요>"))
        c = float(input("추가할 데이터의 성적을 입력하세요>"))
        databases.append({"name": a, "age": b, "score": c})
        print("추가됨")
        num += 1
    elif thing == 2:
        print("[데이터 검색]")
        search = input("검색할 데이터의 key와 value를 입력하세요>").split(":")
        flag = 0
        for i in range(num):
            for key, element in databases[i].items():
                if search[0] == key and search[1] == str(element):
                    print(databases[i])
                    flag = 1
        if flag == 0:
            print("입력한 이름을 갖는 데이터가 존재하지 않습니다.")
    elif thing == 3:
        print("[데이터 삭제}")
        d = input("삭제할 데이터의 이름을 입력하세요>")
        for i in range(num):
            if d == databases[i]["name"]:
                del databases[i]
                print("삭제됨.")
                num-=1
                break
databases = [{"name": "철수", "age": 21, "score": 4.3},
{"name": "영희", "age": 16, "score": 3.1},
{"name": "민수", "age": 24, "score": 3.9},
{"name": "길동", "age": 29, "score": 4.1}]

def menu_one():
    print("[데이터 추가]")
    a = input("추가할 데이터의 이름을 입력하세요>")
    try:
        b = int(input("추가할 데이터의 나이를 입력하세요>"))
        c = float(input("추가할 데이터의 성적을 입력하세요>"))
    except ValueError as exception:
        print(type(exception), exception)
        return menu_one()
    else:
        databases.append({"name": a, "age": b, "score": c})
        print("추가됨")
        with open("lee.txt", "a") as file:
            file.write("{}, {}, {}\n".format(a, b, c))

def menu_two():
    num = len(databases)
    print("[데이터 검색]")
    try:
        search = input("검색할 데이터의 key와 value를 입력하세요>").split(":")
        if len(search) != 2:
            raise ValueError
    except ValueError as exception:
        print("정확하게 key:vlaue로 입력하세요")
        print(type(exception), exception)
        return menu_two()
    else:
        flag = 0
        for i in range(num):
            for key, element in databases[i].items():
                if search[0] == key and search[1] == str(element):
                    print(databases[i])
                    flag = 1
        if flag == 0:
            print("입력한 데이터가 존재하지 않는다.")


def menu_three():
    try:
        num = len(databases)
        if num == 0:
            raise IndexError
        print("[데이터 삭제}")
        flag = 0
        d = input("삭제할 데이터의 이름을 입력하세요>")
        with open("lee.txt", "r") as file:
            moon = file.readlines()
        with open("lee.txt", "w") as file:
            for m in moon:
                (name, age, score) = m.strip().split(", ")
                if name != d:
                    file.write(m)
                else:
                    flag = 1
        if flag == 0:
            print("입력한 데이터가 존재하지 않는다.")
        else:
            print("삭제됨")
        for i in range(num):
            if d == databases[i]["name"]:
                del databases[i]
                break
    except FileNotFoundError as exception:
        print("파일을 찾을 수 없습니다. make.db 실행해주세요")
    except IndexError as exception:
        print("데이터베이스가 비었습니다.")
        print(type(exception), exception)


while True:
    print("메뉴 \n 1.데이터 추가 \n 2.데이터 검색\n 3.데이터 삭제")
    try:
        thing = int(input("메뉴를 선택하세요>"))
        if thing == 1:
            menu_one()
        elif thing == 2:
            menu_two()
        elif thing == 3:
            menu_three()
    except EOFError as exception:
        print(type(exception), exception)
        break
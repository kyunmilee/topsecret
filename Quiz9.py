import os
import random
import datetime

try:
    os.mkdir("current_time")
except FileExistsError:
    pass
with open("current_time/now.txt", "w") as file:
    files = os.listdir()
    file.write("현재 폴더의 목록: [{}] \n".format(", ".join(files)))

with open("current_time/now.txt", "a") as file:
    file.write("그 중에 하나를 랜덤하게 선택: {} \n".format(random.choice(files)))

now = datetime.datetime.now()
with open("current_time/now.txt", "a") as file:
    file.write("현재시각: {}".format(now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")))



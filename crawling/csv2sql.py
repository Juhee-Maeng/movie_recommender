import pandas as pd
import pymysql
import os
import json


# db 정보 불러오기
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRETS_DIR = os.path.join(BASE_DIR, '.secrets')
SECRETS_BASE = os.path.join(SECRETS_DIR, 'base.json')
secrets = json.loads(open(SECRETS_BASE, 'rt').read())

# csv 파일 불러오기
data = pd.read_csv("modified_movie.csv")

# db 연결
db = pymysql.connect(host=secrets['database_host'], port=int(secrets['database_port']), user=secrets['database_user'], password=secrets['database_password'], db=secrets['database_name'], charset='utf8')
cursor = db.cursor()

# 데이터 삽입
sql = "INSERT INTO movie_information (title, link, img_link, pubYear, userRating, director, actor, summary, nation, genre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
for i in range(len(data)):
    cursor.execute(sql, (str(data["title"][i]), str(data["link"][i]), str(data["img_link"][i]), str(data["pubYear"][i]), str(data["userRating"][i]), str(data["director"][i]), str(data["actor"][i]), str(data["summary"][i]), str(data["nation"][i]), str(data["genre"][i])))

# 커밋 후 연결 종료
db.commit()
db.close()

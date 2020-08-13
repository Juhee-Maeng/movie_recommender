import requests
from bs4 import BeautifulSoup
import re
import time


MAIN_URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200802&page='
LINK_URL = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code='
IMAGE_URL = 'https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode='
ACTOR_URL = 'https://movie.naver.com/movie/bi/mi/detail.nhn?code='


def get_link_ids():
    time.sleep(0.1)
    movie_ids = []
    for i in range(1, 41):  # 41로 수정
        time.sleep(0.1)
        req = requests.get(MAIN_URL + str(i))

        if req.status_code == 200:
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            movies = soup.find_all("a", {"class": False, "href": True, "title": True, "onclick": False})

            for movie in movies[2:]:
                number = re.search('[0-9]*$', movie['href']).group()  # 영화마다 부여된 번호
                movie_ids.append(number)
    return movie_ids


def get_contents(movie_id):
    '''
    movie_id : 영화마다 부여된 unique 번호
    '''
    time.sleep(0.1)

    # 1. link (= 영화 주소)
    link = LINK_URL + movie_id

    # 2. img_link(= 이미지 주소)
    img_link = IMAGE_URL + movie_id  # 영화 이미지 주소

    # 영화 url에서 정보를 받습니다.
    req = requests.get(link)
    if req.status_code == 200:
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        # 3. title(= 제목)
        try:
            title = soup.find('h3', {'class': 'h_movie'}).find('a', {'href': True}).text
            title = re.sub('[^0-9가-힣a-zA-Z ]', '', title)
        except:
            # 제목을 알아낼 수 없는 경우 -> 19금 영화라 로그인이 필요한 경우이다.
            return [""]*10

        # 4. userRating(= 네티즌 평점)
        try:
            userRating = soup.find_all('div', {'class': 'netizen_score'})[0].find_all('div', {'class': 'star_score'})[0].find(
                'em').text
        except:
            userRating = 0

        # 장르, 국가, 개봉년도 구하기
        try:
            info_spec = soup.find('dl', {'class':'info_spec'}).find_all('a')
            genre = []
            nation = []
            pubYear = False
            for i in range(len(info_spec)):
                if 'genre' in info_spec[i]['href']: # 장르
                    genre.append(info_spec[i].text)
                elif 'nation' in info_spec[i]['href']: # 국가
                    nation.append(info_spec[i].text)
                elif 'open' in info_spec[i]['href']: # 개봉년도
                    pubYear = info_spec[i].text
                    break
            genre = ','.join(genre)
            nation = ','.join(nation)
            if not pubYear:
                pubYear = ""
        except:
            genre = ""
            nation = ""
            pubYear = ""

        # 8. summary(= 줄거리)
        try:
            summary = soup.find('div', {'class':'story_area'}).find('p', {'class':'con_tx'})
            summary = re.sub('[^0-9a-zA-Z가-힣/. ]{1,}', '', summary.text).strip()
        except:
            summary = ""

        # director(= 감독) 과 actor(= 배우)정보를 얻기 위해 새로운 주소값으로 이동
        actor_link = ACTOR_URL + movie_id
        req = requests.get(actor_link)
        if req.status_code == 200:
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            # 9. director(= 감독)
            try:
                director = []
                for i in soup.find_all('div', {'class': 'dir_product'}):
                    director.append(i.find('a', {'class': 'k_name'})['title'])
                director = ','.join(director)
            except:
                director = ''

            # 10. actor(= 배우)
            try:
                actor = []
                for i in soup.find('ul', {'class': 'lst_people'}).find_all('a', {'class': 'k_name', 'href': True, 'title': True}):
                    actor.append(i['title'])
                actor = ','.join(actor)
            except:
                actor = ''

        # data에 정보 추가하기
        # 영화 id, 제목, link, 이미지link, 개봉일, 네티즌평점, 감독, 배우, 줄거리, 국가, 장르
        return [title, link, img_link, pubYear, userRating, director, actor, summary, nation, genre]

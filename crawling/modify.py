import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("movie.csv")

    # 성인인증 영화는 모두 공백으로 처리되어 있음 -> 따라서 해당 row들을 제거
    df = df.drop(df[df['title'].isnull()].index)

    # 값이 'nan'이면 0 혹은 ' '로 변경합니다.
    if df['pubYear'].isnull().sum() != 0:
        df['pubYear'] = df['pubYear'].fillna(0)

    if df['userRating'].isnull().sum() != 0:
        df['userRating'] = df['userRating'].fillna(0)

    if df['director'].isnull().sum() != 0:
        df['director'] = df['director'].fillna(" ")

    if df['actor'].isnull().sum() != 0:
        df['actor'] = df['actor'].fillna(" ")

    if df['summary'].isnull().sum() != 0:
        df['summary'] = df['summary'].fillna(" ")

    if df['nation'].isnull().sum() != 0:
        df['nation'] = df['nation'].fillna(" ")

    if df['genre'].isnull().sum() != 0:
        df['genre'] = df['genre'].fillna(" ")

    # pubYear이 float type을 띄고 있으므로, int형으로 col의 타입을 변환
    df['pubYear'] = df['pubYear'].astype('int')

    # 수정된 movie.csv 저장
    df.to_csv('modified_movie.csv', index=False, encoding='utf-8')

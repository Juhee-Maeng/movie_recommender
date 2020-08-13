from multiprocessing import Pool
import crawling
import pandas as pd


if __name__ == '__main__':
    pool = Pool(processes=4)
    data = list(pool.map(crawling.get_contents, crawling.get_link_ids()))

    columns = ['title', 'link', 'img_link', 'pubYear', 'userRating', 'director', 'actor', 'summary', 'nation', 'genre']
    df = pd.DataFrame(data, columns = columns)
    df.to_csv('movie.csv', index=False, encoding='utf-8')

import pandas as pd
import numpy as np

class movie_recommend:
    def __init__(self):
        column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        self.df = pd.read_csv('./u.data', sep='\t', names=column_names)
        self.movie_titles = pd.read_csv("./Movie_Id_Titles")
        self.df = pd.merge(self.df,self.movie_titles,on='item_id')
        self.moviemat = self.df.pivot_table(index='user_id',columns='title',values='rating')
        self.ratings = pd.DataFrame(self.df.groupby('title')['rating'].mean())
        self.ratings['num of ratings'] = pd.DataFrame(self.df.groupby('title')['rating'].count())
    
    def alike_movie(self,movie_name):
        movie_user_ratings = self.moviemat[movie_name]
        similar_to_movie = self.moviemat.corrwith(movie_user_ratings)
        corr_movie = pd.DataFrame(similar_to_movie,columns=['Correlation'])
        corr_movie.dropna(inplace=True)
        corr_movie = corr_movie.join(self.ratings['num of ratings'])
        return corr_movie[corr_movie['num of ratings']>100].sort_values('Correlation',ascending=False).head()

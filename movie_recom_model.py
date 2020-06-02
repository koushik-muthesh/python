import pandas as pd
#import numpy as np
data=pd.read_csv("D:/movie.CSV")
#print(data['color'])
l=len(data)
data.insert(0,'UserId',range(1,1+len(data)))
average_rating=pd.DataFrame(data.groupby('movie_title')['imdb_score'].mean())
average_rating['Total Ratings'] = pd.DataFrame(data.groupby('movie_title')['num_user_for_reviews'].count())
movie_user = data.pivot_table(index='UserId',columns='movie_title',values='num_user_for_reviews')
correlations = movie_user.corrwith(movie_user)
correlations.head(10)
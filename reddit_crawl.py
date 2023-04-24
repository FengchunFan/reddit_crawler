#reference used: https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
import praw
import pandas as pd
import csv
import os

#https://old.reddit.com/prefs/apps

reddit = praw.Reddit(client_id='5hgP0Pr-M7fOEg4wGS29aw', client_secret='zt70g1g4xPtseuy-AifqgHf2DWbetQ', user_agent='172_crawler')
#document = "collected_post.csv"
topics = ['ucr', 'riverside']

page_limit = 10000
page_counter = 0
max_file_size = 1 * 1024 * 1024  # 1 MB in bytes
current_file_size = 0
document_number = 1
document_size = 0

posts = []
for topic in topics:
    document = f"collected_reddits_{document_number}.csv"
    subreddit = reddit.subreddit(topic).hot(limit = 5000)
    for post in subreddit:
        if(page_counter < page_limit):
            posts.append([post.title, post.score, post.selftext, post.url, post.num_comments])
            page_counter = page_counter + 1
        else:
            break

posts = pd.DataFrame(posts,columns=['title', 'score', 'text', 'url', 'num_comments'])

#check if document exist in the first place
if os.path.exists(f'collected_reddits_{document_number}.csv'):
    document_size = os.path.getsize(document)
else:
    document_size = 0

#if maximum file size is reached, create a new file
if current_file_size + document_size > max_file_size:
    document_number = document_number + 1
    current_file_size = 0
    document = f"collected_reddits_{document_number}.csv"
posts.to_csv(document, index=False, header=True, encoding='utf-8') #save to a file, one post per row
current_file_size += document_size
#print(posts)
#posts.to_csv(document, index=False, header=True, encoding='utf-8') #save to a file, one post per row
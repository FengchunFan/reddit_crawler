#reference used: https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
import praw
import csv
import os
import sys

#https://old.reddit.com/prefs/apps

reddit = praw.Reddit(client_id='5hgP0Pr-M7fOEg4wGS29aw', client_secret='zt70g1g4xPtseuy-AifqgHf2DWbetQ', user_agent='172_crawler')
#document = "collected_post.csv"
topics = ['all']

page_limit = 1000
page_counter = 0
max_file_size = 0.1 * 1024 * 1024  # 0.1 MB in bytes
document_number = 1
document_size = 0
document = f"collected_reddits_{document_number}.csv"

posts = []
for topic in topics:
    subreddit = reddit.subreddit(topic).hot(limit = 10000)
    for post in subreddit:
        if(page_counter < page_limit):
            posts.append([post.title, post.score, post.subreddit, post.url, post.num_comments])
            page_counter = page_counter + 1
        else:
            break
print(len(posts))
print(page_counter)
    #collection = pd.DataFrame(posts,columns=['title', 'score', 'subreddit', 'url', 'num_comments'])

'''      
with open(document, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'score', 'subreddit', 'url', 'num_comments'])  # header row
    for post in posts:
        post_size = sys.getsizeof(post)
        document_size = os.path.getsize(document)
        if (post_size + document_size > max_file_size):
            document_number = document_number + 1
            document = f"collected_reddits_{document_number}.csv"
        else:
            writer.writerow(post)
'''
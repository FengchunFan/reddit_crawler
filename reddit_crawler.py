import praw
import csv
import os
import sys
import pandas as pd

reddit = praw.Reddit(client_id='5hgP0Pr-M7fOEg4wGS29aw', client_secret='zt70g1g4xPtseuy-AifqgHf2DWbetQ', user_agent='172_crawler')

topics = ['all']
page_limit = 2000
page_counter = 0
max_file_size = 0.1 * 1024 * 1024  # 1 MB in bytes
document_number = 1
document_size = 0
document = f"collected_reddits_{document_number}.csv"
posts = []

for topic in topics:
    subreddit = reddit.subreddit(topic).hot(limit=None)
    for post in subreddit:
        if page_counter < page_limit:
            posts.append([post.title, post.score, post.subreddit, post.url, post.num_comments])
            page_counter += 1
        else:
            print("reached page limit: ", page_limit)
            print(len(posts))
            break

df = pd.DataFrame(posts, columns=['title', 'score', 'subreddit', 'url', 'num_comments'])

df.to_csv(document, index=False)

'''
with open(document, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'score', 'subreddit', 'url', 'num_comments'])  # header row
    for post in posts:
        writer.writerow(post)

'''
'''
def post_to_file(posts, document):
    global document_number
    index = -1
    with open(document, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'score', 'subreddit', 'url', 'num_comments'])  # header row
        for post in posts:
            index += 1
            post_size = sys.getsizeof(post)
            document_size = os.path.getsize(document)
            if post_size + document_size > max_file_size:
                document_number += 1
                document = f"collected_reddits_{document_number}.csv"
                post_to_file(posts[index:], document)
            else:
                writer.writerow(post)

post_to_file(posts, document)
'''

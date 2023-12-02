import csv
import os
import pandas as pd
from facebook_scraper import get_posts
from dotenv import load_dotenv
load_dotenv()

page_name = 'transportforlondon'
fname = page_name + '.csv'
output_file = fname
no_of_pages = 1
fieldnames = ['time', 'text', 'comments', 'comments_full']

# data = pd.read_csv(fname, encoding='utf-8')
#To do: auto create new file if file does not exist
#To do: check if date is greater than yesterday
posts = get_posts(page_name, pages=no_of_pages, credentials=(os.getenv('facebookusername'), os.getenv('facebookpassword')), options={"comments": True})
data_temp = pd.DataFrame(columns=fieldnames)
for post in posts:
    post_temp = pd.DataFrame({"time":post["time"], "text":post["text"], "comments":post["comments"], "comments_full":post["comments_full"]})
    data_temp = pd.concat([data_temp, post_temp], ignore_index=True)
'''
original idea(but failed miserably):
for post in posts:
    postlist = []
    postitem = {"post_id":[], "time":[], "text":[], "comments_full":[]}
    postitem["post_id"].append(post["post_id"])
    postitem["time"].append(post["time"])
    postitem["text"].append(post["text"])
    postitem["comments_full"].append(post["comments_full"])
    postlist.append(postitem)
'''

try:
    data = pd.read_csv(fname, encoding='utf-8')
    output = pd.concat([data, data_temp], ignore_index=True).to_csv(output_file, index=False, encoding='utf-8')
    output.to_csv(output_file, index=False, encoding='utf-8')
except:
    data_temp.to_csv(output_file, index=False, encoding='utf-8')
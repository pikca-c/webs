import csv
import os
import pandas as pd
from facebook_scraper import get_posts
from dotenv import load_dotenv
load_dotenv()

pages = [ 'transportforlondon'] #function to scrape multiple pages
fname = "facebook_page" + '.csv'
output_file = fname
no_of_pages = 1
fieldnames = ['time', 'text', 'comments', 'comments_full']

# data = pd.read_csv(fname, encoding='utf-8')
#To do: auto create new file if file does not exist

data_previous = pd.read_csv(fname, encoding='utf-8')
data_temp = pd.DataFrame(columns=fieldnames,)
pageno = 0

for page in len(pages):
    posts = get_posts(pages[pageno], pages=no_of_pages, credentials=(os.getenv('facebookusername'), os.getenv('facebookpassword')), options={"comments": True})
    data_previous = pd.read_csv(fname, encoding='utf-8')
    data_temp = pd.DataFrame(columns=fieldnames)
    for post in posts:
        if post["post_id"] in data_previous.index:
            continue
        else:
            post_temp = pd.DataFrame({"time":post["time"], "text":post["text"], "comments":post["comments"], "comments_full":",".join(["comments_full"])}, index=["post_id"])
            print(post_temp)
            data_temp = pd.concat([data_temp, post_temp], ignore_index=True)
    pageno = pageno + 1

try:
    data = pd.read_csv(fname, encoding='utf-8')
    output = pd.concat([data_previous, data_temp], ignore_index=True).to_csv(output_file, index=False, encoding='utf-8')
    output.to_csv(output_file, index=False, encoding='utf-8')
except:
    data_temp.to_csv(output_file, index=False, encoding='utf-8')
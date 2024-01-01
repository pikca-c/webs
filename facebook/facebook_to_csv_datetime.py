import csv
import datetime
import os 
from facebook_scraper import get_posts
from dotenv import load_dotenv
load_dotenv()

page_name = 'avantiwestcoastrail'
fname = page_name + "_"+ datetime.date.today().strftime("%Y%m%d") + '.csv'
no_of_pages = 10
fieldnames = ['Date', 'Post Content', 'Post Comments', 'Commenter', 'Comment Number', 'Comment Text']
credential = (os.getenv('facebookusername'), os.getenv('facebookpassword'))
base_url="https://mbasic.facebook.com"
start_url="https://mbasic.facebook.com/"+ page_name + "?v=timeline"
# set_user_agent("Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")


with open(fname, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for post in get_posts(page_name, pages=no_of_pages,base_url=base_url,start_url=start_url, options={"comments": True}):
        print("post:",post)
        writer.writerow({'Date': post['time'], 'Post Content': post['text'], 'Post Comments': post['comments']})
        no = 0
        for comment in post['comments_full']:
            no = no + 1 
            writer.writerow({'Commenter': comment['commenter_name'], 'Comment Number': no, 'Comment Text': comment['comment_text']})
    csvfile.close()
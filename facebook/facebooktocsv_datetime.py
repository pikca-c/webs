import csv
import datetime
from facebook_scraper import get_posts

page_name = 'avantiwestcoastrail'
fname = page_name + "_"+ datetime.date.today().strftime("%Y%m%d") + '.csv'
no_of_pages = 1
fieldnames = ['Date', 'Post Content', 'Post Comments', 'Commenter', 'Comment Number', 'Comment Text']

with open(fname, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for post in get_posts(page_name, pages=no_of_pages, credentials=('wjones2562@gmail.com', 'bA25C558Ym!RMC+'), options={"comments": True}):
        writer.writerow({'Date': post['time'], 'Post Content': post['text'], 'Post Comments': post['comments']})
        no = 0
        for comment in post['comments_full']:
            no = no + 1 
            writer.writerow({'Commenter': comment['commenter_name'], 'Comment Number': no, 'Comment Text': comment['comment_text']})
    csvfile.close()
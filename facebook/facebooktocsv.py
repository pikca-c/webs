import csv
from facebook_scraper import get_posts

with open("facebook.csv", 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Date', 'Post Content', 'Post Comments', 'Commenter', 'Comment Number', 'Comment Text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for post in get_posts('avantiwestcoastrail', pages=1, credentials=('*@gmail.com', '**'), options={"comments": True}):
        writer.writerow({'Date': post['time'], 'Post Content': post['text'], 'Post Comments': post['comments']})
        no = 0
        for comment in post['comments_full']:
            no = no + 1 
            writer.writerow({'Commenter': comment['commenter_name'], 'Comment Number': no, 'Comment Text': comment['comment_text']})
    csvfile.close()
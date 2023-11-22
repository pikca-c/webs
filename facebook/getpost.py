#Credentials required to access the facebook page
from facebook_scraper import get_posts

for post in get_posts('avantiwestcoastrail', pages=1, credentials=('**@gmail.com', '***'), options={"comments": True}):
    print(f"Date: {post['time']}")
    print(f"Post Content: {post['text']}")
    print(f"Post Comments {post['comments']}")
    no = 0
    for comment in post['comments_full']:
        no = no + 1 
        print(f"Commenter: {comment['commenter_name']}")
        print(f"Comment Number {no}: {comment['comment_text']}")
        print("\n")
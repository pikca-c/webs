#Credentials required to access the facebook page
from facebook_scraper import get_posts

for post in get_posts('avantiwestcoastrail', pages=1, credentials=('****@gmail.com', '***'), options={"comments": True}):
    print(post)
    print(post['text'])
    print(post['comments'])
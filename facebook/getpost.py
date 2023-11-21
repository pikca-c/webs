#Needs credentials to run
from facebook_scraper import get_posts

for post in get_posts('NintendoUK', pages=3, credentials=('****@gmail.com', '******')):
    print(post['text'][:50])
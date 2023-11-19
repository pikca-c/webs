"""
Download comments for a public Facebook post.
"""

import facebook_scraper as fs

# get POST_ID from the URL of the post which can have the following structure:
# https://www.facebook.com/USER/posts/POST_ID
# https://www.facebook.com/groups/GROUP_ID/posts/POST_ID
POST_ID = "pfbid031dqgvPZrHrNfYcgHEC1Ag8uXttyinWtJ5Ehef22NEWZjT4i3JbEFrcULaDkrmsk7l"

# number of comments to download -- set this to True to download all comments
MAX_COMMENTS = 100

# get the post (this gives a generator)
gen = fs.get_posts(
    post_urls=[POST_ID],
    options={"comments": MAX_COMMENTS, "progress": True}
)

# take 1st element of the generator which is the post we requested
post = next(gen)

# extract the comments part
comments = post['comments_full']

# process comments as you want...
for comment in comments:

    # e.g. ...print them
    print(comment)

    # e.g. ...get the replies for them
    for reply in comment['replies']:
        print(' ', reply)

for i in range(1, 101):
    fs.write_posts_to_csv(
        group=GROUP_ID, # The method uses get_posts internally so you can use the same arguments and they will be passed along
        page_limit=100,
        timeout=60,
        options={
            'allow_extra_requests': False
        },
        filename=f'./data/messages_{i}.csv', # Will throw an error if the file already exists
        resume_file='next_page.txt', # Will save a link to the next page in this file after fetching it and use it when starting.
        matching='.+', # A regex can be used to filter all the posts matching a certain pattern (here, we accept anything)
        not_matching='^Warning', # And likewise those that don't fit a pattern (here, we filter out all posts starting with "Warning")
        keys=[
            'post_id',
            'text',
            'timestamp',
            'time',
            'user_id'
        ], # List of the keys that should be saved for each post, will save all keys if not set
        format='csv', # Output file format, can be csv or json, defaults to csv
        days_limit=3650 # Number of days for the oldest post to fetch, defaults to 3650
    )
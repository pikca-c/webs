import facebook_scraper as fs

for i in range(1, 5):
    fs.write_posts_to_csv(
        group="UKRailtours", # The method uses get_posts internally so you can use the same arguments and they will be passed along
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
        days_limit=5 # Number of days for the oldest post to fetch, defaults to 3650
    )
import csv
import os
import pandas as pd
from facebook_scraper import get_posts
from dotenv import load_dotenv
load_dotenv()

page_name = 'avantiwestcoastrail'
fname = page_name + '.csv'
output_file = "test.csv"
no_of_pages = 1
fieldnames = ['Date', 'Post Content', 'Post Comments', 'Commenter', 'Comment Number', 'Comment Text']

data = pd.read_csv(fname, encoding='utf-8')
data_temp = get_posts(page_name, pages=no_of_pages, credentials=(os.getenv('facebookusername'), os.getenv('facebookpassword')), options={"comments": True})
data_temp = pd.DataFrame(data_temp)
print(data_temp)
data[fieldnames[0]] = "123"
pd.concat([data, data_temp], ignore_index=True).to_csv(output_file, index=False, encoding='utf-8')
data.to_csv(output_file, index=False, encoding='utf-8')
output = pd.DataFrame(columns=fieldnames)
for filename in os.path("./folder") :
    data = pd.read_csv(filename, encoding='utf-8')
    pd.concat([output, data], ignore_index=True)

output.to_csv(output_file, index=False, encoding='utf-8')
'''
1. Read in the csv file -> new dataframe
2. run the facebook_scraper -> data
3. data -> dataframe (multi columns problems to be solved) + post_id
4. check if post_id exists in the dataframe
    a. if yes, skip
    b. if no, append
5. merge the two dataframes
6. write to csv
7. mulit pages fetch

data structure(Post):
Post_ID(index) 
Date
post content
comments : [comment]
...
'''	

import csv
import os
import pandas as pd
from facebook_scraper import get_posts


page_name = 'avantiwestcoastrail'
fname = page_name + '.csv'
output_file = "test.csv"
no_of_pages = 1
fieldnames = ['Date', 'Post Content', 'Post Comments', 'Commenter', 'Comment Number', 'Comment Text']

data = pd.read_csv(fname, encoding='utf-8')
data_temp = data.copy()
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
3. data -> dataframe
4. merge the two dataframes
5. write to csv

data structure:
Post_ID(index) 
Date
post content
comments : [comment]
...

if date > yesterday:
do sth. -> append in csv

'''	

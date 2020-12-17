import csv
from urllib import urlopen
import re

# Open and read HTMl / XML
xml = urlopen("https://www.imdb.com/search/title/?genres=comedy&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=E2BNXY3K4AK3AYB8TW0F&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_1' + str(page) + '&ref_=adv_nxt', headers=headers)").read()

# Grab article titles and links using regex
xmlTitle = re.compile("&lt;title&gt;(.*)&lt;/title&gt;")
xmlLink = re.compile("&lt;link&gt;(.*)&lt;/link&gt;")

# Find and store the data
findTitle = re.findall(xmlTitle,xml)
findLink = re.findall(xmlLink,xml)

#Iterate through the articles to create a range
iterate = []
iterate[:] = range(1, 25)

# Open the CSV file, write the headers
writer = csv.writer(open("pytest.csv", "wb"))
head = ("Title", "URL")
writer.writerow(head)

# Using a For Loop, write the results to the CSV file, row by row
for i in iterate:
	writer.writerow([findTitle[i], findLink[i]])
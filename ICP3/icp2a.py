from bs4 import BeautifulSoup
import urllib.request
import os

# Set the url to variable and open it
url="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
urllib.request.urlopen(url)
source_code = urllib.request.urlopen(url)
plain_text = source_code

# parse the html content using Beautiful soup library
soup = BeautifulSoup(plain_text, "html.parser")

# print the title of the page
print(soup.title)

# find all the elements with tag <a>
atag=soup.find_all('a')

# iterate each <a> tag and get the elements with href attribute
for eachtag in atag:
    href=eachtag.get('href')
    print(href)
    #print(atag)

# create an empty list,
th_list = []

# Find the table with specified class iterate through each row
for rows in soup.find_all('table', class_='wikitable sortable plainrowheaders') :

    rows_1 = rows.find_all('tr')
    # Find the data tag td in each row and print the text in it
    for row in rows_1:
        td = row.find_all("td")
        for i in td:
            print(i.text)

            # Find the header tag and print the text that is not already in th text
            th = row.find("th")
            if th.text not in th_list:
                th_list.append(th.text)
                print("State or Union Territory:  ", th.text)

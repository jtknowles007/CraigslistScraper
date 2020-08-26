#! /usr/bin/env python3

from craigslist import CraigslistForSale
import re
import datetime

i = 0
mysite = 'muncie'
myzipcode = 46013
mydistance = 100
myquery = '(bandsaw|\"band saw\")'

thesearch = CraigslistForSale(site=mysite, 
        filters = {'query':myquery,
            'search_titles':True,
            'zip_code':myzipcode,
            'search_distance':mydistance})

print("Search: {}\nZip Code: {}\nDistance: {} miles".format(myquery,myzipcode,mydistance))
print("==================================================\n\n")
for result in thesearch.get_results(sort_by='newest'):
    i=i+1
    itemnumber = str(i)
    itemname = result['name']
    itemprice = result['price']
    itemdatestring = result['datetime']
    itemdatestringtodate = datetime.datetime.strptime(itemdatestring, '%Y-%m-%d %H:%M')
    itemdate = itemdatestringtodate.strftime('%b %d, %Y')
    itemurl = result['url']
    itemlocation = re.findall(r'\/\/(.*?)\.',itemurl)

    print("{}) {} {}".format(itemnumber,itemname.upper(),itemprice))
    print(itemdate)
    print(itemlocation[0].capitalize())
    print(itemurl)
    print(" ")
print("==================================================")


"""

Code Challenge
  Name: 
    Post Codes Germany
  Filename: 
    postcodes_germany.py
  Problem Statement: (post_codes_germany.txt, zuordnung_plz_ort.csv )
    We have to bring together the information of two files. 
    In the first file, we have a list of nearly 15000 lines of post codes with the 
    corresponding city names plus additional information. 

    The other file contains a list of the 19 largest German cities. 
    Each line consists of the rank, the name of the city, the population, 
    and the state (Bundesland): 
    
    Our task is to create a list with the top 19 cities,
    with the city names accompanied by the postal code. 
    If you want to test the following program, 
    you have to save the list above in a file called largest_cities_germany.txt 
    and you have to download and save the list of German post codes

  Output:
    The output of this file looks like this, 
    but we have left out all but the first three postal codes for every city: 
    
        Berlin {'10715', '13158', '13187', ...}
        Hamburg {'22143', '22119', '22523', ...}
        München {'80802', '80331', '80807', ...}
        Köln {'51065', '50997', '51067', ...}
        Frankfurt am Main {'65934', '60529', '60308', ...}
        Essen {'45144', '45134', '45309', ... }
        Dortmund {'44328', '44263', '44369',...}
        Stuttgart {'70174', '70565', '70173', ...}
        Düsseldorf {'40217', '40589', '40472', ...}
        Bremen {'28207', '28717', '28777', ...}
        Hannover {'30169', '30419', '30451', ...}
        Duisburg {'47137', '47059', '47228', ...}
        Leipzig {'4158', '4329', '4349', ...'}
        Nürnberg {'90419', '90451', '90482', ...}
        Dresden {'1217', '1169', '1324', ...}
        Bochum {'44801', '44892', '44805', ...}
        Wuppertal {'42109', '42119', '42287', ...}
        Bielefeld {'33613', '33607', '33699', ...}
        Mannheim {'68161', '68169', '68167', ...}
      
  Hint: 
    Using Regular Expression 
    zuordnung_plz_ort.csv
    list of nearly 15000 lines of post codes with the corresponding city names 
    plus additional information.

"""
import pandas as pd
import requests as re

url = 'https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population'
html = re.get(url).content 
postcode=pd.read_csv('C:/Users/Suraj  kumar/Desktop/Forsk_Lab/Regular_Expression/zuordnung_plz_ort.csv')
postcode.drop(['osm_id','bundesland'],axis=1,inplace=True)
postcode.drop([0],axis=0,inplace=True)
postcode.columns=['City','Postcode']
data = pd.read_html(html)

new_data = data[0].head(20)

new_data.drop([2,3,4,5,6,7,8],axis=1,inplace=True)
new_data.drop([0],axis=0,inplace=True)
new_data.columns=['Rank','City']

merged_data=pd.merge(new_data,postcode,on='City')
merged_data.drop(['Rank'],axis=1,inplace=True)
merged_data['Postcode']=merged_data['Postcode'].apply(str)
merged_data=merged_data.groupby('City')
merged_data.first()
#merged_data.get_group('Berlin')
#merged_data.to_dict('series')
merged_data = merged_data.groupby('City')['Postcode'].apply(', '.join).reset_index()
merged_data.to_dict()

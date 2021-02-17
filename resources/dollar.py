from flask_restful import Resource
from bs4 import BeautifulSoup
import requests
import pandas as pd


class Dollar(Resource):
  def get(self):
    # Add header and  url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    url = "https://www.rava.com/"
    r = requests.get(url)

    # Initiate beautiful and list element to extract all the rows in the table
    soup = BeautifulSoup(r.content, "html.parser")
    table = soup.findAll("table", {"class": ["tablapanel2"]})[0]
    rows = table.find_all('tr')
    row_list = list()

    # Iterate through all of the rows in table and get through each of the cell to append it into rows and row_list
    for tr in rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        row_list.append(row)

    # removes 1st row (column titles)
    del row_list[0]
 
    # Create Pandas Dataframe
    df_bs = pd.DataFrame(row_list,columns=['Especie','Ultimo','Dia', 'Mes', 'Ano'])

    # return as json
    return(df_bs.to_json(orient='records'),200)

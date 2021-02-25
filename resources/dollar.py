from flask_restful import Resource
from flask.wrappers import Response
#import requests
#from bs4 import BeautifulSoup
import pandas as pd
from .func import table2json 


class Dollar(Resource):
  def get(self):

    # table index = 0 Dollar table
    row_list = list()
    row_list = table2json(0)

    # Create Pandas Dataframe
    # Adds column names
    df_bs = pd.DataFrame(row_list,columns=['Especie','Ultimo','Dia', 'Mes', 'Ano'])

    # return as json
    resp = Response(response=df_bs.to_json(orient='index'),
        status=200,
        mimetype="application/json")

    return(resp)
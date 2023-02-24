import csv
from statistics import mean
from threading import local
from turtle import down, width
from unicodedata import decimal
from numpy import sort
import pandas as pd
from bokeh.plotting import figure, show
from decimal import * 
import itertools
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6, Magma, Inferno, Plasma, Viridis, Cividis, Category10_10
from bokeh.plotting import figure, output_file, save
from bokeh.transform import factor_cmap
import pandas_bokeh
import random


#Tri colonne et header fichier final
used_cols = [1, 2, 10]
headercsv = ['Period', 'Data_value', 'Series_title_2']
fichier = pd.read_csv("/Users/theorobert/Desktop/scrapping/dc5b_clean_td_ROBERT_Theo/electronic-card-transactions-december-2022-csv-tables.csv", usecols=used_cols)

#Supprime ligne vide et garde Credit|Debit|Services
fichier = fichier.dropna()
fichier = fichier[fichier['Series_title_2'].str.contains('^(Credit|Debit|Services)$')]

#reset de l'index
fichier = fichier.reset_index(drop=True)
fichier.index.name = 'ID'
#fichier final
fichier.to_csv('/Users/theorobert/Desktop/scrapping/dc5b_clean_td_ROBERT_Theo/exo 3 Python/result.csv', header=headercsv, index=True)

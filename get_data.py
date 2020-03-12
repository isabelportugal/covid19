import urllib.request
import os

working_dir = os.getcwd()
output_dir = working_dir + '/data/'

os.mkdir(working_dir + '/data')

file_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

confirmations = 'time_series_19-covid-Confirmed.csv'
deaths = 'time_series_19-covid-Deaths.csv'
recover = 'time_series_19-covid-Recovered.csv'

urllib.request.urlretrieve(file_url + confirmations, output_dir + confirmations)
urllib.request.urlretrieve(file_url + deaths, output_dir + deaths)
urllib.request.urlretrieve(file_url + recover, output_dir + recover)

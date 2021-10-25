import plotly.express as px
import pandas as pd
import csv

with open("Size of TV,_Average time spent watching TV in a week (hours).csv") as csv_file:
      df = pd.read_csv(csv_file)
      fig = px.scatter(df, x = "Size of TV", y = "\tAverage time spent watching TV in a week (hours)")
      fig.show()
import plotly.express as px
import pandas as pd
import csv

with open("Student Marks vs Days Present.csv") as csv_file:
      df = pd.read_csv(csv_file)
      fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
      fig.show()
    
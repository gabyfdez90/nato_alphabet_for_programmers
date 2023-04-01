import pandas as pd
import os

#Create a function that gets the data from the csv file and convert it into a dataframe
def get_alphabet():
    csv_path = os.path.join(os.path.dirname(__file__), 'alphabet_for_programmers.csv')
    alphabet_df = pd.read_csv(csv_path)
    return alphabet_df
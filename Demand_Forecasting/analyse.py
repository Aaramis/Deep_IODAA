import pandas as pd

from utils import write_logs
from rich import print as rprint

class analyse():

    def __init__(self) -> None:
        self.train = pd.read_csv('./data/train.csv', parse_dates=['date'])
        self.test = pd.read_csv('./data/test.csv', parse_dates=['date'])

    def display_info_df(self, df : pd.DataFrame, df_name : str):
        rprint("-----------------------------------------------------")
        rprint(f"                       {df_name.upper()} SET                     ")
        rprint("-----------------------------------------------------\n")

        rprint(df.describe())
        rprint(f"\n {df.head()}\n")


    def get_date_min_max(self, df : pd.DataFrame) -> int :
        """
        Get the oldest and the most recent day of a dataset
        """
        col_day = df.columns[df.dtypes == 'datetime64[ns]'].tolist()
        if len(col_day) :
            date_min  = df['date'].min().date()
            date_max  = df['date'].max().date()
            return date_min, date_max
        else :
            write_logs("There is no datetime colonne in this dataframe", "critical", True)
import pandas as pd
import sys
import logging
import subprocess
import os 

from rich import print as rprint

from utils import write_logs

### Loading data
train = pd.read_csv('./data/train.csv', parse_dates=['date'])
test = pd.read_csv('./data/test.csv', parse_dates=['date'])

rprint("-----------------------------------------------------")
rprint("                       TRAIN SET                     ")
rprint("-----------------------------------------------------\n")

rprint(train.describe())
rprint(f"\n {train.head()}\n")



rprint("-----------------------------------------------------")
rprint("        Time period of the train dataset             ")
rprint("-----------------------------------------------------\n")

def get_date_min_max(df : object ) -> int :
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


def main():

    log_file = os.path.join(f'{".log"}')

    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s :: %(module)s:%(lineno)d :: %(levelname)s :: %(message)s',
        datefmt="%d-%m-%Y %H:%M:%S",
        filemode='w'
    )
    rprint(f"Started logging here: {log_file}")
    logging.info('Started logging')

    last_commit = os.popen('git rev-parse HEAD').read().strip()
    write_logs(msg=f"Last Deep_IODAA commit: {last_commit}", status="info")
    write_logs(msg=f"Running command: python {subprocess.list2cmdline(sys.argv)}", status="info")

    test = pd.DataFrame()

    train_d_min, train_d_max = get_date_min_max(test)
    rprint(f"\nMin date from train set: {train_d_min}")
    rprint(f"Max date from train set: {train_d_max}")
    return 

if __name__ == "__main__":
    sys.exit(main())

# train_d_min, train_d_max = get_date_min_max(train)
# lag_size = (test['date'].max().date() - train['date'].max().date()).days
# rprint(f"Max date from test  set: {test['date'].min().date()}")
# rprint(f"Max date from test  set: {test['date'].max().date()}")
# rprint(f"Number of day to predict, {lag_size}")
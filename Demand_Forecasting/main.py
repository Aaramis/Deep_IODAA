import logging
import os
import subprocess
import sys
import pandas as pd

from rich import print as rprint
from utils import write_logs
from 


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

import os
import pandas as pd


def read_frmgham():
    """
    Function reads frmgham2.csv file and returns a DataFrame.

    :return: Pandas DataFrame
    """
    # Obtain pathway of csv file
    abspath = os.path.abspath(__file__)  # obtain absolute pathway to file
    head_path, filename = os.path.split(abspath)
    data_path = os.path.join(head_path, 'frmgham2.csv') # data pathway

    # Create DataFrame
    df = pd.read_csv(data_path)
    df['SEX'].replace(to_replace={1:'male', 2:'female'}, inplace=True)
    return df
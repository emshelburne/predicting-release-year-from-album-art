# General helper functions for notebooks

import pandas as pd 


# Function to examine dataframes

def examine_df(df: pd.DataFrame,
               name: str = 'this dataframe',
               include_stats: bool = True,
               include_sample: bool = True) -> None:
    """
    Check basic info about a dataframe df
    """
    
    print(f"\n\nNumber of records in {name} is: {len(df)}\n")
    print(f"\n\nNumber of features in {name} is: {len(df.columns)}\n")
    print(f"The columns in {name} are: {df.columns}\n")
    print(f"\n Other info about {name}:\n")
    print(df.info())
    if include_stats == True:
        print(f'\n Basic statistical info about {name}:\n')
        print(df.describe())
    if include_sample == True:
        print(f"\n\nSample of records in {name}:")
        print(df.head(5))
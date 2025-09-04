# DS 5032
# Assignment 1
# Author: Luedtke, Terry
# Email: epf7ch@virginia.edu

import numpy as np
import pandas as pd

# %% 
# Question 3

def download_data(force=False):
    """Download and extract course data from Zenodo."""
    import urllib.request
    import zipfile
    import os
    
    zip_path = 'data.zip'
    data_dir = 'data'
    
    if not os.path.exists(zip_path) or force:
        print("Downloading course data...")
        urllib.request.urlretrieve(
            'https://zenodo.org/records/16954427/files/data.zip?download=1',
            zip_path
        )
        print("Download complete")
    
    if not os.path.exists(data_dir):
        print("Extracting data files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Data extracted")
    
    return data_dir

download_data()

# %%
# Question 4

df = pd.read_csv('data/metabric.csv')
df
# %%
# Question 5

print(df['Type of Breast Surgery'].value_counts())
print(df['Overall Survival (Months)'].describe())

# %%
# Question 6
"""
The data could be used to determine at what ages women should be 
screened for breast cancer. The ECDF (and related graphs) could show 
when the age range of the highest rate of occurrence, and therefore
the highest value for screening. However the data needs to be evaluated
against general life expectancy data. In particular, the drop in 
occurences after age 80 could be simply due to a reduced population,
rather than a lower risk of breast cancer.
"""


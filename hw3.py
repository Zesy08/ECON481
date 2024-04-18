#!/usr/bin/env python
# coding: utf-8

# In[117]:


def github() -> str:
    """
    Returns Github link.
    """

    return "https://github.com/Zesy08/ECON481/blob/main/hw3.py"


# In[118]:


import pandas as pd

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    result = pd.DataFrame()
    
    for year in years:
        url = f"https://lukashager.netlify.app/econ-481/data/ghgp_data_{year}.xlsx"
        test = pd.read_excel(url, sheet_name = 'Direct Emitters', index_col = False, skiprows = 3)
        test["year"] = year
        result = pd.concat([result, test], ignore_index = True)

    return result


# In[119]:


import pandas as pd

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    result = pd.DataFrame()

    for year in years:
        url = f"https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb"
        test = pd.read_excel(url, sheet_name = year, index_col = False)
        test["year"] = year
        result = pd.concat([result, test], ignore_index = True)

    result = result.dropna(how = 'all')
    return result


# In[120]:


def n_null(df: pd.DataFrame, col: str) -> int:
    """
    Returns amount of nulls in a certain column
    """

    return df[col].isnull().sum()


# In[121]:


def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Some docstrings.
    """
    temp = pd.merge(emissions_data, parent_data, left_on=['year', 'Facility Id'], right_on=['year', 'GHGRP FACILITY ID'], how='left')

    result = temp[['Facility Id', 'year', 'State', 'Industry Type (sectors)', 
                   'Total reported direct emissions', 'PARENT CO. STATE', 'PARENT CO. PERCENT OWNERSHIP']]

    result.columns = map(str.lower, result.columns)

    return result


# In[122]:


def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Some docstrings.
    """
    ans = df.groupby(group_vars).agg({'total reported direct emissions': ['min', 'median', 'mean', 'max'], 
                                      'parent co. percent ownership': ['min', 'median', 'mean', 'max']}, as_index=True)
    
    ans = ans.sort_values(by=('total reported direct emissions', 'mean'), ascending=False)

    return ans


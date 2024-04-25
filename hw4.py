#!/usr/bin/env python
# coding: utf-8

# In[175]:


def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/Zesy08/ECON481/blob/main/hw4.py"


# In[176]:


import pandas as pd

def load_data() -> pd.DataFrame:
    """
    Some docstrings.
    """

    url = f'https://lukashager.netlify.app/econ-481/data/TSLA.csv'
    result = pd.read_csv(url, index_col = 0, parse_dates = True)

    return result


# In[177]:


import matplotlib.pyplot as plt

def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Some docstrings
    """

    data = df['Close']

    fig, ax = plt.subplots()

    data.plot(ax=ax, color = "black")

    plt.ylabel('Closing Price')
    ax.set_title("Closing Price from " + Start + " to " + End)
    ax.set_xlim([Start, End])


# In[178]:


import statsmodels.api as sm

def autoregress(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """

    data = df[['Close']]

    data = data.diff()

    data['Lagged'] = data.shift(periods = 1)
    
    data = data.dropna()
    
    model = sm.OLS(data['Close'], data['Lagged'])

    result = model.fit(cov_type='HC1')

    return result.tvalues


# In[179]:


import statsmodels.formula.api as smf

def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Some docstrings.
    """

    data = df[['Close']]

    data['Change'] = data.diff()

    data['Lagged'] = data['Change'].shift(periods = 1)
    data['Positive'] = (data['Change'] > 0).astype(int)
    
    data = data.dropna()

    result = smf.logit('Positive ~ Lagged', data = data).fit()
    
    return result.tvalues['Lagged']


# In[180]:


def plot_delta(df: pd.DataFrame) -> None:
    """
    Some docstrings.
    """

    data = df['Close'].diff()

    fig, ax = plt.subplots()

    data.plot(ax=ax, color = "black")
    plt.ylabel('Delta Closing Price')
    ax.set_title("Change in Closing Price over time")


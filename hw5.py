#!/usr/bin/env python
# coding: utf-8

# In[56]:


def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/Zesy08/ECON481/blob/main/hw5.py"


# In[54]:


import requests
from bs4 import BeautifulSoup

def scrape_code(url: str) -> str:
    """
    Some docstrings.
    """
    r1 = requests.get(url)
    assert r1.ok
    r1_bs = BeautifulSoup(r1.text)

    total_code = [x.text for x in r1_bs.find_all('code', class_ = 'sourceCode python')]
    result = ''

    for curr_code in total_code:
        code = curr_code.strip()

        if not code.startswith('%'):
            result += code + '\n'

    return result.strip()


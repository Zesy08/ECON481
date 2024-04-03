#!/usr/bin/env python
# coding: utf-8

def github() -> str:
    return "https://github.com/Zesy08/ECON481/blob/main/hw1.py"

def evens_and_odds(n: int) -> dict:
    my_dict = {
        'evens': 0,
        'odds': 0
    }
    for i in range(n):
        if i % 2 == 0:
            my_dict['evens'] += i
        else:
            my_dict['odds'] += i
    return my_dict

from typing import Union
from datetime import datetime, date, time, timedelta

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    dt1 = datetime.strptime(date_1, "%Y-%m-%d")
    dt2 = datetime.strptime(date_2, "%Y-%m-%d")
    diff = (dt2-dt1).days
    
    if diff < 0:
        diff *= -1
        
    if (out == 'string'):
        return "There are " + str(diff) + " days between the two dates"
        
    return diff

def reverse(in_list: list) -> list:
    rev_list = []
    i = len(in_list) - 1
    while i > -1:
        rev_list.append(in_list[i])
        i -= 1

    return rev_list


def prob_k_heads(n: int, k: int) -> float:
    
    n_minus_k_fac = 1
    for i in range(1,n-k+1):
        n_minus_k_fac *= i
        
    n_choose_k = 1
    for i in range(k+1, n+1):
        n_choose_k *= i
    n_choose_k /= n_minus_k_fac

    return n_choose_k * (0.5**k) * (0.5**(n-k))


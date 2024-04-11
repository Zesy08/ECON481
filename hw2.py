#!/usr/bin/env python
# coding: utf-8

# In[55]:


def github() -> str:
    """
    Returns Github link.
    """

    return "https://github.com/Zesy08/ECON481/blob/main/hw2.py"


# In[53]:


import numpy as np

def simulate_data(seed=481) -> tuple:
    
    rng = np.random.default_rng(seed=seed)
    x_draws = rng.normal(0, np.sqrt(2), size=1000*3).reshape((1000,-1))
    e = rng.standard_normal(size=1000).reshape(1000)

    y = 5 + 3*x_draws[:, 0] + 2*x_draws[:, 1] + 6*x_draws[:, 2] + e

    return (y, x_draws)


# In[54]:


import numpy as np
import scipy as sp

def estimate_mle(y: np.array, X: np.array) -> np.array:

    opt_values = sp.optimize.minimize(
        fun = mle,
        x0 = np.ones(4).reshape(-1),
        args = (X, y),
        method = 'Nelder-Mead'
    )
    Beta_hat = opt_values.x

    return Beta_hat


# In[49]:


def mle(Beta: np.array, X: np.array, y: np.array) -> np.array:

    X = np.c_[np.ones(X.shape[0]).reshape(-1,1), X]
    
    e = y - (X @ Beta)
    prob_e = (np.exp((-e**2)/2))/(np.sqrt(2*(np.pi)))
    sum_prob_e = np.sum(np.log(prob_e))
    
    return -sum_prob_e


# In[46]:


import numpy as np
import scipy as sp

def estimate_ols(y: np.array, X: np.array) -> np.array:

    opt_values = sp.optimize.minimize(
        fun = sse,
        x0 = np.ones(4).reshape(-1),
        args = (X, y),
        method = 'Nelder-Mead'
    )
    Beta_hat = opt_values.x

    return Beta_hat


# In[47]:


def sse(Beta: np.array, X: np.array, y: np.array) -> np.array:
    
    X = np.c_[np.ones(X.shape[0]).reshape(-1,1), X]
    
    e = y - (X @ Beta)
    e_sums = np.sum(np.square(e))
    
    return e_sums


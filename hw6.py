#!/usr/bin/env python
# coding: utf-8

# In[109]:


def github() -> str:
    """
    Some docstrings.
    """

    return "https://github.com/Zesy08/ECON481/blob/main/hw6.py"


# In[110]:


def std() -> str:
    """
    Some docstrings.
    """

    q = """
    select itemid,
    sqrt(sum((bidamount - avg_bid) * (bidamount - avg_bid)) / (count(*) - 1)) as std
    from (select itemid,
        bidamount,
        avg(bidamount) over (partition by itemid) as avg_bid
        from bids)
    group by itemid
    having count(*) > 1
    """

    return q


# In[111]:


def bidder_spend_frac() -> str:
    """
    Some docstrings.
    """
    q = """
       select b.biddername
    , b.total_bids as total_bids
    , case when s.total_spend is null then 0 else s.total_spend end as total_spend
    , case when s.total_spend is null then 0 else s.total_spend end / b.total_bids as spend_frac
    from (
        select biddername
        , sum(maxbid) as total_bids
        from (
            select biddername
            , itemid
            , max(bidamount) as maxbid
            from bids
            group by biddername, itemid
            )
        group by biddername) as b
    left join
        (
        select biddername
        , sum(maxbid) as total_spend
        from (
            select biddername
            , max(bidamount) as maxbid
            from bids
            group by itemid
        )
        group by biddername) as s
    on b.biddername = s.biddername
    """

    return q


# In[112]:


def min_increment_freq() -> str:
    """
    Some docstrings.
    """

    q = """
    with ranked_bids as (
        select b.itemid
            , b.bidderName
            , b.bidamount
            , i.bidIncrement
            , row_number() over (partition by b.itemid order by b.bidamount) as rn
        from bids b
        join items i on b.itemid = i.itemid
        where i.isBuyNowUsed = 0
        ),
        prev_bids AS (
            SELECT rb.itemid
                , rb.bidderName
                , rb.bidamount
                , rb.bidIncrement
                , rb.rn
                , lag(rb.bidamount) over (partition by rb.itemid order by rb.rn) as prev_bid
            from ranked_bids rb
        ),
        increment_bids AS (
            SELECT itemid
                , bidderName
                , bidamount
                , bidIncrement
                , prev_bid
            from prev_bids
            where prev_bid is not null and bidamount = prev_bid + bidIncrement
        )
        select count(*) * 1.0 / (
                                select count(*) 
                                from bids b 
                                join items i on b.itemid = i.itemid where i.isBuyNowUsed = 0
                                ) as freq
        from increment_bids
    """
    
    return q


# In[113]:


def win_perc_by_timestamp() -> str:
    """
    Some docstrings.
    """
    q = """
    select time_norm as timestamp_bin
    , avg(iswinbid) as win_perc
    from (
        with a as (
            select itemid, starttime, endtime, 
            julianday(endtime) - julianday(starttime) as length
            from items
        )
        select b.itemid, b.bidtime, a.starttime, a.endtime,
        cast(((julianday(endtime)-julianday(bidtime)) / a.length)*10+1 as integar) as time_norm
        , b.bidamount == max(bidamount) over (partition by b.itemid) as iswinbid
        from bids as b
        inner join a
        on b.itemid=a.itemid
        )
    group by timestamp_bin
    """

    return q


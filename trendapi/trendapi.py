# To use Google Trend API remove """ from labels

import pandas as pd
import matplotlib.pyplot as plt                 
from pytrends.request import TrendReq

pytrend = TrendReq()

# Interest by Region
""" 
pytrend.build_payload(kw_list=[‘Taylor Swift’])
df = pytrend.interest_by_region()
df.head(10)
"""
# Get Google Hot Trends data
"""
df = pytrend.trending_searches(pn='brazil')
df.head(20) 
"""

# Related Queries, returns a dictionary of dataframes (For Influencers)
""" 
pytrend.build_payload(kw_list=['Como fazer'])
related_queries = pytrend.related_queries()
related_queries.values() 
"""

# Related Topics, returns a dictionary of dataframes
""" 
pytrend.build_payload(kw_list=['slime'])
related_topic = pytrend.related_topics()
related_topic.values()
 """
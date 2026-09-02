import pandas as pd
import numpy as np

sports = {
    'bask':'BasketBall',
    'hand':'HandBall',
    'snow':'Snowsport',
    'base':'BaseBall',
    'swim':'Swimming'
}

sIndex = pd.Series(sports)

print(sIndex.iloc[1])
print(sIndex.loc['swim'])

print(sIndex.str.upper())

#@title
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import preprocessing

df = pd.read_csv('http://storm.cis.fordham.edu/~yli/data/adultAll.csv')

df.info()

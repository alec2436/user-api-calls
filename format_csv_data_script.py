import numpy as np
import pandas as pd


csvfilename = 'alec_user_permissions.csv'

df = pd.read_csv(csvfilename, sep=',', header=None)

B_numpy = df.values
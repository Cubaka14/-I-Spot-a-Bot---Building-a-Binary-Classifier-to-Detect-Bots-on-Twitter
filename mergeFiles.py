import numpy as np
import pandas as pd
dfs = []

dfs.append(pd.read_csv(r"cresci2015Preprocessed.csv"))
dfs.append(pd.read_csv(r"cresci2017Preprocessed.csv"))

mergedResult = pd.concat(dfs, sort=True)

writer = pd.ExcelWriter('cresciFullPreProcessed.xlsx', engine='xlsxwriter')
mergedResult.to_excel(writer, sheet_name='Sheet1')
writer.save()


mergedResult.to_csv("cresciFullPreProcessed.csv")

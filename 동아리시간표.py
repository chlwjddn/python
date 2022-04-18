import pandas as pd

col = ["a","b","c"]
ind = [1,2,3]
con = [[0,0,0],[0,0,0],[0,0,0]]

pd.DataFrame(con, colums= col, index= ind)

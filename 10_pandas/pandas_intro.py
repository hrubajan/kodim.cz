import pandas

mesta = pandas.read_csv("08_lekce/mesta.csv", encoding='utf-8', index_col='mesto')

print(mesta)

mensi = mesta.loc[["litvinov","olomouc","praha"],"obyvatel":"vymera"]

print(mensi)

# vse v jupyteru
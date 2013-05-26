import pandas
df = pandas.DataFrame()
df = df.load( 'wholetable.df')


#find the conflicts
conflictedDataFrame = df[ (df.Is_bad == 1) & (df.Is_cover == 1) ] 


#add a column called source to the table
df.insert( 2, 'source', None )
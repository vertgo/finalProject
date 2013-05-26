def getSource( inURL ):
	if "fbcdn" in inURL:
		return "facebook"


#assuming df is the dataframe
df[ 'source' ] = map( getSource,  df[ 'Image_url' ] )
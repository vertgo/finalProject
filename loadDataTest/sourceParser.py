def getSource( inURL ):
	if "fbcdn" in inURL:
		return "facebook"


	elif "tripadvisor.com" in inURL:
		return "tripadvisor"

	elif "flickr.com" in inURL:
		return "flickr"

	elif "yelp.com" in inURL:
		return "yelp"
	elif "yelpcdn.com" in inURL:
		return "yelp"

	elif "tumblr" in inURL:
		return "tumblr"

	elif "4sqi.net" in inURL:
		return "4square"

	elif "nytimes.com" in inURL:
		return "nytimes"

	elif "wp-content" in inURL:
		return "blog"
	elif "blogspot" in inURL:
		return "blog"	
	elif "wp-content" in inURL:
		return "blog"
	elif "wordpress.com" in inURL:
		return "blog"


#assuming df is the dataframe
#df[ 'source' ] = map( getSource,  df[ 'Image_url' ] )
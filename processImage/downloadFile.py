import urllib2
import pandas
import pycurl
import numpy
from threading import Thread
import os.path


def downloadRange( inDF, inRange ):
	print ("downloading"+ str( inRange[0] )+"," + str(inRange[-1]) )

	for i in inRange:
		
		try:
			filename = "images/" +inDF.loc[i, 'Image_filename']
			#if it is a file, check the file size
			if os.path.isfile( filename ): 
				statinfo = os.stat(filename)
				if ( statinfo.st_size == 0): #if the size is 0, then download it
					print "downloading: " + str(i)
					downloadFile("http://s3.amazonaws.com/HoppitImagesTest/PlaceImages/" + inDF.loc[i, 'Image_filename'], filename )
				else:
					print "skipping: " + str(i)
			#if ( os.path.isfile( filename) :
			#	print "downloading: " + str(i)
			#	downloadFile("http://s3.amazonaws.com/HoppitImagesTest/PlaceImages/" + inDF.loc[i, 'Image_filename'], filename )
			else: #if it's not a file download it
				print "downloading: " + str(i)
				downloadFile("http://s3.amazonaws.com/HoppitImagesTest/PlaceImages/" + inDF.loc[i, 'Image_filename'], filename )
				
			
		#else:
		#	downloadFile("http://s3.amazonaws.com/HoppitImagesTest/PlaceImages/" + inDF.loc[i, 'Image_filename'], filename )
		
		except:
			print "error with: " + str( i )

			

			
def downloadFile( inURL, inFilePath ):
	print "downloading:" + inFilePath 
	fp = open( inFilePath  , "wb" )
	pc = pycurl.Curl()
	pc.setopt( pc.URL,  inURL)
	pc.setopt(pycurl.WRITEDATA, fp)
	pc.setopt(pc.FAILONERROR, False)
	pc.perform()
	fp.close()


def runmain():
	NUM_THREADS = 20;
	df = pandas.DataFrame()
	df = df.load( '../../loadDataTest/wholetable.df' )
	numRows = df.count()[0]
	for i in range(NUM_THREADS):
		curRange = range( i, numRows + i)
		strideRange = curRange[ :: NUM_THREADS ]
		t = Thread(target=downloadRange, args=( df, strideRange ) )
		t.start()

if __name__ == '__main__':
	runmain()
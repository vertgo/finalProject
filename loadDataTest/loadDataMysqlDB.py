import pandas.io.sql as psql


import MySQLdb
mysql_cn= MySQLdb.connect(host='hoppitdbprodro.cfbipmelwom2.us-east-1.rds.amazonaws.com', 
                port=3306,user='hoppituser', passwd='hopp1t', 
                db='hoppit')
df_mysql = psql.frame_query("SELECT * FROM hs_place_images LIMIT 10", con=mysql_cn)    
print 'loaded dataframe from MySQL. records:', len(df_mysql)
mysql_cn.close()
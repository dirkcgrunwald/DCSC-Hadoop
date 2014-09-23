##
## Shove the patent data into HDFS
##
## Use use .hdfs files to indicate if the corresponding
## file is in HDFS
##

to_hdfs: patents.hdfs cite75_99.hdfs inventor.hdfs coname.hdfs match.hdfs pat63_99.hdfs
	@echo Done

patents.hdfs:	
	hdfs dfs -test -d patents || hdfs dfs -mkdir patents
	touch patents.hdfs

cite75_99.hdfs: patents.hdfs acite75_99.zip	
	-hdfs dfs -rm -r patents/cite
	-hdfs dfs -mkdir patents/cite
	zcat acite75_99.zip | hdfs dfs -put - patents/cite/cite75_99.txt
	touch cite75_99.hdfs

inventor.hdfs: patents.hdfs ainventor.zip
	-hdfs dfs -rm -r patents/inventor
	-hdfs dfs -mkdir patents/inventor
	zcat ainventor.zip | hdfs dfs -put - patents/inventor/inventor.txt
	touch inventor.hdfs

coname.hdfs: patents.hdfs aconame.zip
	-hdfs dfs -rm -r patents/coname
	-hdfs dfs -mkdir patents/coname
	zcat aconame.zip | hdfs dfs -put - patents/coname/coname.txt
	touch coname.hdfs

match.hdfs: patents.hdfs amatch.zip
	-hdfs dfs -rm -r patents/match
	-hdfs dfs -mkdir patents/match
	zcat amatch.zip | hdfs dfs -put - patents/match/match.txt
	touch match.hdfs

pat63_99.hdfs: patents.hdfs apat63_99.zip
	-hdfs dfs -rm -r patents/patents
	-hdfs dfs -mkdir patents/patents
	zcat apat63_99.zip | hdfs dfs -put - patents/patents/pat63_99.txt
	touch pat63_99.hdfs

clean:
	-rm *.hdfs

spotless: clean
	hdfs dfs -rm -r patents
 

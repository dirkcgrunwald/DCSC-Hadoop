##
## Shove the patent data into HDFS
##
## Use use .hdfs files to indicate if the corresponding
## file is in HDFS
##

to_hdfs: patents.hdfs cite75_99.hdfs inventor.hdfs coname.hdfs match.hdfs pat63_99.hdfs
	@echo Done

patents.hdfs:	
	! hadoop fs -test -d patents || hadoop fs -mkdir patents
	touch patents.hdfs

cite75_99.hdfs: patents.hdfs acite75_99.zip	
	-hadoop fs -rm -r patents/cite75_99.txt
	zcat acite75_99.zip | hadoop fs -put - patents/cite75_99.txt
	touch cite75_99.hdfs

inventor.hdfs: patents.hdfs ainventor.zip
	-hadoop fs -rm -r patents/inventor.txt
	zcat ainventor.zip | hadoop fs -put - patents/inventor.txt
	touch inventor.hdfs

coname.hdfs: patents.hdfs aconame.zip
	-hadoop fs -rm -r patents/coname.txt
	zcat aconame.zip | hadoop fs -put - patents/coname.txt
	touch coname.hdfs

match.hdfs: patents.hdfs amatch.zip
	-hadoop fs -rm -r patents/match.txt
	zcat amatch.zip | hadoop fs -put - patents/match.txt
	touch match.hdfs

pat63_99.hdfs: patents.hdfs apat63_99.zip
	-hadoop fs -rm -r patents/pat63_99.txt
	zcat apat63_99.zip | hadoop fs -put - patents/pat63_99.txt
	touch pat63_99.hdfs

 clean:
	-rm *.hdfs

spotless: clean
	hadoop fs -rm -r patents
 
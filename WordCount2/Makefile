HADOOP        = /usr/lib/hadoop
HADOOP_MR     = /usr/lib/hadoop-0.20-mapreduce/
HADOOP_HDFS   = /usr/lib/hadoop-hdfs
CLASSPATH=$(HADOOP)/hadoop-common.jar:$(HADOOP)/hadoop-auth.jar:$(HADOOP)/hadoop-annotations.jar:$(HADOOP_MR)/hadoop-core.jar:$(HADOOP_HDFS)/hadoop-hdfs.jar
JAR	= jar
JAVAC	= javac

WordCount2.jar: WordCount2.java
	-mkdir wordcount_classes
	javac -classpath $(CLASSPATH) WordCount2.java -d wordcount_classes
	$(JAR) -cvf WordCount2.jar -C wordcount_classes/ .

run:	WordCount2.jar	
	-hadoop fs -rm -r sou	
	hadoop fs -mkdir sou
	hadoop fs -put 2002-sou.txt sou
	-hadoop fs -rm -r output
	hadoop jar ./WordCount2.jar org.myorg.WordCount2 sou output

clean::	
	-rm WordCount2.jar
	-rm -rf wordcount_classes
	-hadoop fs -rm -r output
HADOOP        = /usr/lib/hadoop
HADOOP_MR     = /usr/lib/hadoop-0.20-mapreduce/
HADOOP_HDFS   = /usr/lib/hadoop-hdfs
CLASSPATH=$(HADOOP)/hadoop-common.jar:$(HADOOP)/hadoop-auth.jar:$(HADOOP)/hadoop-annotations.jar:$(HADOOP_MR)/hadoop-core.jar:$(HADOOP_HDFS)/hadoop-hdfs.jar

STREAMING	=$(HADOOP_MR)/contrib/streaming/hadoop-streaming-*.jar

run-mapper:	
	-hadoop fs -rm -r output
	hadoop jar $(STREAMING) \
	  -D mapred.reduce.tasks=0 \
	  -input patents/pat63_99.txt -output output \
	  -file AverageByAttributeMapper.py \
	  -mapper AverageByAttributeMapper.py
	-rm -rf output
	hadoop fs -get output .

run-mapreduce:	
	-hadoop fs -rm -r output
	hadoop jar $(STREAMING) \
	  -input patents/pat63_99.txt -output output \
	  -file AverageByAttributeMapper.py \
	  -mapper AverageByAttributeMapper.py \
	  -file AverageByAttributeReducer.py \
	  -reducer AverageByAttributeReducer.py
	-rm -rf output
	hadoop fs -get output .


clean::	
	-rm -rf output
	-hadoop fs -rm -r output
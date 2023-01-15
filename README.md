# Big_Data_Yet_Another_Kafka

BD2_044_056_110_123
Repo created programmatically. Project Title: Yet another Kafka (YaK)

YaK or Yet Another Kafka is one of the projects that can be chosen as part of the BigData Course (UE20CS322) at PES University.
It involves setting up a mini-Kafka on a student's system, complete with a Producer,Subscriber and a Publish-Subscribe architecture.
Our project calls for using the MQTT protocol architecture as a base and utilizes socket programming to do communication using Transport Layer Protocol.

![mqtt](https://user-images.githubusercontent.com/79096803/212528603-1a668b81-9b92-44c7-9e50-d9c6471def6b.png)



With multiple publisher-subscriber established along with multi-threading, each thread is adjacent to a topic that is published, capacity to hold multiple messages. 
The subscriber can eventually view the messages subscribed to. The broker is responsible for managing topics.
3 kafka brokers have been created. Zookeeper plays the part of a kafka health check here and displays the number of active threads running in session.

Steps to execuete:

Download zip folder or git-clone the repository.
Run the broker.py file.
Follow it with the publisher.py where in the topics need to be created with their respective messages.
The subscriber.py file is then run, to subscriber to a topic of choice.
The zookeeper.py follows suite displaying the status.

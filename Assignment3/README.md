# Assignment 3: ZooKeeper Register/Lookup in Publish-Subscribe using ZMQ and Mininet

### Team members

 - Zhuangwei Kang
 - Manyao Peng
 - Minhui Zhou
 - Yingqi Li
 
### Environment
  - Ubuntu 16.04
  - Python
  - Pyzmq
  - Mininet
  - Kazoo
  
### File Description (/SourceCode/):
  - Broker.py : Broker class that defines  Broker's behavior
  - Publisher.py : Publisher class that defines Publishers' behavior
  - Subscriber.py : Subscriber class that defines Subscribers' behavior
  - BrokerT.py : Broker test file
  - mPublisherT.py : Publisher test file using mininet
  - mSubscriberT.py : Subscriber test file using mininet
  - ZMQHelper.py : Custom API that encapsulates Pyzmq API
  - mininet.py : Entrance file for system test using mininet
  - BusTopology.py : Used to build up bus topology
  - StarTopology.py : Used to build up star topology
  - TreeTopology.py : Used to build up tree topology
  
### Main Logic
  - The whole system has 3 brokers, n publishers, n subscribers, 1 zookeeper server, all of which are mininet host.
  - In ZooKeeper server, there are permanent nodes like Brokers, Publishers and Subscribers and ephemeral node like Leader.
  Brokers contain three ephemeral znodes Broker1, Broker2 and Broker3. Publishers contain ephemeral znodes, n concrete  publishers. Subscribers contain ephemeral znodes, n concrete subscribers.
  - Broker: 
    - Connect to ZooKeeper and create Broker znodes.
    - Watch Publishers.
    - Watch Leaders. In the initial state, the first broker of the system creates leader, build leader znode. Every broker should watch leader. Leader znode stores the IP of broker leader. When the second broker wants to join into the system and create znode, it will find the leader znode has already exists, so the second broker becomes the follower automatically.
    - After receiving the message, the broker synchronizes the message to the follower and sends message to the subscriber.
  
  - Publishers:
    - Every publisher watches leader znode and Publishers only send messages to leader according to IP address stored in Leader znode.
    - When one publisher dies, the corresponding ephemeral znode disappears. Leader watches that the number of children of publishers changes and checks in the storage that the corresponding publisher disappears, so it deletes all contents about the died publisher.
    
  - Subscribers:
    - Subsribers are similar to Publishers, every subscriber watches leader znode.
    - There is one difference that subscribers deal with not only new sent publication but also history publication.
    
  - Leader: If Broker1 is leader, now it died. Because both Broker2 and Broker3 watch leader, a leader election begins. Publishers stop sending messages until a new leader appears. Similarly, Subscribers stop receiving messages until a new leader appears. Because the leader IP changes, every publisher should reconnect to the new leader.
  
#### Test Methods:
  - Atomatically test using Mininet
  
#### Topology Type:
  - Bus Topology
  - Star Topology
  - Tree Topology 
  
#### Atomatically Test using Mininet
  

 
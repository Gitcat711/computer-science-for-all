## Typical Questions and Answers.

#### 1. What are TCP and UDP?
Both __TCP__ and __UDP__ are protocols that deals with sending chunk of __data__(packets) over a network. Used together with IP(which deals with the "_where_"), these protocols define _how_ the data is sent.  

**Tranfer Control Protocol(TCP)**
  - is _connection oriented_, i.e. once a connection is established, data can be sent from both parties. It is the most widely used protocol over the internet mostly due to its _reliability_. Its purpose is to ensure the all the *packets* are recieved as uncorrupted files.
  - For two devices to communicate, a `TCP` connection must be established. This connection enables sending data in ordered chunks(packets). If some packets are lost along the way, the device _recieving_ data can ask for them again.
  - After both computers are aware that the transfer is over(there are no packets remaining/missing), the connection is _dropped_. As a consequence the, `TCP` trasnfer is slower, but error correction is ensured.
  - Common protocols that works on top of `TCP` are: **HTTP, HTTPS, FTM, SMTP, Telnet**.

  **User Datagram Protocol(UDP)**
   - is a simpler, connectionless Internet Protocol where multiple messages are sent as packets in chunks using`UDP`.
   - It was designed for **fast data transmission**.
   - When datagrams(packets) are released into the network there is no way of telling whether they reach their destination. Data can arrive out of order, duplicated or none at all.
   -  The simplicity of `UDP` reduces the overhead of other protocols and can be adequate for some applications such as real-time media streams or broadcasts.
   - Protocols such as **DHCP** and **VOIP** work on top of `UDP`
----------
#### 2. What is Latency and Ping?

- **Latency** - also known as _lag_ or _delay_ is a metric that measures the amount of time it takes to transfer information from one point to the another. It is measured in _milliseconds(ms)_. In packet-switched networks the latency is measured either `one-way`(_direct trip from source to destination_) or `round-trip`(_trip from source to destination and forthback_).

- However, round trip delay time is more often quoted, being able to be measured from a single point. __RTT__ is time taken for a `packet` to be sent to a destination point and for the _acknowlegdement_ message to get back to the source.

- For calculating RTT, we use the `ping` command line utility, available
```cmd
ping google.com
PING google.com (x.x.x.x): 56 data bytes
64 bytes from 216.58.203.174: icmp_seq=0 ttl=56 time=6.484 ms
64 bytes from 216.58.203.174: icmp_seq=1 ttl=56 time=7.417 ms
64 bytes from 216.58.203.174: icmp_seq=2 ttl=56 time=32.127 ms
64 bytes from 216.58.203.174: icmp_seq=3 ttl=56 time=7.943 ms
64 bytes from 216.58.203.174: icmp_seq=4 ttl=56 time=8.443 ms
64 bytes from 216.58.203.174: icmp_seq=5 ttl=56 time=26.171 ms
64 bytes from 216.58.203.174: icmp_seq=6 ttl=56 time=7.706 ms
 ```

- You can see that the average time is around `55-56` ms. In majority of cases the `ping-rate` is equivalent to the `effective latency` between a device and a server, but factors such as throttling and congestion might affect the results. The terms are roughly synonymous and many games and applications reports the __*latency as ping rate*__.
---------
#### 3. What are important networking metrics?
- **Metrics** are used to verify desired behaviours of processes in quantitative and qualitative manner. In Computer Networks metrics can helps us identify underlying problems, enhance connections or even decide for the most suitable internet plans.  
- The effective performance of a network is defined by the combination of different metrics which may vary because each network is unique in its nature and design. However, there are some standard and relevant measurements applicable to any network:
    - **`bandwidth`** - maximum rate at which information can be tranferred.
    - **`throughput`** - actual rate at which information can be transferred.
    - **`jitter`** - time difference in packet inter-arrival time.(details in further question.)
    - **`error rate`** - number of corrupted bits.
- Another important metric is **`packet loss`**, measuring what percentage of packets is lost while transferring data over a network. (_this is not always applicable, as `TCP` was designed to solve this exact problem, guaranteeing `0` packet loss_)
> It is not mandatory to measure performance.Instead it can also be modelled and simulated. One such example is using state transition diagrams to model queuing performance using a **Network Simulator**

--------------

<<<<<<< HEAD
#### 4. What is a URL?
- **URLs**(_uniform resource locators_) are sequences of characters used to identify resources on the internet. They are specified in the header of the request.
```
http://www.google.com:80/path/res?q=x
|---| |-----------------||------||---|
protocol | host --------||path--||query|
```
  - The **Protocol**, usually `http` or `https`. This part dictates how the data pointed at by the whole url should be processed.
  - The **Host**, address contains a _subdomain(www)_, a _domain(google.com)_ and a _port number(80)_, usually hidden in a modern browsers.
  - the resource **path** represents the resource's location on the server.
  - a **query string**, beginning with `?`, that contains different `field=values&` pairs.(this is abstract definition, we will look into this with deeper dive.)

- A **URL** is not specific to the `HTTP` protocol, but it is a generic and standardised way of locating resources on a network.
- A _URL_ is subtype of **URI**(_Uniform Resource Identifier_), but accompanied by a "access mechanism" or "network locator"(`http://`).  **Note**: While all _URLs are URI_, **not** all URIs are URLs.

----------------------------
#### 5. What are Status Codes?
- Status codes are 3-digit integers, part of the server's response in HTTP protocol. With URLs and HTTP verbs (_get, post, delete, put, etc_), a client can make requests to the server, which sends back a response containing the _status_ of the request and a message _payload_.
- The _status code_ indicates whether the request has been successfully processed or not. The code are grouped into _five_ classes:
  - **Informational messages**(`1xx`): This class was introduced in `HTTP/1.1` and indicates that everything is OK so far and the client can continue with the request.
  - **Success messages**(`2xx`): These ones tell the client that the client that the request was acknowledged and successfully processed.
  - **Redirection messages**(`3xx`): These messages imply that further action must be taken to complete the request. Usually, they indicate that different URL must be used to access the resource.
  - **Client-error messages**(`4xx`): They are used to inform the client there was a problem with their request. The problem could be an invalid URL, missing field or wrongly formatted data.
  - **Server-error message**(`5xx`): They show that the server failed to process the request.
- Below is tabular representation of the _class & codes_.

|Class|Code|Text|Comments|
|-----|------|-----|------|
|_Success_|`200`|OK|All is well, valid request and response|
|_Redirection_|`301`|Moved Permamently|Page is now at new location, (_automatic redirect in most modern browsers)_|
|_Redirection_|`302`|Found|Page is now at new location Temporarily|
|_Client Error_|`401`|Unauthorized|Page Typically requires login credentials.|
|_Client Error_|`403`|Forbidden|Server will not allow this request.|
|_Client Error_|`404`|Not Found|Server cannot find what was asked for|
|_Server Error_|`500`|Internal Server Error|Generic server failure in responding to the otherwise-valid request

------------------
=======
 #### 4. What is difference between Bandwidth and throughput?
> Both *`bandwidth`* and *`throughput`* are metrics used to describe the performance of data transfer over a network segment(a link from point `A`to point `B`).

- **`bandwidth`** - refers to the maximum theoretic amount of data(number of packets) that can be sent on th channel,regardless of practical considerations.
- **`throughput`** - refers to the actual amount of data that travels through the segment successfully
- Lets exemplify it,
  - A _highway_ has the capacity of moving 300 cars at the same time, this is `bandwidth`. But most of the times due to jam or congestion, the actual number of cars that it can move is around 200, this is `throughput`.
  - This distinction is relevant as ISPs usually advertise their `bandwidth` which is often higher than the `throughput` you will receive.
- These metrics are computer over _single unit of time_, expressed as _bits/seconds(`bps`)_. Modersn networks are faster and therefore have their speed measured in millions of bits per second -> megabits/sec(`Mbps`) or in billions of bits/sec -> gigabits/sec(Gbps).   
-----------
#### 5. What is Jitter?
- Jitter is defined as the variation in the delay of received packets in computer networks. While we know that **Latency** is the time it takes to move a packet from point A to B, **Jitter** is the _change_ in that time.
- Jitter, referred as **Packet Delay Variation**(_though both are not completely synonymous , can be used interchangeably_), i an undesirable effect caused by inherent tendencies of **TCP/IP** networks. It is measured in milliseconds. 
- Explaining Jitter,
  - *_Ideal Case_* - A simple network between two computers, `A` & `B`. `A` sends a packet to `B` in `20ms` and B sends a response to `A` in `20ms`. This indicates flow of data to be continous and the neither of the machine experience _jitter_.
  - *_Practical_* - Supposdely A sends packets every 20ms,yet the roter between A and B is busy handling some other intnsive tasks on the nwtworks. Thus computer B won't receive the packets constantly or evenly, i.e instead of every 20ms, the machine B receives packets with delay(i.e. every 40ms or 60ms). This phenomenon is called Jitter.
 - There's heavy chance we all have faced the _Jitter_. Remember those lag spikes when playing online video games, where our player teleports across tht map. And that pauses we face while bufferring Youtube videos.
 - Congestion, improper queuing, configuration errors are some of the reasons of Jitter in TCP/IP networks.
>>>>>>> f78a3e2b48d13876a4f1e9967147a3e32ca9fcdc

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
- The effective performance of a network is defined by the combination of different metrics which may vary because wach network is unique in its nature and design. However, there are some standard and relevant measurements applicable to any network:
    - **`bandwidth`** - maximum rate at which information can be tranferred.

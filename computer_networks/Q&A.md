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

## Gist of Everyday Networking Terms.

#### Introduction
Its essential to understand networking, especially who manages the servers. Apart from getting your services online and smooth functioning of the applications, it also helps us to figure out the issues and diagnose various problems that comes with them.

#### The Most Basic Terms.
> There are many other terms that we may come across, and this list cannot be more exhaustive, so we are diving into some basic terms, high-level concepts. Various terms can be explained in-place, while more exhaustive discussion over the same.

- **Connection** - In Networking, a connection refers to pieces of related information that are transferred through a network. This is generally infers that a connection is built prior to data transfer(_by following certain procedures laid out in protocol_) and then is deconstructed at the the end of the data transfer.
- **Packets** - A packet, is the most basic unit that is transfered over a network. When communicating over a network, packets are the envelopes that carry your data(in bits, bytes, pieces)from one end point to the other.

  > Packets have a header portion that contains information about the packet including the source and destination, timestamps, network hops, etc. The main portion of a packet contains the actual data being transferred. It sometimes called the body or the payload.

- **Network Interface** - A network interface can refer to any kind of software interface to networking hardware. Fo instance, if you have two network cards in your computer, you can control and configure each network interface assoicated with them individually.
  > A network interface may be associated with a physical device, or it may be a representation of a virtual interface. The "loopback" device, which is a virtual interface to the local machine, is example of this.

- **LAN**  - LAN stands for _Local Area Network_. It refers to a network that is not publicly accessible to the greater internet. A home or office plays a perfect example of what lan is.

- **WAN** - WAN stands for_Wide Area Network_, a more extensive network than LAN. While WAN is relevant term to describe large, dispersed networks in general, it is usually meant to define Internet, as a whole.
  > If an interface is said to be connected in WAN, it is generally assumed that it is reachable through internet.

- **Protocol** - A Protocol is a set of rules and standards that basically define a language that devices can use to communicate between them. There are number of protocols that are extensively used in networking, and they are often implemented  in different layers.

  > Some low-level protocols are TCP, UDP, IP and ICMP. Some familiar examples of application layer protocols, built on top of these lower level protocols, are HTTP(for the web access), SSH, TLS/SSL, and FTP.

- **Port**  - A port is an address on a single machine that can be tied to a specific piece of software. It is not a physical interface or location, but it allows your server to be able to communicate using more than one application.

- **Firewall**  - A firewall is a program that decides whether traffic coming into a specific server or going out should be allowed. A firewall usually works for creating rules for which type of traffic is acceptable(kinda works ike a filter) on which ports. Generally, firewall blocks ports that are not used by a specific application on a server.

- **NAT** - NAT stands for _network address translation_. An easy way to translate incoming requests into a a routing server to the relevant devices or servers that it knows about in the LAN. This is usually implemented in physical LANs as a way to route requests though one IP address to the necessary backend servers.

- **VPN** - Virtual Private Network, means connecting separate LANs through the internet, while maintaining privacy. This is used as a means of connecting remote systems as if they were on a local network, often for security reasons.

**********************

#### Network Layers
1.  The topological order for discussing the networking is often in horizontal way. But, between various hosts, it's implementation is layered in a vertical fashion throughout a computer or network.

2. This means that there are multiple technologies and protocols that are built on top of each other in a order of communication to function with ease. In a successive layers, the abstraction levels of raw data is little bit more, which in returns makes it more simpler for users and applications.
3. This kind of modelling allows us to leverage lower layer in new ways without investing the time and energy to develop the protocols and applications that handles those type of traffics.

4. As a data is sent out of one machine, it begins at the top of the stack and filters downwards. At the lowest level, actual transmission to another machine takes place, and now the data travels back up through the layers of the other computer.
5. Each layer has the ability to add its own _"wrapper"_ around the data that it receives from the adjacent layer, which will help the layers that come after it decide what to do with the data when it's received.

  #### OSI Model(Open Systems Interconnect)
    > Its one of the method of talking about the different layers of network communication is the OSI model, Open Systems Interconnect. This model defines seven separate layers.

    - **`Application`** - The application layer is the layer that the users and user-applications most often interact with. Network communication is discussed in terms of availability of resources, partners to communicate with, and data synchronisation.

    - **`Presentation`** - The Presentation layer is responsible for mapping resources and creating context. It is used to translate lower level of networking data into data that application expect us to see.

    - **`Session`**  - The session layer is a connection handler. It creates, maintains, and destroys connections  between nodes in a persistent way.

    - **`Transport`**  - The transport layer is responsible for handling the layers above it a reliable connection. In this context, reliable refers to the ability to verify that a piece of data was received intact at the other end of the connection.(_This layer_ can resend the information that has been dropped or corrupted and can acknowledge the receipt of data to remote computers.)

    - **`Network`** - The network layer is used to route data between different nodes on the network. It uses addresses to be able to tell which computer to send information to. This layer can also break data/larger messages into smaller chunks, which are reassembled on the opposite end.

    - **`Data Link`** - This layer is implemented as a method of establishing and maintaining reliable links bwtween different nodes or devices on a network using existing physical connections.

    - **`Physical`** - The physical layer is responsible for handling the actual physical devices that are used to make a connection. This layer involves the bare software that manages physical connections as well as the hardware itself(like Ethernet).

  #### TCP/IP model
  > The most commonly known as Internet Protocol suite, is another layering model that is simpler and has been widely adopted. It defines the four separate layers, some of which share similarity with OSI model. You can observe that this model is bit more abstract and fluid. Thus results in easier implementation it it dominant way of categorising  the networking.

   - **`Application`** - In this model, the application layer is responsible for creating and transmitting user data between applications. The applications can be on a remote systems, and should appear to operate as if locally to the end user.  

   - **`Transport`** - The transport layer is responsible for communication between processes. This level of networking utilizes ports to address different services. It can build up unreliable or reliable connections depending on the type of protocol used.   

   - **`Internet`** - The internet layer is used to transport data from node in a network. This layer is aware of the endpoints of the connections, but doesn't worry about actual connection needed to get from one place to another. IP addresses are defined in this layer as a way of reaching remote systems in an addressable manner.

   - **`Link`** - The link layer implements the actual topology of th local network that allows the internet layer to present an addressable interface. It establishes connections between neighbouring nodes to send data.

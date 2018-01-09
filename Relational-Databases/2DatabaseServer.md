### What is a Database Server?

- A Database Server can mean two different things. First, it can be a computer program that provides database services as specified by _client-server model_., or it can be the host (hardware part of a database).

- A Database server, while used as the _hardware_ part of database, is a computer dedicated to perform database storage and retrieval.This computer runs the database software application(DBMS - database management systems). The hardware is the location that the host for the database on the network is poiting too.

- When referring to the software, we are talking about the program that receives and interprets requests. These requests are called __Queries__ which are request to store, retrieve, or change data in the database. Database Servers can:
  - Read Data,
  - Store Data, 
  - Analyze data,
  - Validate data against a Schema.
  
 - In small _application_ development, or some simple side-projects, the application and the database will be hosted on the same computer, meaning they won't need to communicate over a network. 
 - In _medium-scale_ applications, such as intranet or low-volume website, will most likely be hosted in a dedicated server while the database will be on a seperate dedicated server. The application would then connect to the database via _Uniform Resource Locator(URL)_
 - In high-scale applications, the volume of the data transactions can be so big that one single computer wouldn't be able to handle the work. In such case, the software application may be running on the hundreds of servers, and the database server will need to become a Custer of Server servers, with one server doing the coordination, and the other hosting portions of the database.
 
 - A group of database servers(called as _Cluster_)can coordinate to share data across multiple physical pieces of hardware. This is used for very large databases, or for redundancy. For this reason, Database Server mostly refers to the software, rather than the hardware.

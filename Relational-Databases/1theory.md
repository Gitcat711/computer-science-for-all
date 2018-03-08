# Introduction to Databases.

### What is Database Management System(DBMS)?
  - **Massive** - DBMS are handling terabytes of data today. So one of the critical aspects is that _data_ handled by DBMS is much larger than it can typically fit in normal computing systems. So they are designed to handle large amount of Data.
  - **Persistent** - Indicates that the data in the database management system outlives the program that executes on that data. Very often there will be multiple programs operating on same data.
  - **Safe** - It signifies that the data shouldn't be lost or overwritten when there can be failures(hardware, software, power-outage, corruption due to user). Number of built-in mechanism that ensures it safety & consistency.
  - **Multi-User** - Program may allow many different applications and users to access the data concurrently.There is a mechanism in DBMS called _Concurrency Control_. It's more centred around the _data_ in DB rather _Database_ itself.
  - **Convenient** - It is necessary to ensure that we should be able to do very powerful and interesting processing on that data. There is a notion in databases called _Physical data Independence_.(data is independent of the way programs think about the structure of the data). This is where high-level query languages comes into the picture. They are more of _Declarative_
  -  **Efficient** - Performance is based on efficiency. So it is essential to execute thousands of complex queries per second, we need the DBMS to be Efficient.
  - **Reliability** - 99.99999999% uptime. Doesn't need more info why its important.

### Concepts
 - **Data Model** - Set or Records(Relational), XML, Graph Data Model. Data model tells you about the general form of data that's going to be stored in a Database.
 - **Schema v/s Data*** - _Schema_ sets up the structure of the database. Whereas the data is the actual data stored in the Schema. Typically data may change over time, but schema has it's existence from the time it is created in a pretty same way.
 - **Data Definition Language(DDL)** - To set up the Schema, we normally use what's known as DDL. It is used to set up a schema or structure for a particular database.
 - **Data Manipulation or Query Language** - After schema is set and initial data is loaded, then it is possible to start querying and modifying the data and that's typically done with DML.

### People Involved
1. **DBMS Implementer** - Builds whole DBMS systems and implements it.
2. **Database Designer** - Establishes the Schema. Works on how to Structure the data before we build an Application. The works gets very difficult with the complexity of the application.
3. **Database Application Developer** - Building a programs or applications that runs on database, often interfacing between the eventual user and the data itself. These programs are the ones that operates on the databases, created by the developer.
4. **Database Administrator** - Loads the data, sorts of gets the whole things running and pretty much smoothly. Important job when it comes to handle the database with huge amount of data. Highly valued, highly paid.

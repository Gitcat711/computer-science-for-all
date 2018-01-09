### What are Connection Strings?

_Connection strings_ are URLS taht points at a database, hosted on a server. They use the Uniform Resource Indicator(URI) standard ti structure the different parts. Abstractly , they are repreented like this:
  ```
  dbprotocol://username:password
  @hostname: port./dbname
  %%delim%protery=value
  ```
  
  - **`dbprotocol`** will be different for each database type:
    - Postgres -> `postgres` & `pg`
    - MySQL -> `mysql`
    - Microsoft SQL servers -> `jdbc:sqlserver`
    
  - **`username:pasword`** is standard way if specifying authentication. For some databases(namely SQL Servers), the user and password are entered at the end, the `property=value` section.
  
  - **`hostname`** is the address of the servers the database is located on. If the database you are connecting to is your own computer, this value is `localhost` or `0.0.0.0`. If it is _remote_, you will name enter a hostname like `aws-us-east-1-portal29.dblayer.com`
  - **`ports`** is how you know which port to connect to. The default default ports between database servers. 
  -**`delim`** denotes a delimiter. Some databases read from the querystring `?property=value&property=value`,some use semicolon,`/cricket;property=value;property=value`. These properties and values are used to send extra information to the database. 

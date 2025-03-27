import random

def dbms():
    global question1,select,d1,d2,d3,d4
    question1 = [
        "Which of the following is a primary key property?",
        "Which normal form removes partial dependency?",
        "What is the purpose of an index in a database?",
        "Which SQL command is used to remove a table from a database?",
        "What is the full form of ACID in databases?",
        "Which of the following is not a type of database model?",
        "Which of the following ensures the uniqueness of values in a column?",
        "Which command is used to remove all rows from a table without removing its structure?",
        "What is the role of the foreign key in a database?",
        "Which normal form deals with multivalued dependency?",
        "What is the main function of the 'HAVING' clause in SQL?",
        "Which type of join returns only matching rows from both tables?",
        "Which of the following is an advantage of using a relational database?",
        "What is the purpose of the 'GROUP BY' clause in SQL?",
        "Which of the following is a DCL (Data Control Language) command?",
        "What type of database is MongoDB?",
        "Which SQL function is used to find the number of rows in a table?",
        "What is the main function of a database transaction?",
        "Which of the following is true about a view in SQL?",
        "Which of the following commands is used to modify existing records in a table?",
        
    # Basic Level
    "What does DBMS stand for?",
    "Which of the following is a type of database?",
    "Which language is used to query a database?",
    "Which of the following is an example of a DBMS?",
    "Which of the following is NOT a characteristic of DBMS?",
    "Which component of DBMS handles user requests?",
    "Which key uniquely identifies a record in a table?",
    "Which SQL statement is used to retrieve data?",
    "Which of the following is NOT a DML command?",
    "Which command is used to remove all rows from a table?",

    # Intermediate Level
    "Which join returns only matching rows between tables?",
    "What is the purpose of an index in a database?",
    "Which statement is used to modify an existing table?",
    "Which of the following is an ACID property?",
    "What does the 'I' in ACID stand for?",
    "Which type of database model uses tables?",
    "Which SQL clause is used to filter records?",
    "Which of the following is NOT a normal form?",
    "Which normalization form eliminates transitive dependency?",
    "Which command is used to create a new database?",

    # Advanced Level
    "Which data structure is used for indexing in most DBMS?",
    "What is the purpose of a foreign key?",
    "Which SQL function is used to count the number of rows?",
    "What is a deadlock in DBMS?",
    "Which of the following is a non-clustered index?",
    "Which locking mechanism prevents dirty reads?",
    "What is a stored procedure?",
    "What is the difference between DELETE and TRUNCATE?",
    "Which of the following is an example of a NoSQL database?",
    "Which technique is used in distributed databases to maintain consistency?",

    # Transactions & Concurrency
    "What is the role of a transaction log?",
    "Which concurrency control technique ensures serializability?",
    "What does 'dirty read' mean in database transactions?",
    "Which of the following is a schedule that preserves consistency?",
    "Which isolation level provides the highest level of isolation?",
    "Which recovery method is used for transaction failures?",
    "What does the term 'phantom read' refer to?",
    "Which of the following is NOT a concurrency control mechanism?",
    "What is the purpose of checkpointing in DBMS?",
    "Which command is used to manually commit a transaction?",

    # Advanced SQL Queries
    "Which SQL clause is used for aggregation?",
    "What does the GROUP BY clause do?",
    "Which SQL function is used to find the highest value in a column?",
    "Which of the following allows combining results from multiple queries?",
    "What does the HAVING clause do in SQL?",
    "Which SQL keyword is used to remove duplicate records?",
    "Which command is used to create a view?",
    "Which SQL operation is used to retrieve unique values?",
    "What is the difference between UNION and UNION ALL?",
    "Which SQL statement is used to return records that do not match in both tables?",

    # Data Warehousing & NoSQL
    "Which of the following is a characteristic of a data warehouse?",
    "What is the primary use of OLAP in DBMS?",
    "Which NoSQL database type is best for storing key-value pairs?",
    "Which query language is used in MongoDB?",
    "Which of the following is a column-oriented NoSQL database?",
    "What does CAP theorem state about distributed databases?",
    "Which NoSQL model is best for hierarchical data?",
    "Which of the following is an example of an eventual consistency model?",
    "Which technology is used to process large-scale distributed data?",
    "What is the role of sharding in NoSQL databases?",

    # Database Security & Optimization
    "Which of the following is a database security measure?",
    "What is SQL injection?",
    "Which technique is used for query optimization?",
    "What is the purpose of database indexing?",
    "Which of the following is a database backup strategy?",
    "What is the role of a database administrator (DBA)?",
    "Which DBMS feature ensures high availability?",
    "What is the difference between a materialized view and a regular view?",
    "Which command is used to revoke privileges from a user?",
    "Which database storage technique minimizes redundancy?"


    ]

    options1 = [
        ["A) Uniqueness", "B) Redundancy", "C) Duplicates", "D) Volatility"],
        ["A) 1NF", "B) 2NF", "C) 3NF", "D) BCNF"],
        ["A) To store data", "B) To speed up searches", "C) To secure data", "D) To remove redundancy"],
        ["A) DELETE", "B) DROP", "C) REMOVE", "D) TRUNCATE"],
        ["A) Atomicity, Consistency, Isolation, Durability", "B) Availability, Consistency, Integrity, Durability", 
         "C) Accuracy, Consistency, Integrity, Database", "D) Atomicity, Concurrency, Integrity, Durability"],
        ["A) Hierarchical", "B) Relational", "C) Network", "D) Array-based"],
        ["A) Primary Key", "B) Index", "C) Foreign Key", "D) Trigger"],
        ["A) DELETE", "B) DROP", "C) TRUNCATE", "D) REMOVE"],
        ["A) Ensures uniqueness", "B) Establishes a link between tables", "C) Increases performance", "D) Stores metadata"],
        ["A) 1NF", "B) 2NF", "C) 3NF", "D) 4NF"],
        ["A) Filters grouped data", "B) Sorts query results", "C) Joins tables", "D) Inserts records"],
        ["A) INNER JOIN", "B) LEFT JOIN", "C) RIGHT JOIN", "D) FULL JOIN"],
        ["A) Increased security", "B) Data consistency", "C) Efficient data retrieval", "D) All of the above"],
        ["A) Filters records", "B) Groups records with similar values", "C) Sorts records", "D) Joins multiple tables"],
        ["A) SELECT", "B) DELETE", "C) GRANT", "D) UPDATE"],
        ["A) Relational", "B) NoSQL", "C) Hierarchical", "D) Network"],
        ["A) COUNT()", "B) SUM()", "C) AVG()", "D) MAX()"],
        ["A) To rollback changes", "B) To execute a single SQL query", "C) To execute a stored procedure", "D) To modify schemas"],
        ["A) A view stores data", "B) A view is a virtual table", "C) A view is a duplicate table", "D) A view is a backup of a table"],
        ["A) INSERT", "B) UPDATE", "C) ALTER", "D) CREATE"],
    ["Database Management System", "Data Backup Management System", "Distributed Base Management System", "Data Binding Management System"],
    ["Relational", "Hierarchical", "Network", "All of the above"],
    ["SQL", "HTML", "Python", "Java"],
    ["MySQL", "MS Word", "Google Chrome", "Linux"],
    ["Ensures data redundancy", "Supports multiple users", "Provides security features", "Handles large amounts of data efficiently"],
    ["Query Processor", "Storage Manager", "Transaction Manager", "Buffer Manager"],
    ["Primary Key", "Foreign Key", "Candidate Key", "Composite Key"],
    ["SELECT", "INSERT", "UPDATE", "DELETE"],
    ["SELECT", "UPDATE", "INSERT", "DROP"],
    ["DELETE", "DROP", "TRUNCATE", "REMOVE"],

    # Intermediate Level
    ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"],
    ["To improve query performance", "To store data permanently", "To delete duplicate data", "To manage foreign keys"],
    ["ALTER TABLE", "UPDATE TABLE", "MODIFY TABLE", "CHANGE TABLE"],
    ["Atomicity", "Aggregation", "Clustering", "Data Mining"],
    ["Isolation", "Integrity", "Information", "Indexing"],
    ["Relational", "Hierarchical", "Network", "Object-Oriented"],
    ["WHERE", "HAVING", "ORDER BY", "GROUP BY"],
    ["1NF", "2NF", "3NF", "6NF"],
    ["2NF", "3NF", "BCNF", "4NF"],
    ["CREATE DATABASE", "NEW DATABASE", "ADD DATABASE", "GENERATE DATABASE"],

    # Advanced Level
    ["B+ Tree", "Linked List", "Hash Table", "Stack"],
    ["To establish a relationship between tables", "To store unique values", "To act as a primary key", "To delete duplicate rows"],
    ["COUNT()", "SUM()", "AVG()", "MAX()"],
    ["A situation where two transactions are waiting for each other", "A situation where a transaction fails", "A situation where a database crashes", "A situation where data is corrupted"],
    ["A secondary index", "A clustered index", "A unique index", "A primary index"],
    ["Two-Phase Locking", "Read Committed", "Read Uncommitted", "Optimistic Concurrency Control"],
    ["A precompiled SQL statement", "A function that runs outside the database", "A type of index", "A type of transaction"],
    ["DELETE removes specific rows, while TRUNCATE removes all rows", "Both work the same way", "TRUNCATE is slower than DELETE", "DELETE cannot be rolled back"],
    ["MongoDB", "Oracle", "MySQL", "PostgreSQL"],
    ["Two-Phase Commit", "Write-Ahead Logging", "Checkpoints", "ACID Transactions"],

    # Transactions & Concurrency
    ["To keep track of all transactions", "To delete logs automatically", "To backup user data", "To store database schemas"],
    ["Two-Phase Locking", "Deadlock Prevention", "Indexing", "Normalization"],
    ["Reading uncommitted changes of another transaction", "Reading committed changes of another transaction", "A transaction waiting for another transaction", "A transaction failing due to an error"],
    ["Serializable Schedule", "Non-Serializable Schedule", "Uncommitted Schedule", "Dirty Schedule"],
    ["Serializable", "Read Committed", "Repeatable Read", "Read Uncommitted"],
    ["Undo Log", "Redo Log", "Checkpointing", "Shadow Paging"],
    ["When new records appear in between two reads of a query", "When the same record is read twice", "When a transaction fails", "When a deadlock occurs"],
    ["Timestamp Ordering", "Two-Phase Locking", "Indexing", "Deadlock Detection"],
    ["To store recovery information", "To store indexes", "To optimize queries", "To enhance transaction speed"],
    ["COMMIT", "SAVEPOINT", "ROLLBACK", "TRANSACTION"],

    # Advanced SQL Queries
    ["GROUP BY", "HAVING", "ORDER BY", "WHERE"],
    ["Groups rows that have the same values in specified columns", "Sorts rows in descending order", "Filters results based on conditions", "Joins multiple tables"],
    ["MAX()", "SUM()", "AVG()", "COUNT()"],
    ["UNION", "JOIN", "MERGE", "COMBINE"],
    ["Filters grouped results", "Sorts results", "Filters individual rows", "Merges multiple queries"],
    ["DISTINCT", "GROUP BY", "UNIQUE", "HAVING"],
    ["CREATE VIEW", "NEW VIEW", "GENERATE VIEW", "DEFINE VIEW"],
    ["DISTINCT", "UNIQUE", "FILTER", "GROUP BY"],
    ["UNION removes duplicates, UNION ALL keeps all records", "Both remove duplicate records", "UNION ALL removes duplicates", "UNION is faster"],
    ["EXCEPT", "INTERSECT", "MINUS", "DIFFERENCE"],

    # Data Warehousing & NoSQL
    ["Stores historical data for analysis", "Stores real-time transactional data", "Supports only structured data", "Requires constant updates"],
    ["Analyzing multidimensional data", "Performing transactional operations", "Optimizing storage", "Managing backups"],
    ["Key-Value Store", "Graph Database", "Relational Database", "Hierarchical Database"],
    ["Mongo Query Language (MQL)", "SQL", "NoSQL", "GraphQL"],
    ["Cassandra", "Redis", "MySQL", "Neo4j"],
    ["A distributed system can have at most two of consistency, availability, and partition tolerance", "A database can be fully consistent and highly available", "CAP theorem applies only to relational databases", "CAP theorem applies only to NoSQL databases"],
    ["Document Store", "Key-Value Store", "Graph Database", "Column-Family Store"],
    ["Cassandra", "MongoDB", "Oracle", "PostgreSQL"],
    ["Hadoop", "MySQL", "Oracle", "PostgreSQL"],
    ["Dividing data into smaller parts across multiple servers", "Combining multiple databases into one", "Replicating the same data across all nodes", "Encrypting data at rest"],

    # Database Security & Optimization
    ["User authentication", "Ignoring data backups", "Allowing unrestricted access", "Disabling encryption"],
    ["A method to inject malicious SQL queries", "A database encryption technique", "A technique for query optimization", "A method to increase indexing speed"],
    ["Indexing", "Partitioning", "Normalization", "All of the above"],
    ["To speed up data retrieval", "To remove duplicate records", "To compress data", "To enhance data security"],
    ["Full Backup", "Differential Backup", "Incremental Backup", "All of the above"],
    ["Ensuring database security and performance", "Developing application logic", "Maintaining user interfaces", "Managing network connectivity"],
    ["Replication", "Sharding", "Indexing", "Query Optimization"],
    ["Materialized views store actual data, regular views do not", "Regular views store data, materialized views do not", "Both are the same", "Materialized views take less space"],
    ["REVOKE", "DENY", "REMOVE", "DISABLE"],
    ["Normalization", "Denormalization", "Replication", "Partitioning"]


    ]

    # Select a random question
    select = random.randint(0, len(question1) - 1)

    # Shuffle options for randomness
    random.shuffle(options1[select])

    # Extract four options randomly
    d1, d2, d3, d4 = options1[select]
dbms()

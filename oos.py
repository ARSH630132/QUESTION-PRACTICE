import random

def o():
    global question1,select,d1,d2,d3,d4
    question1 = [
        "Which of the following is the core of an operating system?",
        "Which scheduling algorithm is used in time-sharing systems?",
        "What is the primary purpose of an operating system?",
        "Which of the following is not an operating system?",
        "Which of the following is a real-time operating system?",
        "What is thrashing in an operating system?",
        "Which scheduling algorithm may cause starvation?",
        "What is the purpose of virtual memory?",
        "Which of the following is an example of a deadlock prevention method?",
        "Which of the following is a disk scheduling algorithm?",
        "What is the function of a semaphore in process synchronization?",
        "Which of the following page replacement algorithms has the lowest page fault rate?",
        "Which of the following is not a type of kernel?",
        "Which inter-process communication method allows processes to communicate using messages?",
        "What is the main function of a device driver?",
        "Which of the following is a non-preemptive scheduling algorithm?",
        "What is a critical section in process synchronization?",
        "Which process state comes immediately after 'Ready' when the CPU is allocated?",
        "Which system call is used to create a new process in Unix?",
        "Which scheduling algorithm selects the process with the shortest execution time first?",
    # Basic Level Questions
    "What is an operating system?",
    "Which of the following is NOT an operating system?",
    "Which component of an OS interacts directly with hardware?",
    "What is the main function of an OS?",
    "What is the kernel?",
    "Which OS is open-source?",
    "What is a real-time operating system?",
    "What does a multi-user OS do?",
    "Which is NOT a function of an OS?",
    "What is a command-line interface?",

    # Process Management
    "What is a process?",
    "Which state is a process in when waiting for an I/O operation?",
    "What is the purpose of a process control block (PCB)?",
    "Which scheduling algorithm executes the shortest job first?",
    "Which of the following is a preemptive scheduling algorithm?",
    "What is a context switch?",
    "What is the purpose of a time quantum in round-robin scheduling?",
    "Which algorithm causes starvation for long processes?",
    "What is the role of the dispatcher?",
    "What is a zombie process?",

    # Threads & Concurrency
    "What is a thread?",
    "What is the difference between a process and a thread?",
    "Which type of threading is managed by the OS?",
    "What is multithreading?",
    "Which of the following is an advantage of multithreading?",
    "What is a race condition?",
    "What is a critical section?",
    "Which synchronization mechanism uses a binary variable?",
    "Which problem does Peterson’s solution address?",
    "What is the producer-consumer problem?",

    # Memory Management
    "What is main memory?",
    "Which memory management technique allows processes to be allocated non-contiguous memory?",
    "What is swapping in OS?",
    "What is fragmentation?",
    "Which algorithm selects the smallest free partition for a process?",
    "Which paging technique reduces page table size?",
    "What is demand paging?",
    "Which algorithm replaces the page that was least recently used?",
    "What is thrashing in an operating system?",
    "Which OS memory component stores page tables?",

    # File Systems
    "What is a file system?",
    "Which file allocation method uses linked blocks?",
    "What is an inode?",
    "Which file system does Windows primarily use?",
    "What is file fragmentation?",
    "What does the term 'mounting a file system' mean?",
    "Which file system structure maintains directory entries?",
    "Which technique speeds up file searches in a directory?",
    "What is an absolute path?",
    "Which file permission allows a user to execute a file?",

    # I/O Management
    "What is direct memory access (DMA)?",
    "Which I/O device uses a disk scheduling algorithm?",
    "Which disk scheduling algorithm gives the best average seek time?",
    "What is a spooler in an OS?",
    "What is an interrupt?",
    "Which of the following is a non-volatile storage device?",
    "What is RAID in storage?",
    "Which RAID level provides both mirroring and striping?",
    "What is seek time in disk scheduling?",
    "Which disk scheduling algorithm prevents starvation?",

    # Virtualization & Cloud Computing
    "What is virtualization in operating systems?",
    "Which technology is used to create virtual machines?",
    "What is a hypervisor?",
    "Which type of virtualization runs directly on hardware?",
    "What is cloud computing?",
    "Which cloud model provides complete software applications?",
    "Which cloud deployment model is used only by a single organization?",
    "What is containerization?",
    "Which tool is commonly used for containerization?",
    "Which cloud service model provides virtual machines?",

    # Security & Protection
    "What is an access control list (ACL)?",
    "Which OS feature prevents unauthorized access?",
    "What is a firewall?",
    "Which type of attack exploits buffer overflows?",
    "What is an antivirus program?",
    "What is authentication in security?",
    "Which method is commonly used for user authentication?",
    "Which OS feature restricts access to system resources?",
    "What is encryption?",
    "Which security technique scrambles data to prevent unauthorized access?",

    # Advanced Topics
    "What is a microkernel?",
    "Which OS follows a monolithic architecture?",
    "What is an embedded operating system?",
    "Which OS is best suited for real-time applications?",
    "What is a distributed operating system?",
    "Which scheduling algorithm is used in real-time systems?",
    "What is load balancing in distributed computing?",
    "Which OS is used in mobile devices?",
    "What is the main advantage of a 64-bit OS over a 32-bit OS?",
    "Which OS is commonly used for supercomputers?"

    ]

    options1 = [
        ["A) Shell", "B) Kernel", "C) CPU", "D) Compiler"],
        ["A) First Come First Serve (FCFS)", "B) Round Robin", "C) Shortest Job Next", "D) Priority Scheduling"],
        ["A) Manage hardware", "B) Execute programs", "C) Provide user interface", "D) All of the above"],
        ["A) Windows", "B) Linux", "C) Oracle", "D) MacOS"],
        ["A) Windows", "B) RTOS", "C) MacOS", "D) Unix"],
        ["A) Excessive swapping of pages", "B) CPU overload", "C) Deadlock", "D) High CPU utilization"],
        ["A) First Come First Serve (FCFS)", "B) Shortest Job Next (SJN)", "C) Round Robin (RR)", "D) Multilevel Queue"],
        ["A) Increases disk space", "B) Reduces RAM usage", "C) Extends RAM using secondary storage", "D) Increases CPU speed"],
        ["A) Banker's Algorithm", "B) Mutual Exclusion", "C) Circular Wait", "D) Hold and Wait"],
        ["A) FIFO", "B) SSTF", "C) SCAN", "D) All of the above"],
        ["A) Process termination", "B) Process synchronization", "C) CPU scheduling", "D) Memory allocation"],
        ["A) FIFO", "B) Optimal Page Replacement", "C) LRU", "D) MRU"],
        ["A) Monolithic", "B) Microkernel", "C) Hybrid", "D) Middleware"],
        ["A) Shared Memory", "B) Message Passing", "C) Paging", "D) Thrashing"],
        ["A) Manage CPU", "B) Manage RAM", "C) Control hardware devices", "D) Handle system calls"],
        ["A) Round Robin", "B) First Come First Serve (FCFS)", "C) Shortest Job First", "D) Priority Scheduling"],
        ["A) A part of RAM", "B) A section where processes execute critical operations", "C) A disk section", "D) A CPU section"],
        ["A) Waiting", "B) Running", "C) Terminated", "D) Blocked"],
        ["A) exec()", "B) fork()", "C) create()", "D) spawn()"],
        ["A) First Come First Serve (FCFS)", "B) Shortest Job First (SJF)", "C) Round Robin (RR)", "D) Priority Scheduling"],
       
    # Basic Level Questions
    ["A) Software that manages hardware", "B) A programming language", "C) A type of hardware", "D) A database"],
    ["A) Linux", "B) Python", "C) Windows", "D) macOS"],
    ["A) Kernel", "B) Shell", "C) Application", "D) Compiler"],
    ["A) Manage hardware and software", "B) Write code", "C) Perform calculations", "D) Design applications"],
    ["A) The core of the OS", "B) A user interface", "C) A type of memory", "D) A storage device"],
    ["A) Windows", "B) Linux", "C) macOS", "D) Solaris"],
    ["A) Processes tasks within a deadline", "B) Runs in batch mode", "C) Uses only single-user mode", "D) Runs without a CPU"],
    ["A) Supports multiple users", "B) Supports only one user", "C) Can run only one process", "D) Works without memory"],
    ["A) Managing memory", "B) Controlling hardware", "C) Running applications", "D) Writing code"],
    ["A) GUI-based OS", "B) A text-based interface", "C) A programming tool", "D) A network protocol"],

    # Process Management
    ["A) A program in execution", "B) A piece of memory", "C) A hardware component", "D) A network device"],
    ["A) Running", "B) Ready", "C) Waiting", "D) Terminated"],
    ["A) Stores process information", "B) Controls hardware", "C) Runs user programs", "D) Manages user accounts"],
    ["A) FIFO", "B) SJF", "C) Round Robin", "D) Priority Scheduling"],
    ["A) First-Come-First-Serve", "B) Shortest Job Next", "C) Round Robin", "D) Priority Scheduling"],
    ["A) Changing the running process", "B) Removing processes", "C) Allocating memory", "D) Running a program"],
    ["A) Measure time", "B) Prevent starvation", "C) Allocate CPU time", "D) Control memory"],
    ["A) First-Come-First-Serve", "B) Round Robin", "C) Shortest Job First", "D) Multilevel Queue"],
    ["A) Allocate memory", "B) Load processes", "C) Schedule processes", "D) Manage user permissions"],
    ["A) A completed process", "B) A waiting process", "C) A process with no parent", "D) A terminated but not removed process"],

    # Threads & Concurrency
    ["A) A lightweight process", "B) A process segment", "C) A kernel component", "D) A memory block"],
    ["A) Processes share resources, threads don't", "B) Threads run independently, processes don't", "C) Processes have separate memory, threads share memory", "D) Threads are slower than processes"],
    ["A) User-level", "B) Kernel-level", "C) Hardware-level", "D) Application-level"],
    ["A) Running multiple processes", "B) Running multiple threads in a process", "C) Executing a program", "D) Running multiple programs on different computers"],
    ["A) Faster execution", "B) Uses more memory", "C) Slows down processing", "D) Increases CPU usage"],
    ["A) A process error", "B) Incorrect thread execution order", "C) Conflict between threads", "D) A type of memory"],
    ["A) A protected memory area", "B) A process state", "C) A CPU register", "D) A scheduling algorithm"],
    ["A) Mutex", "B) Semaphore", "C) Pipeline", "D) Deadlock"],
    ["A) Prevents race conditions", "B) Optimizes memory", "C) Schedules processes", "D) Controls CPU usage"],
    ["A) A threading issue", "B) A producer creating data for a consumer", "C) A memory leak", "D) A CPU scheduling algorithm"],

    # Memory Management
    ["A) Secondary storage", "B) The primary storage unit", "C) A cache memory", "D) A CPU register"],
    ["A) Paging", "B) Swapping", "C) Contiguous allocation", "D) Segmentation"],
    ["A) Moving a process to disk", "B) Moving a process to cache", "C) Allocating more memory", "D) Deleting a process"],
    ["A) Free space wastage", "B) Running multiple processes", "C) Managing memory", "D) Process execution"],
    ["A) First Fit", "B) Best Fit", "C) Worst Fit", "D) Next Fit"],
    ["A) Page Table", "B) TLB", "C) Cache", "D) MMU"],
    ["A) Swaps pages on demand", "B) Loads all pages initially", "C) Doesn't use swapping", "D) Uses fixed partitions"],
    ["A) FIFO", "B) LRU", "C) Optimal", "D) Random"],
    ["A) High CPU usage", "B) Frequent page swapping", "C) Insufficient memory", "D) Process scheduling delay"],
    ["A) Page table", "B) Cache", "C) Register", "D) RAM"],

    # File Systems
    ["A) A storage structure", "B) A network protocol", "C) A memory unit", "D) A user interface"],
    ["A) Contiguous", "B) Indexed", "C) Linked", "D) Random"],
    ["A) A file index", "B) A memory block", "C) A process table", "D) A disk scheduler"],
    ["A) FAT32", "B) NTFS", "C) EXT4", "D) HFS+"],
    ["A) Slow disk performance", "B) Running multiple OS", "C) A security issue", "D) A boot error"],
    ["A) Connects a file system", "B) Formats the disk", "C) Deletes all files", "D) Compresses files"],
    ["A) File allocation table", "B) Directory structure", "C) File permissions", "D) Virtual memory"],
    ["A) Indexing", "B) Fragmentation", "C) Defragmentation", "D) Partitioning"],
    ["A) Full directory path", "B) A relative path", "C) A hidden file", "D) A symbolic link"],
    ["A) Read", "B) Write", "C) Execute", "D) Modify"],
  
    ["A mechanism that allows I/O devices to access memory directly", "A process that increases CPU speed", "A method of disk defragmentation", "A technique for virtual memory management"],
    ["Hard disk", "Monitor", "Keyboard", "Mouse"],
    ["SSTF (Shortest Seek Time First)", "FIFO (First In First Out)", "SCAN", "C-SCAN"],
    ["A process that manages printing jobs", "A type of memory management", "A method for CPU scheduling", "A hardware component in a computer"],
    ["A signal that temporarily halts CPU execution", "A process that speeds up CPU execution", "A technique for increasing RAM size", "A method for swapping processes"],
    ["SSD", "RAM", "Cache", "Registers"],
    ["A data storage virtualization technology", "A method for compressing files", "A CPU scheduling technique", "A type of file system"],
    ["RAID 10", "RAID 0", "RAID 1", "RAID 5"],
    ["Time taken to move the disk head to a specific track", "Time taken to read data from the disk", "Total execution time of a process", "Time taken to fetch data from RAM"],
    ["SCAN", "SSTF", "FIFO", "LOOK"],
    
    ["Creating virtual instances of resources", "Increasing the speed of a processor", "A security technique", "A method of disk fragmentation"],
    ["Hypervisor", "Compiler", "Debugger", "Scheduler"],
    ["Software that creates and manages virtual machines", "A tool for increasing RAM", "A type of cloud storage", "A CPU scheduling algorithm"],
    ["Type-1 Hypervisor", "Type-2 Hypervisor", "Process Virtualization", "Memory Virtualization"],
    ["On-demand access to computing resources over the internet", "A technique for cooling data centers", "A method for encrypting files", "A programming language"],
    ["SaaS", "PaaS", "IaaS", "DaaS"],
    ["Private Cloud", "Public Cloud", "Hybrid Cloud", "Community Cloud"],
    ["A lightweight virtualization method using containers", "A type of computer networking", "A process of data compression", "A programming paradigm"],
    ["Docker", "VMware", "Hyper-V", "OpenStack"],
    ["IaaS", "PaaS", "SaaS", "DaaS"],
    
    ["A list that defines access permissions for users", "A method of data encryption", "A type of firewall", "A security vulnerability"],
    ["User authentication", "Defragmentation", "Process scheduling", "Disk fragmentation"],
    ["A network security system that monitors and controls incoming and outgoing network traffic", "A hardware component that increases CPU speed", "A tool for memory management", "A process scheduling algorithm"],
    ["Buffer overflow attack", "Man-in-the-middle attack", "SQL injection", "Denial of Service (DoS) attack"],
    ["A program designed to detect and remove malware", "A type of network protocol", "A virtual memory management technique", "A CPU optimization tool"],
    ["Verifying the identity of a user", "A method for disk scheduling", "A programming language", "A technique for increasing RAM"],
    ["Username & Password", "CPU Scheduling", "Process Management", "Memory Fragmentation"],
    ["Access control", "Disk defragmentation", "Process scheduling", "Cache memory optimization"],
    ["The process of converting information into a secure format", "A technique for increasing CPU speed", "A type of network protocol", "A hardware component"],
    ["Scrambling data to prevent unauthorized access", "A method for data compression", "A type of file system", "A process scheduling algorithm"],
    
    ["A minimalistic operating system core that provides essential services", "A type of cloud storage", "A method for increasing RAM size", "A programming language"],
    ["Linux", "Windows NT", "Unix", "MS-DOS"],
    ["An OS designed for dedicated devices with specific functions", "A virtualized operating system", "A high-performance computing OS", "A cloud-based OS"],
    ["Real-time OS (RTOS)", "Batch OS", "Multi-user OS", "Network OS"],
    ["A system that allows multiple computers to work together as one", "A technique for optimizing memory", "A method for CPU scheduling", "A type of file system"],
    ["Rate-Monotonic Scheduling", "Round Robin", "FIFO", "Multilevel Queue"],
    ["Distributing workloads efficiently across multiple computing resources", "A process scheduling technique", "A method for encrypting files", "A programming paradigm"],
    ["Android", "Windows", "Linux", "MacOS"],
    ["Supports larger memory and better processing power", "Uses less power", "Increases CPU clock speed", "Has more colors"],
    ["Linux", "Windows HPC Server", "Unix", "MS-DOS"]




    ]

    # Select a random question
    select = random.randint(0, len(question1) - 1)

    # Shuffle options for randomness
    random.shuffle(options1[select])

    # Extract four options randomly
    d1, d2, d3, d4 = options1[select]
    

o()

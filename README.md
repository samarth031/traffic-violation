# traffic-violation
Code to find traffic violations using Hash tables and Trees

All violations are noted by a traffic policeman in a file as a record <license number of driver, fine amount>. At the end of each day, files from all traffic policemen are collated. If a driver had been charged with more than three violations so far, then he has to be booked for further legal action. Also, the police department provides additional bonus to those policemen who have brought in large fine earnings. All policemen who have collected equal to or more than 90% of the highest total fine collected by an individual policeman, shall be awarded the bonus.
The program should help the police department answer the below queries:
1. Find out the drivers who are booked for legal action: All such license numbers are to be output in a file called “violators.txt”.
2. Find out the policemen who are eligible for bonus: The list of policemen eligible for bonus must be output in a file called “bonus.txt”.
3. Perform an analysis of questions 1 and 2 and give the running time in terms of input size, n.

-------

Use hash tables for keeping track of drivers (and their violations), and a binary tree for keeping track of policemen (and their bookings).
Data structures to be used:
DriverHash: A separately chained hash table indexed by license numbers where each entry is of the form < license number, number of violations>. A simple hash function h(x) = x mod M, where M is the size of hash table can be used for this.
PoliceTree: This is a Binary Tree of entries of the form <police ID, total fine amount>

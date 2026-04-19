#  Password Cracking and Secure Hashing Project

##  Overview
This project demonstrates password cracking techniques and secure hashing mechanisms using Kali Linux.
It highlights how weak passwords can be compromised using dictionary attacks and how modern security techniques such as SHA-256 hashing and salting improve password security.

##  Objectives
- Demonstrate dictionary attack using John the Ripper
- Show weakness of plain text and MD5 hashing
- Implement SHA-256 hashing using Python
- Apply salting for enhanced security
- Compare different security levels

##  Tools Used
- Kali Linux
- John the Ripper
- Python

## Project Workflow
1. Created weak password file (plain text)
2. Generated MD5 hashes
3. Performed dictionary attack on MD5 (successfully cracked)
4. Generated SHA-256 hashes
5. Attempted attack on SHA-256 (slow)
6. Applied salting to passwords
7. Compared security results

## Results

Method  Result 
 Plain Text  Easily Readable 
 MD5 Cracked 
 SHA-256  Difficult to Crack 
 Salted Passwords Highly Secure 
 
##  Conclusion
This project shows that weak passwords and outdated hashing algorithms like MD5 are insecure. Strong hashing (SHA-256) combined with salting significantly improves password security.

##  Files Included
- password.txt
- hashed(md5).txt
- hashed_password (sha256).txt
- salted_password.txt
- Python scripts (hashing & salting)

# Natas Level 2 -> 3

# Primary Security Concept
robots.txt enumeration & hidden directory exposure

# Approach 
- Inspected page source and observed a reference to blocked content
- Investigated /robots.txt
- Identified hidden directory path /s3cr3t/
- Navigated to directory and located credentials


# Outcome
- Successfully retireved the password for the next level.

# Evidence
![Level 3 Screenshots](../screenshots/level03.md)

# Key Learning
Security through obscurity is ineffective. Attackers routinely enumerate 'robots.txt' and directory paths to locate hidden sensitive resources.

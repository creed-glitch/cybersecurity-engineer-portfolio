# Natas Level 8 -> 9

# Primary Security Concept
Command injection vulnerability through unsantitized user input

---

# Approach 
- Inspected page source and identified unsafe usage of the 'passthru()' function
- Crafted input containing command separators to escape intended execution flow
- Injected additional commands to access protected system files

--- 

# Outcome
Successfully executed injected system commands and retrieved the password for Level 10.

---

# Evidence
![Level 9 Screenshots](../screenshots/level09.md)

---

# Key Learning 
Failure to sanitize user input can allow attackers to execute arbitary system commands, leading to full system compromise.

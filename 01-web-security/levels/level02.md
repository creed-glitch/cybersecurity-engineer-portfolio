# Natas Level 1 -> 2

# Primary Security Concept 
Insecure directory exposure and improper file access controls

---

# Approach 
- Inspected webpage elements and indentified a hidden image reference 'files/pixel.png'
- Opened the image in a new browser tab
- Observed a visible directory path in the URL
- Removed the image filename to access the full directory listing
- Located and examined the 'users.txt' file containing crednentials

---

# Outcome
Successfully retrieved the password for Level 3 from an exposed directory.

--- 
# Evidence
![Level 2 Screenshot](../screenshots/level02.md)

---
# Key Learning
Public directory listings can expose sensitive files if proper access controls are not enforced.

# Natas Level 6 -> 7 

# Primary Security Concept
Insecure exposure of sensitive file paths through HTML comments

---

# Approach 
- Inspected page source and discoverd a hidden HTML comment revealing a file path
- Appended the disclosed directory path to the base URL
- Accessed the file containing senesitve authentication data

--- 

# Outcome
Successully retrieved the password for Level 8. 

---

# Evidence
![Level 7 Screenshot](../screenshots/level07.md)

---

# Key Learning
Hidden comments and developer notes can expose sensitive interal file paths and should never be left accessible in production environments.

# Natas Level 0

# Primary Security Concept
Exposed source code containing sensitive credentials

---

### Approach 
- Inspected the web page using browser developer tools
- Viewed the page source code to identify hidden comments
- Located a plaintext password embedded within an HTML comment

---

### Outcome
Successfully retrieved the password for Level 1 from exposed source code. 

---

### Evidence
![Level 0 Screenshot](../screenshots/level00.md)

--- 

### Key Learning
Sensitive credentials should neve be stored in client-side source code, even if hidden within comments, as attackers can easily inspect and retrieve them. 

# Natas Level 4 -> 5

# Primary Security Concept 
Insecure cookie-based authentiation control

---

# Approach
- Opened browser developer tools and inspected cookies
- Identified a 'loggedin' cookie set to '0'
- Modified the cookie value to '1' to simulate authenticated access
- Reloaded the page to gain unauthorized access

---

# Outcome 
Successfully bypassed authentication and retrieved the password for Level 6.

---

# Evidence 
![Level 5 Screenshot](../screenshots/level05.md)

---

# Key Learning
Client-side authentication controls using cookies can be manipulated if not properly validated server-side.

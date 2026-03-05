# Natas Level 3 -> 4

# Primary Security Concept
Referrer-based authentication bypass

---

# Approach 
- Used Burp Suite to intercept HTTP requests
- Modified the HTTP referrer header to spoof requests as originating from a trusted source
- Replayed manipulated requests until authentication checks were bypassed

---

# Outcome
Successfully bypassed access controls and retrieved the password for Level 5.

---

# Evidence
![Level 4 Screenshot](../screenshots/level04.md)

---

# Key Learninng 
Authentication mechanisms relying soley on referrer headers are insecure and easily manipulated.

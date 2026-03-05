# Natas Level 5 -> 6

# Primary Security Concept 
Sensitive file exporsure through insecure source code references

--- 

# Approach 
- Inspected the page source code using browser developer tools
- Identified a referenced file path 'includes/secret.inc'
- Manually appended the path to the base URL
- Retrieved the secret value stored in the exposed configuration file
- Submitted the extracted secret to obtain the next password

---

# Outcome
Successfully retrieved the password for Level 7.

---

# Evidence
![Level 6 Screenshots](../screenshots/level06.md)

---

# Key Learning
Senstive configuration files should never be publicly accessible, as source code references can reveal critical system secrets.

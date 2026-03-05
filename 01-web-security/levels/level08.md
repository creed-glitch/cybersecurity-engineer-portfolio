# Natas Level 7 -> 8

# Primary Security  Concept
Weak secret obfuscation and reversible encoding

---

# Approach 
- Inspected page source and analyzed the secret verification function
- Identified reversible encoding logic applied to the secret
- Reimplemented the tranformation logic using Pythhon
- Generated the correct decoded value required for authentication

---

# Outcome
Successfully computed the correct secret and retrieved the password for Level 9.

---

# Evidence
![Level 8 Screenshots](../screenshots/level08.md)

---

# Key Learning
Obfuscation without cryptographic security provides little protection, as attacker can reverse engineered encoding logic.

# TODO - Critical Issues

### **Global State Race Condition**

- **File**: `cogs/fun/games.py:15-24`
- **Issue**: Class-level `is_game_active` shared across all servers
- **Impact**: Game state conflicts in multi-server deployments
- **Fix**: Use per-guild game state management

## Minor Issues

### **Inconsistent Error Handling**

- Several commands lack proper error handling for user input validation
- Should add try/catch blocks for user-facing commands

### **Missing Logging**

- No structured logging for debugging and monitoring
- Should add proper logging instead of print statements

---

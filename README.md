# Window Manager Simulation

## Details
**Name:** Saad Arqam  
**URN:** 2024-B-02122005A  

---

## Problem Statement

Design a simplified window manager system similar to a desktop environment.

- Each window is identified by a unique ID  
- A window can be in one of three states:  
  - **OPEN**
  - **MINIMIZED**
  - **CLOSED**

### Key Requirements:
- Only **OPEN** windows are visible  
- Windows must be maintained in a strict **z-order (top → bottom)**  
- The system should support:
  - Open
  - Focus
  - Minimize
  - Restore
  - Close  

---

## Data Structure Selection

To efficiently manage window ordering and operations:

- A **Doubly Linked List (DLL)** with dummy head and tail nodes is used to maintain the z-order of open windows  
- A **HashMap (`dict`)** stores references to nodes for O(1) access  
- Another **HashMap** tracks the current state of each window  

### Why this works:
This combination allows:
- Fast insertion and deletion in O(1)
- Direct access to any window in O(1)

---

## State Handling

Each operation validates the current state before execution:

- Only **OPEN** windows can be minimized  
- Only **MINIMIZED** windows can be restored  
- **FOCUS**:
  - Restores the window if minimized  
  - Then brings it to the top  
- Operations on closed or non-existent windows are safely ignored  

This ensures correct and consistent state transitions.

---

## Edge Case Handling

- If no windows are open, `top()` returns **-1**  
- Invalid operations (e.g., minimizing a closed window) are ignored  
- Re-opening a closed window creates a **new instance**  
- Focusing a minimized window automatically restores it before moving it to the top  

---

## Summary

The solution efficiently handles all operations using:
- **Doubly Linked List** → maintains order  
- **HashMaps** → enable constant-time access  

All major operations run in **O(1)** time, ensuring scalability for large inputs.
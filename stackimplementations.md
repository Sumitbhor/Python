### 🧠 **1. Undo / Redo Functionality (Text Editors, IDEs)**

**Applications:**

* Microsoft Word
* Notepad++
* Visual Studio Code

**How stack is used:**

* One stack stores actions for **Undo** (last operation undone first).
* Another stack stores actions for **Redo** (if the user redoes an undone action).

---

### 🌐 **2. Web Browsers (Back / Forward Navigation)**

**Applications:**

* Google Chrome
* Mozilla Firefox
* Microsoft Edge

**How stack is used:**

* One stack stores visited pages (**Back stack**).
* When the user goes back, the page is pushed onto a **Forward stack**.
* Allows moving backward and forward efficiently.

---

### 📞 **3. Function Call Management (Call Stack)**

**Applications:**

* All programming languages’ **runtime systems** (Python, Java, C, etc.)
* IDEs and debuggers like **PyCharm**, **Eclipse**, **VS Code**

**How stack is used:**

* Function calls are pushed on the **call stack**.
* When a function returns, it’s popped from the stack.

---

### 🧮 **4. Expression Evaluation and Syntax Parsing**

**Applications:**

* Compilers (GCC, Clang, Java Compiler)
* Calculators
* Programming interpreters

**How stack is used:**

* Used in **infix → postfix** conversion and **postfix evaluation**.
* Used by compilers to check **balanced parentheses** or evaluate expressions.

---

### 🎮 **5. Game Development (State Management)**

**Applications:**

* Unity Engine
* Unreal Engine

**How stack is used:**

* **Game states** (e.g., main menu, pause menu, gameplay) are managed using a stack.
* Push new state (pause), pop it to return to previous state (gameplay).

---

### 🧰 **6. Software with Recursive Features**

**Applications:**

* Photoshop (filter layering)
* Blender (object transformation hierarchy)

**How stack is used:**

* To manage **recursive** or **nested transformations/actions**.

---

### 🧾 **7. Browser Tab History Management**

**Applications:**

* Chrome / Edge (individual tab histories)

**How stack is used:**

* Each tab’s navigation uses a separate **stack** for forward/backward pages.

---

### 🕹️ **8. Virtual Machines & Interpreters**

**Applications:**

* Java Virtual Machine (JVM)
* Python Interpreter (CPython)

**How stack is used:**

* Each thread has its own **stack frame** to handle method calls and local variables.

---

### 🧩 **9. Undo/Redo in Design Software**

**Applications:**

* Adobe Photoshop
* Figma
* AutoCAD

**How stack is used:**

* Stores previous design states (actions pushed/popped for undo/redo).

---

### 📚 **10. Browser / App Navigation History**

**Applications:**

* Android apps (Activity stack)
* iOS apps (Navigation controller stack)

**How stack is used:**

* New activity/screen is pushed when opened.
* Pressing “Back” pops the current screen.

---

✅ **In summary:**

| Application Type | Example Software | Stack Usage                        |
| ---------------- | ---------------- | ---------------------------------- |
| Text Editor      | MS Word, VS Code | Undo/Redo                          |
| Web Browser      | Chrome, Firefox  | Back/Forward Navigation            |
| Compiler         | GCC, JVM         | Expression Parsing, Function Calls |
| Game Engine      | Unity, Unreal    | Game State Management              |
| Design Software  | Photoshop, Figma | Undo/Redo Actions                  |
| Mobile App       | Android/iOS      | Screen Navigation Stack            |

 
##  Features
- Add new tasks with title, assignee, and due date.  
- Update task status (e.g., OPEN, DONE, INPR).  
- List all tasks in a conversation.  
- Delete entire conversations along with their tasks & messages.  
- Simple chat interface where the assistant understands natural language commands.

---

**File Explanations:**

- **demo.py**:  
  This is the main entry point of the application. Running this file launches the interactive Command line interface where users can manage their tasks via natural language.

- **db.py**:  
  Contains all the functions to **interact with the SQLite database**, including creating tables, inserting new tasks,deleting conversations, updating task status, and retrieving task list.

- **tools.py**:  
  Implements the **task management tools** that the AI agent uses to execute user commands, such as adding new tasks, listing current tasks, updating the tasks.

- **agent.py**:  
  Sets up the **LangChain AI agent**, defines how it interprets user instructions, and connects it to the task management tools.

- **chat_tasks.db**:  
  SQLite database file where all **tasks, messages, and conversation history** are stored .



##  Example Commands
- `You: Add a task "Prepare project report" for Aditya due on 2025-09-15`  
- `Employer: Please create a task to review code assigned to Lakshay.`  
- `You: Mark the first task as DONE.`  
- `Employer: Show me all tasks.`  
- `You: Delete this conversation.`  

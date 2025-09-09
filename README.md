#  Task Updater

This project is an **AI-powered task manager** that helps you create, update, list, and manage tasks through natural conversations.  
It uses **LangChain + Google Gemini** for AI reasoning and integrates with a **SQLite database** to store tasks and conversations.

---

##  Features
- Add new tasks with title, assignee, and due date.  
- Update task status (e.g., OPEN, DONE, INPR).  
- List all tasks in a conversation.  
- Delete entire conversations along with their tasks & messages.  
- Simple chat interface where the assistant understands natural language commands.

---

##  Project Structure
Task_updater/
│── demo.py # Main chat interface
│── db.py # Handles SQLite database (tasks, conversations, messages)
│── tools.py # Tools for adding, updating, listing, deleting tasks
│── agent.py # LangChain agent setup
│── chat_tasks.db # SQLite database file
│── .env # API keys and environment variables
│── README.md # Project Working


##  Example Commands
- `You: Add a task "Prepare project report" for Aditya due on 2025-09-15`  
- `Employer: Please create a task to review code assigned to Lakshay.`  
- `You: Mark the first task as DONE.`  
- `Employer: Show me all tasks.`  
- `You: Delete this conversation.`  

import db
from agent import get_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def run_demo():
    """
    Runs a command-line demo of the task-updating chat with memory.
    The agent listens to messages and creates or updates tasks in the database.
    """
    print("Starting demo setup...")
    db.init_db()
    conv_id = "conv1"
    db.create_conversation(conv_id, "Demo Chat")
    agent_executor = get_agent()

    # --- Initialize chat history ---
    chat_history = [
        SystemMessage(content="You are a helpful assistant who helps the user manage tasks."),
    ]
    
    print("Setup complete. Starting chat interface.")
    print("=== Task Updater Chat Demo ===")
    print("Type messages as 'You: message' or 'Employer: message'")
    print("Commands: /tasks, /exit")
    print("-"*30)

    while True:
        msg = input("> ").strip()
        if msg == "/exit":
            print("Exiting chat. Goodbye!")
            break
        
        # listing all the tasks for the current conversation
        if msg == "/tasks":
            # Explicitly ask the agent to list tasks for the current conversation
            response = agent_executor.invoke({"input": f"List all tasks for conversation {conv_id}", "chat_history": chat_history})
            print("Agent:", response["output"])
            chat_history.append(AIMessage(content=response["output"]))
            continue
        
        # deleting the current chat
        if msg == "/delete chat":
            # Delete the chat and related task and messages
            db.delete_conversation(conv_id)
            print(f"Successfullt deleted chat for {conv_id}")
            continue
        
        if ":" not in msg:
            print("Please format your message as 'You: message' or 'Employer: message'")
            continue

        sender, text = msg.split(":", 1)
        sender, text = sender.strip(), text.strip()
        
        # Save the message to the database
        db.add_message(conv_id, sender, text)

        # Append the new human message to history
        human_message_content = f"In conversation {conv_id}, {sender} said: '{text}'. If this is a task or update, handle it."
        chat_history.append(HumanMessage(content=human_message_content))

        # Invoke agent with the full history
        response = agent_executor.invoke({"input": human_message_content, "chat_history": chat_history})
        
        # Add agent's response to history for next turn
        print("Agent:", response["output"])
        chat_history.append(AIMessage(content=response["output"]))

if __name__=="__main__":
    run_demo()
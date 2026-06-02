import os
from datetime import datetime

def log_conversation(history_text, folder="conversation_history"):
    """
    Saves the conversation history to a markdown file with a timestamp.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    timestamp = datetime.now().strftime("%m%d%H%M")
    filename = f"conversation_history_{timestamp}.md"
    filepath = os.path.join(folder, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(history_text)
    
    print(f"Successfully saved history to {filepath}")

if __name__ == "__main__":
    # Example usage (this would be called with actual history content)
    sample_history = "# Conversation History\n\nSample content."
    log_conversation(sample_history)

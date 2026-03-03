def show_messages(messages):
    """Exibe uma simples menssagem de texto"""
    for message in messages:
        print(message)

def send_messages(sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Transfering message: {current_message}")
        sent_messages.append(current_message)
  
messages = ['hello', 'goodbye', 'welcome', 'hi']
sent_messages = []

show_messages(messages)
send_messages(sent_messages)

print(f"\nMessages: {messages}")
print(f"Sent Messages: {sent_messages}")

def show_messages(text_messages):
    """display text messages"""
    for msg in text_messages:
        text= f'{msg.title()}'
        print(text)
short_text_messages = ['hi', 'hello', 'bye', 'goodnight']
show_messages(short_text_messages)

print("\nMaking copy of my show messages:")
show_messages(short_text_messages[:])

def send_messages(call):
    
    while call:
        current_message = call.pop()
        print(f"Ready to sent message {current_message}")
        sent_messages.append(current_message)

sent_messages = []
print("\nThe messages before sending:")
show_messages(short_text_messages[:])
print("\nThe following messages has been sent:")
send_messages(show_messages(short_text_messages[:]))

print('\nThe original list still has its elements saved.')
print('Original List:')
show_messages(short_text_messages)
print('\nList after sending the copy of the Original List elements:')
send_messages(show_messages(short_text_messages[:]))

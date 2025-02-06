import lab_chat as lc
from lab_chat import get_peer_node, join_group, chat_task


def get_username():
    base_username = input("Enter desired username: ")
    username = base_username.strip().upper()
    print("Username set to " + username)
    return username
def get_group():
    base_group = input("Please specify desired group: ")
    group = base_group.strip().upper()
    print("Group selected: " + group)
    return group
def get_message():
    base_message = input("Send a message: ")
    message = base_message.strip().upper()
    return message
def initialize_chat():
    user = get_username()
    group = get_group()
    lc.get_peer_node(user)
    lc.join_group(group)
    lc.chat_task()
initialize_chat()
def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")
start_chat()

def get_peer_node(username): # this is a function named get_peer_node.
username: I assume this takes username provided by user. 
The get_peer_node returns a Pyre node object n that was previously defined as n = Pyre(username). 
This function appears to start a Pyre node for peer-to-peer communication.

def join_group(node, group): # this is a function named join_group.
node: I assume this takes node from Pyre.
group: I assume this takes group provided by user.
join_group does not return anything.
This function appears to join a group provided by the user and print a message saying which group.

def chat_task(ctx, pipe, n, group): # this is a function named chat_task.
ctx: ZeroMQ Connection Context.
pipe: communication pipe polled by ZeroMQ for messages.
n: takes Pyre node of chat.
group: takes input provided by user for group.
The function chat_task does not return anything.
This function likely establishes a connection and initiates communication in chat. It also establishes 
some basic formating of messages sent in the chat and new users joining the chat.

def get_channel(node, group): # function named get_channel.
node: takes Pyre node of chat. 
group: takes previously established group provided by user.
get_channel returns zhelper.zthread_fork which probably creates a new thread to run chat_task(). n=node: the 
node for communication. group=group: the group to join. ctx: ZeroMQ connection.  
chat_task: likely reruns chat task in a new thread, but I am not entirely sure...
this function allows multiple threads to be used. This could help make the chat run 
smoothly without being blocked by too many messages/ operations. 
# tocs
TOCS - is the TelegramOpenChatSystem that allows you to chat with other people without binding your personal data!

- [What is?](https://github.com/Bluty4444/tocs/edit/master/README.md#what-is)
- [Getting started](https://github.com/Bluty4444/tocs/edit/master/README.md#getting-started)
- [All commands](https://github.com/Bluty4444/tocs/edit/master/README.md#all-commands)
- [For Devs](https://github.com/Bluty4444/tocs/edit/master/README.md#for-devs)

# What is?
TOCS was inspired by xmpp chat systems and now endures it experence to telegram! Telegram is centralized system with general server on the top and client on the bottom, the tocs rejects this  idea and provides system without servers. The tocs won't collect your data and chat history and can be imply maintained only by one telegram bot! 

# Getting started

#### User creating

1. First you need to create new user or session (the same thing) by /setname command. Without session you can't do any commands in bot like room creating or connecting to other rooms
2. Then you can set password of you session by /setpass command so you can login in session from other Telegram accounts. It's not necessary but highly recommended 
3. And enjoy, from now you can do all of the tocs commands!

#### Start chatting

###### If you want own room
Type the /newroom with all arguments
- Room name. It is a public name of room, the users can use it to connect or delete the room (only creator can)
- Password. If the room is private you need it for connection, if not it used to deleting the room (only creator can)
- Room type (open or private). The private rooms won't be shown by /list command and require password for connection
###### If you don't want own room
Type /list and choose one you liked

Then type /connect with all arguments
If you're connecting to private room please type room password after room name
After that the chat history message will appear

Note: The tocs don't collect your chat history so keep this message if you need it

###### How to chat?
Just reply to the chat history message. The message will disapppear and will be shown on chat history

# All commands

### /help
#### Description:
Used to get full list of commands
#### args:
No args required

### /helpme
#### Description:
Used to get full info about command 
#### args:
- !command - command which info you want to get
Note:
Replace the / with ! in command to get info 

## Profile settings

### /setname 

#### Description:
Used for name change or session creation
#### args:
- name - public username \\
  legth conditions - 3 to 12 symbols
  
### /setpass
  
#### Description:
Used for user password change
#### args:
- password - user password \\
  legth conditions - 3 to 64 symbols

### /login
  
#### Description:
Used to assign the name of another user
#### args:
- name - name of user you want to assign
- password - password of user you want to assign

### /profile
  
#### Description:
Used to get self user info

Provides personal data like:
Your tocs user name
Password hash - hash of your tocs user password
Session hash - hash of your Telegram user id
#### args:
No args required

## Chat settings

### /newroom
#### Description:
Used to room creation
#### args:
- name - name of your room
- password - password of your room \\
  legth conditions - 6 to 12 symbols
- type - type of your room (open or private)

### /delroom
#### Description:
Used to delete room
#### args:
- name - name of room you want to delete

### /connect
#### Description:
Used to connect to rooms
#### args:
- name - name of room you want to connect

### /disconnect
#### Description:
Used to disconnect from rooms
#### args:
No args required

### /list
#### Description:
#### args:

### /dev
#### Description:
Info about me and my projects
#### args:
No args required

# For Devs

## The JSON files structure
### users.json
{
 "session hash" : [
 "User name",
 "Password hash",
  [
   connect_msg_id,
   "Current connection chat history"
  ]
 ]
}
### rooms.json
{
 "room name" : [
  "Creator session hash",
  "Room password hash",
  "Room type"
 ],
 [
  connected_telegram_users_ids
 ]
}
## General info
Hello guys, this project was oriented on safety of users and user's data so I built some protection into the tocs, but you need to understand that it is basic version of client. The code if fully open-source so you can simply fork and modify code. Good luck!

## PS: 
I will comment code in future updates ;)

from telethon import TelegramClient, events
from hashlib import sha256
import asyncio
import json

#logging | delete or comment for disable
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Enter your tg info there:
# App api_id
API_KEY = "12345" 
# App api_hash
API_HASH = '0123456789abcdef0123456789abcdef'
# Bot api_hash
BOT_API = '12345:0123456789abcdef0123456789abcdef'

client = TelegramClient(
	session="tocs",
    api_id=API_KEY,
    api_hash=API_HASH
).start(bot_token=BOT_API)


@client.on(events.NewMessage)
async def main(event):

	text = event.text.split(r' ')

	text[0] = text[0].lower()

	if text[0] == "/start":

		await event.respond("Hello, it's basic implementation of tocs - TelegramOpenChatSytem.\
			\nYou can simply chat in Telegram without binding your personal data, Good luck!")

	elif text[0] == "/help":

		await event.respond("**Command list** \n\
			`/helpme` <!command> | get full info about command \n\
			\n\
			**profile settings** \n\
			`/setname` <username> \n\
			`/setpass` <password> \n\
			`/login` <username> <password> \n\
			`/profile` \n\
			\n\
			**chat settings** \n\
			`/newroom` <room name> <password> <type: `open/private`> \n\
			`/delroom` <room name> <password> \n\
			`/connect` <room name> <password: only if room is private> \n\
			`/disconnect` \n\
			`/list` \n\
			\n\
			`/dev` | see the dev's corner \
			")

	elif text[0] == "/helpme":

		text[1] = text[1].lower()
		
		with open("helpme.json", encoding='utf-8') as in_helpme:
		
			heplme = json.loads(in_helpme.read())

		in_helpme.close()

		docs = heplme.get(text[1])

		if docs != None:

			await event.respond(f"The {text[1]} command\n\n {docs}")

		else:

			await event.respond("**Ooopsie...**,\n\
				invalid command")

	elif text[0] == "/setname":

		hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

		with open("users.json", encoding='utf-8') as in_users:
		
			users = json.loads(in_users.read())

		in_users.close()

		userdata = users.get(hashid)

		legth = len(text[1])

		if userdata != None:

			await event.respond("**Session was found**\n\
				updating info...")

			if legth >= 3 and legth <= 12:

				usernames = list(users.values())

				if text[1] not in usernames:

					users.update({hashid : [text[1], userdata[1], userdata[2]]})

					with open("users.json", "w", encoding='utf-8') as out_users:

						json.dump(users, out_users, indent=4, ensure_ascii=False)

					out_users.close()

					await event.respond("**Successfully updated**,\n\
						try `/profile` for see your data")

				else:

					await event.respond("**ERROR**,\n\
						user with this name already exists")

			else:

				await event.respond("**ERROR**,\n\
					your username isn't match the requirements")

		else: 

			await event.respond("**Seems there's no your session**\n\
				Creating new user...")

			if legth >= 3 and legth <= 12:

				usernames = list(users.values())

				if text[1] not in usernames:

					users.update({hashid : [text[1], None, None]})

					with open("users.json", "w", encoding='utf-8') as out_users:

						json.dump(users, out_users, indent=4, ensure_ascii=False)

					out_users.close()

					await event.respond("**Successfully created**,\n\
						try `/profile` for see your data")

				else:

					await event.respond("**ERROR**,\n\
						user with this name already exists")

			else:

				await event.respond("**ERROR**,\n\
					your username isn't match the requirements")

	elif text[0] == "/setpass":

		hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

		with open("users.json", encoding='utf-8') as in_users:
		
			users = json.loads(in_users.read())

		in_users.close()

		userdata = users.get(hashid)

		if userdata != None:

			await event.respond("**Session was found**\n\
				updating info...")

			legth = len(text[1])

			if legth >= 3 and legth <= 64:

				userpass = sha256(f"{text[1]}".encode("utf-8")).hexdigest()

				users.update({hashid : [userdata[0], userpass, userdata[2]]})

				with open("users.json", "w", encoding='utf-8') as out_users:

					json.dump(users, out_users, indent=4, ensure_ascii=False)

				out_users.close()

				await event.respond("**Successfully updated**,\n\
					try `/profile` for see your data")

			else:

				await event.respond("**ERROR**,\n\
					your password isn't match the requirements")

		else: 

			await event.respond("**Seems there's no your session**,\n\
				please create new user by `/setname` command")

	elif text[0] == "/login":

		hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

		with open("users.json", encoding='utf-8') as in_users:
		
			users = json.loads(in_users.read())

		in_users.close()

		userdata = users.get(hashid)

		if userdata != None:

			usr_keys = list(users.keys())

			log_usr = []

			for user in usr_keys:

				userdata = users.get(user)

				if userdata[0] == text[1]:

					log_usr.append(userdata)

				else:

					continue

			if log_usr != []:

				await event.respond("**User has been found**,\n\
					trying to login...")

				for user in log_usr:

					userpass = sha256(f"{text[2]}".encode("utf-8")).hexdigest()

					if user[1] == userpass:

						users.update({hashid : [text[1], userdata[1], userdata[2]]})

						with open("users.json", "w", encoding='utf-8') as out_users:

							json.dump(users, out_users, indent=4, ensure_ascii=False)

						out_users.close()

						await event.respond("**Successfully logined**")

						break

					else:

						continue

				else:

					await event.respond("**ERROR**,\n\
						invalid password")

			else:

				await event.respond("**ERROR**,\n\
					there's no users with this name")

		else: 

			await event.respond("**Seems there's no your session**,\n\
				please create new user by `/setname` command")

	elif text[0] == "/profile":

		hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

		with open("users.json", encoding='utf-8') as in_users:
		
			users = json.loads(in_users.read())

		in_users.close()

		userdata = users.get(hashid)

		if userdata != None:

			await event.respond(f"**- - Your profile - -**\n\n\
				**Username**: \n`{userdata[0]}` \n\
				\n\
				**Password hash**: \n`{userdata[1]}` \n\
				**Session hash**: \n`{hashid}`\
				")

		else:

			await event.respond("**Seems there's no your session**,\n\
				please create new user by `/setname` command")

	elif text[0] == "/newroom":

		hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

		with open("rooms.json", encoding='utf-8') as in_rooms:
		
			rooms = json.loads(in_rooms.read())

		in_rooms.close()

		roomdata = rooms.get(text[1])

		if roomdata == None: 

			passlegth = len(text[2])

			if passlegth >= 6 and passlegth <= 12:

				roompass = sha256(f"{text[2]}".encode("utf-8")).hexdigest()

				if text[3] == "open" or text[3] == "private":

					await event.respond("**Creating new room**")

					rooms.update({text[1] : [[hashid, roompass, text[3]], []]})

					with open("rooms.json", "w", encoding='utf-8') as out_rooms:

						json.dump(rooms, out_rooms, indent=4, ensure_ascii=False)

					out_rooms.close()

					await event.respond(f"**Successfully created**,\n\
						try `/connect {text[1]}` to connect")

				else:

					await event.respond("**ERROR**,\n\
						you have entered the invalid room type")

			else:

				await event.respond("**ERROR**,\n\
					your room password isn't match the requirements")

		else:

			await event.respond("**ERROR**,\n\
				room with this name already exists")
		
	elif text[0] == "/delroom":
		
		with open("rooms.json", encoding='utf-8') as in_rooms:
		
			rooms = json.loads(in_rooms.read())

		in_rooms.close()

		roomdata = rooms.get(text[1])

		if roomdata != None:

			hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

			if roomdata[0][0] == hashid:

				await event.respond("**Room was found**,\n\
					trying to delete...")

				roompass = sha256(f"{text[2]}".encode("utf-8")).hexdigest()

				if roomdata[0][1] == roompass:

					rooms.pop(text[1])

					with open("rooms.json", "w", encoding='utf-8') as out_rooms:

						json.dump(rooms, out_rooms, indent=4, ensure_ascii=False)

					out_rooms.close()

					await event.respond("**Successfully deleted**,\n\
						try `/list` to see available rooms")

				else:

					await event.respond("**ERROR**,\n\
						invalid password")

			else:

				await event.respond("**ERROR**,\n\
					only creator can delete the room")

		else:

			await event.respond("**ERROR**,\n\
				there's no rooms with this name")

	elif text[0] == "/connect":

		await event.delete()

		hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

		with open("users.json", encoding='utf-8') as in_users:
		
			users = json.loads(in_users.read())

		in_users.close()

		userdata = users.get(hashid)

		if userdata[2] == None:

			with open("rooms.json", encoding='utf-8') as in_rooms:
		
				rooms = json.loads(in_rooms.read())

			in_rooms.close()

			roomdata = rooms.get(text[1])

			if roomdata != None:

				roomtype = roomdata[0][2]

				user_id = event.sender_id

				if roomtype == "open":
				
					user_ids = roomdata[1]

					user_ids.append(user_id)

					rooms.update({text[1] : [roomdata[0], user_ids]})

					with open("rooms.json", "w", encoding='utf-8') as out_rooms:

						json.dump(rooms, out_rooms, indent=4, ensure_ascii=False)

					out_rooms.close()

					out_text = f"{text[1]} || Chat History\n"

					await event.respond(out_text)

					conn_msg = event.id + 1

					users.update({hashid : [userdata[0], userdata[1], [conn_msg, out_text]]})

					with open("users.json", "w", encoding='utf-8') as out_users:

						json.dump(users, out_users, indent=4, ensure_ascii=False)

					out_users.close()

				elif roomtype == "private":

					roompass = sha256(f"{text[2]}".encode("utf-8")).hexdigest()

					if roompass == roomdata[0][1]:

						user_ids = roomdata[1]

						user_ids.append(user_id)

						rooms.update({text[1] : [roomdata[0], user_ids]})

						with open("rooms.json", "w", encoding='utf-8') as out_rooms:

							json.dump(rooms, out_rooms, indent=4, ensure_ascii=False)

						out_rooms.close()

						out_text = f"{text[1]} || Chat History\n\n"

						await event.respond(out_text)

						conn_msg = event.id + 1

						users.update({hashid : [userdata[0], userdata[1], [conn_msg, out_text]]})

						with open("users.json", "w", encoding='utf-8') as out_users:

							json.dump(users, out_users, indent=4, ensure_ascii=False)

						out_users.close()

					else:

						await event.respond("**ERROR**,\n\
							invalid password")

				else:

					await event.respond("**ERROR**,\n\
						invalid room type")

			else:

				await event.respond("**ERROR**,\n\
					there's no rooms with this name")

		else:

			await event.respond("**ERROR**,\n\
				you have been already connected")

	elif text[0] == "/disconnect":
		
		hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

		with open("users.json", encoding='utf-8') as in_users:
		
			users = json.loads(in_users.read())

		in_users.close()

		with open("rooms.json", encoding='utf-8') as in_rooms:
		
			rooms = json.loads(in_rooms.read())

		in_rooms.close()

		userdata = users.get(hashid)

		conn_msg = userdata[2][0]

		if userdata != None and conn_msg != None:

			await event.delete()

			users.update({hashid : [userdata[0], userdata[1], None]})

			with open("users.json", "w", encoding='utf-8') as out_users:

				json.dump(users, out_users, indent=4, ensure_ascii=False)

			out_users.close()

			roomname = userdata[2][1].split(" || ")[0]

			roomdata = rooms.get(roomname)

			roomdata[1].remove(event.sender_id)

			rooms.update({roomname : roomdata})

			with open("rooms.json", "w", encoding='utf-8') as out_rooms:

				json.dump(rooms, out_rooms, indent=4, ensure_ascii=False)

			out_rooms.close()

			await event.respond("**Successfully disconnected**")

			msg_id = event.id + 1

			await asyncio.sleep(1)

			await client.delete_messages(event.sender_id, msg_id)

		else:

			await event.respond("**ERROR**,\n\
				you have been already disconnected")

	elif text[0] == "/list":

		with open("rooms.json", encoding='utf-8') as in_rooms:
		
			rooms = json.loads(in_rooms.read())

		in_rooms.close()

		out_rooms = list(rooms.keys())

		for room in rooms:

			roomtype = rooms.get(room)

			if roomtype == "private":

				out_rooms.remove(room)

			else:

				continue

		out_rooms = '\n '.join(out_rooms)

		await event.respond(f"**List of available groups:** \n\n {out_rooms}")

	elif text[0] == "/dev":
		
		await event.respond("Hello dude!\
			\nMy name is bluty and I'm creator of this shit ( ͡° ͜ʖ ͡°)\
			\n\nOther projects:\
			\n[All dead :(](https://bit.ly/3HIf6mG)\
			\nLinks on me:\
			\n[4pda](https://4pda.to/forum/index.php?showuser=8883770)\
			\n[telegram](https://t.me/bluty4444)\
			\n[github](https://github.com/bluty4444)\
			\n\n#🇺🇦", link_preview=False)

	else:

		hashid = sha256(f"{event.sender_id}".encode("utf-8")).hexdigest()

		with open("users.json", encoding='utf-8') as in_users:
		
			users = json.loads(in_users.read())

		in_users.close()

		userdata = users.get(hashid)

		reply_msg = await event.get_reply_message()

		if userdata != None and reply_msg != None:

			conn_msg = userdata[2]

			if conn_msg[0] != None and conn_msg[0] == reply_msg.id:

				await event.delete()
				
				with open("rooms.json", encoding='utf-8') as in_rooms:
		
					rooms = json.loads(in_rooms.read())

				in_rooms.close()

				roomname = reply_msg.message.split(" || ")[0]

				user_ids = rooms.get(roomname)[1]

				if user_ids != None:
				
					for user_id in user_ids:

						hashid = sha256(f"{user_id}".encode("utf-8")).hexdigest()

						conn_msg = users.get(hashid)[2]

						out_text = f"{conn_msg[1]}\n**{userdata[0]}**\n{event.text}\n"

						userdata = users.get(hashid)

						users.update({hashid : [userdata[0], userdata[1], [userdata[2][0], out_text]]})

						await client.edit_message(user_id, conn_msg[0], out_text)

				with open("users.json", "w", encoding='utf-8') as out_users:

					json.dump(users, out_users, indent=4, ensure_ascii=False)

				out_users.close()

			else:

				pass

		else:

			pass


if __name__ == '__main__':
	
	client.run_until_disconnected()

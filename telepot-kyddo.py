import telepot
from pprint import pprint
import time

def smartReply(msg, id):
	mkeyboard = {'hide_keyboard': True}
	msg = msg.lower()
	if 'mumbai' in msg:
		mkeyboard={'keyboard': [['weather', 'places to visit']]}
		bot.sendMessage(id, 'Bahut Accha place. With great places to visit, you\'ll have a terrific experience. Wanna know more?', reply_markup=mkeyboard)
	elif any(map(lambda x: x in msg, ['weather', 'climate'])):
		bot.sendMessage(id, 'You might not be comfy-comfy with weather! It has highly humid and moderately hot climate. Not to sweat ji, you\'ll get thanda-thanda juice at every corner of the street', reply_markup=mkeyboard)
	elif any(map(lambda x: x in msg, ['beautiful', 'places', 'visit'])):
		with open('mumba2.jpg', 'rb') as f:  # some file on local disk
			response = bot.sendPhoto(id, f)
			pprint(response)
		with open('mumba1.jpg', 'rb') as f:  # some file on local disk
			response = bot.sendPhoto(id, f)
			pprint(response)
		bot.sendMessage(id, 'With places like Gateway of India, Girgaum beach, Babulnath temples and more, you\'ll have Jolly Fun, I say', reply_markup=mkeyboard)
	elif 'crime' in msg:
		bot.sendMessage(id, 'Time to get serious. With moderate (55.43) level of crime, you can be moderately sure that you won\'t get robbed or killed... or raped. Yeah, truth hurts. Also, name one city that is completely safe. #sadReality')
	elif any(map(lambda x: x in msg, ['book', 'flight', 'ticket', 'tickets', 'plane'])):
		mkeyboard={'keyboard': [['IndiGo 1h 30m from ₹ 4,428'],
			['SpiceJet SpiceJet 1h 40m from ₹ 4,584'],
			['GoAir GoAir 1h 15m from ₹ 4,650'],
			['Jet Airways Jet Airways 1h 35m from ₹4,764'],
			['Air India Air India 1h 35m from ₹ 5,644']
			]}
		bot.sendMessage(id, 'Flights from 5-9 July', reply_markup=mkeyboard)
	elif '1h' in msg:
		bot.sendMessage(id, 'Please book your flight from www.google.co.in/flights. Have a happy journey!', reply_markup=mkeyboard)
	else:
		bot.sendMessage(id, 'Tell me more...', reply_markup=mkeyboard)

def handle(blob):
	flavor = telepot.flavor(blob)
	if flavor == 'chat':
		content_type, chat_type, chat_id = telepot.glance(blob)
		print (content_type, chat_type, chat_id)
		if content_type == 'text':
			smartReply(blob['text'], blob['from']['id'])
	elif flavor == 'inline_query':
		query_id, from_id, query_string = telepot.glance(blob, flavor='inline_query')
		print ('Inline query:', query_id, from_id, query_string)
	pprint(blob)

bot = telepot.Bot('228012170:AAFyhTtVFfqkWfL3fOoEZ7lMYrCT9uriRkc')
bot.message_loop(handle)
print ('Listening...')

# Keep the program running
while True:
	time.sleep(10)

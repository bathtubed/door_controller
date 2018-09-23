import parse

def parse_from_swipe(raw_data):
	# ;6008870002357650=6614035050?
	iso, rin = parse.parse(";{}={}?", raw_data)
	
	return rin
	

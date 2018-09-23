import sys
from .parse_rin import *

def file_swipe(f=None):
	if f == None:
		f = sys.stdin
	for line in f:
		try:
			rin = parse_from_swipe(line)
			yield rin
		except:
			print("Failed to parse", line)

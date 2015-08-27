#!/usr/bin/env python3

import random
import simplejson
import string


def getRandomString(length=10, chars=string.ascii_lowercase) -> str:
	return "".join(random.choice(chars) for _ in range(length))


def getRandomDict(json=True):
	key = getRandomString()
	value = getRandomString()
	d = {key : value}
	if json:
		return simplejson.dumps(d)
	return d

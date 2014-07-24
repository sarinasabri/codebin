#!/usr/bin/env/python

import barf

code_keys = barf.Barf.msg_codes.keys()

i=0
for code in barf.Barf.msg_codes:
	if code is 'TAB':
		barf.Barf(code, "This be " + code_keys[i])
	else:
		barf.Barf(code, "This be " + code_keys[i] + " message with 12hr time.")
		barf.Barf(code, "This be " + code_keys[i] + " message with 24hr time.", time=True, hour=False)
		barf.Barf(code, "This be " + code_keys[i] + " message without time.", time=False)
	
	i += 1


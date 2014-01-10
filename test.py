#!/usr/bin/env/python

import barf

code_keys = barf.Barf.msg_codes.keys()

i=0
for code in barf.Barf.msg_codes:
	barf.Barf(code, "This be " + code_keys[i] + " message.")
	barf.Barf(code, "This be " + code_keys[i] + " message without time.\n", False)
	i += 1

#! /usr/bin/env python
#
# Barf, a cli message system.
#
# Author: Sina Mashek <mashek@thescoundrels.net>, Tristy H. <kittytristy@gmail.com>
# Version 1.4
# License: Expat, http://cptmashek.mit-license.org

import datetime
import time
from platform import system
from sys import modules


class Barf:
	def_codes = {
		'DEF': '    ',
		'ACT': ' [~]',
		'MSG': ' [-]',
		'SAV': ' [#]',
		'PLG': ' [*]',
		'DBG': ' [$]',
		'ERR': ' [!]',
		'ROL': ' [@]',
		'TAB': '\t'  # Left in for backwards compatibility
	}

	if system() == "Windows":
		try:
			from colorama import init
			init()
			msg_codes = {
				"DEF": '\033[0m%s' % def_codes['DEF'],
				"ACT": '\033[33m%s' % def_codes['ACT'],
				"MSG": '\033[44;36m%s' % def_codes['MSG'],
				"SAV": '\033[32m%s' % def_codes['SAV'],
				"PLG": '\033[35m%s' % def_codes['PLG'],
				"DBG": '\033[45;31m%s' % def_codes['DBG'],
				"ERR": '\033[31m%s' % def_codes['ERR'],
				"ROL": '\033[46;33m%s' % def_codes['ROL'],
				"TAB": def_codes['TAB']
			}
		except:
			print "Install the 'colorama' python package on Windows for ANSI color code support."
			msg_codes = def_codes
	else:
		msg_codes = {
			"DEF": '\033[0m%s' % def_codes['DEF'],
			"ACT": '\033[93m%s' % def_codes['ACT'],
			"MSG": '\033[94m%s' % def_codes['MSG'],
			"SAV": '\033[92m%s' % def_codes['SAV'],
			"PLG": '\033[35m%s' % def_codes['PLG'],
			"DBG": '\033[1;91m%s' % def_codes['DBG'],
			"ERR": '\033[91m%s' % def_codes['ERR'],
			"ROL": '\033[33m%s' % def_codes['ROL'],
			"TAB": def_codes['TAB']
		}

	def __init__(self, code, message, time=True, hour=True):

		if "debug = true" or "debug = True" in open('options.cfg').read():
			if code not in self.msg_codes:
				code = "DEF"

			if code == "TAB":
				print self.timeless_barf(code, message)
			else:
				print self.barf(code, message, time, hour)

	def get_time(self, hour):
		"""
		Make time sexy
		"""
		if hour is False:
			return time.strftime('[%I:%M:%S %p] ', time.localtime(time.time()))
		else:
			return time.strftime('[%H:%M:%S] ', time.localtime(time.time()))

	def get_time_for_file(self):
		return "%s-%s" % (datetime.date.today(), time.strftime("%H%M%S", time.localtime(time.time())))

	def barf(self, code, message, time, hour):
		if time is False:
			return self.timeless_barf(code, message)
		else:
			return self.raw_barf(code, message, hour)

	def raw_barf(self, code, message, hour):
		return self.color(code, self.get_time(hour) + message) + self.msg_codes["DEF"]

	def timeless_barf(self, code, message):
		return self.color(code, message) + self.msg_codes["DEF"]

	def color(self, code, message):
		if 'colorama' in modules:
			message = message.replace("\n", "\033[0m\n")
		return "%s %s" % (self.msg_codes[code], message)

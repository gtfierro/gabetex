#!/usr/bin/env Python
############################
#		GaBeTeX			   #
############################

import re
from parse import *

# use a dict to map english words and math functions to parsing functions and latex code

recognized = 	{
				'/': parse_frac,
				'*': parse_mult,
				'+': parse_add,
				'-': parse_sub
				}
				
				
# Read - Eval - Print - Loop				
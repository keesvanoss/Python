# Superpy.py

* ## Highlight 1): Date calculation
To make calculations with dates is difficult in Python. You do need the Datetime library to convert ASCII dates into date objects. This way you can make calculations with dates in an easy way. So first convert dates into dates objects before doing any calculations.

Example:
	# Convert dates to date objects for comparing
	exp_date = datetime.strptime(bought[key][3].strip("'"), '%Y-%m-%d')
	buy_date = datetime.strptime(bought[key][1].strip("'"), '%Y-%m-%d')

if buy_date <= exp_date:

* ## Highlight 2): Parameter check
When enetering routines, parameters are required. If you are missing parameters or having parameters in the wrong format, the program ends with an error. When entering a routine, I check f the right parameters are given and if dates are in the right format. If not, a decent message is displayed.

* ## Highlight 3)




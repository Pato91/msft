def draw_line(tl, label=''):
	''' draw a ruler line with a given tick length and an optional label '''
	line = '-' * tl
	if label:
		line += ' ' + label
	print(line)

def draw_interval(cl):
	''' draw tick interval based upon central tick length: cl'''
	if cl > 0:
		draw_interval(cl-1)
		draw_line(cl)
		draw_interval(cl-1)

def ruler(n, tl):
	''' recursively draw an englosh ruler upto mark n
	n:  number of cm for ruler
	tl: major tick length
	not drawn to scale

	Runtime : analyse the runtime of draw_interval() : (2^cl) - 1
	'''
	draw_line(tl, 'O')

	for i  in range(1, n+1):
		draw_interval( tl - 1 ) #draw interior ticks for each inch
		draw_line( tl, str(i) ) #draw inch line for i


ruler(30, 5)

def fun(name):
	if name.startswith('h'):
		return name #*3
print filter(fun, ['hari','hass','house'])

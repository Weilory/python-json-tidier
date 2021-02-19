import os

directory = os.path.dirname(os.path.realpath(__file__))

for path in os.listdir(directory):
	if path.endswith(".jsonpy"): 
		name = ''.join(path.split('.')[0:-1]) + '.json'
		
		with open(path, 'r') as f:
			rawstr = f.read()

		prar = []

		inquote = False
		for dd in rawstr:
			if dd == '"':
				inquote = not inquote
			if inquote:
				prar.append(dd)
			else:
				if dd not in [" ", "\t", "\n"]:
					prar.append(dd)

		rar = []
		for ii, dd in enumerate(prar):
			if not (dd == ',' and prar[ii + 1] in [']', '}']):
				rar.append(dd)

		json_str = ''.join(rar)

		nfile = open(name, 'w')
		nfile.truncate()
		nfile.write(json_str)




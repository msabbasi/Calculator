import evalidate
import re

#def parse(exp):
#    chunks = ['']

#    for character in exp:
#        if character.isdigit():
#            if chunks[-1].isdigit():   # If the last chunk is already a number
#                chunks[-1] += character  # Add onto that number
#            else:
#                chunks.append(character) # Start a new number chunk
#        elif character in '+-/*':
#            chunks.append(character)  # This doesn't account for `1 ++ 2`.

#    return chunks[1:]

def valid_syntax(string, search=re.compile(r'[^a-z0-9.\(\)\-\+\*\/]').search):
	return not bool(search(string))


def evaluate(expression, data):
	success, result = evalidate.safeeval(expression,data,safenodes=['Num','Load','Name','Expression','BinOp','Add','Mult','Sub','Div'])
	print result
	if success:
		return success, result
	else:
		if "NameError" in result:
			error = result.split('name', 1)[-1]
		elif "OverflowError" in result:
			error = "Could not compute; number too large"
		else:
			error = "invalid expression"
		return success, error

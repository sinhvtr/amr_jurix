import argparse

def create_arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-input", required=True, type=str, help="Input file")
	args = parser.parse_args()
	return args
	
if __name__ == '__main__':
	args = create_arg_parser()
	input = args.input
	
	with open(input, 'rb') as f:
		sentences = f.readlines()
	
	new_sentences = []
	
	for i in range(len(sentences)):
		sent = sentences[i][0:len(sentences[i])-5]
		new_sentences.append(sent)
	
	with open(input+'.txt', 'wb') as fout:
		for sent in new_sentences:
			fout.write(sent)
			fout.write('\n')
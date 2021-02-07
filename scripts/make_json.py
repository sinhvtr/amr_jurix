import json
import argparse
import re

def create_arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-sents", required=True, type=str, help="File with sentences")    
	parser.add_argument("-amrs", required=True, type=str, help="File with AMR linearized")
	parser.add_argument("-output", required=True, type=str, help="Output file")
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = create_arg_parser()
	sents_file = args.sents
	amrs_file = args.amrs
	output_file = args.output
	
	with open(sents_file, 'rb') as f:
		sentences = f.readlines()
	
	with open(amrs_file, 'rb') as f:
		amrs = f.readlines()
			
	pairs = []
	print len(sentences)
	print len(amrs)
	for i in range(len(sentences)):
		# print i
		d = {}
		sentences[i] = sentences[i].lower()
		sentences[i] = sentences[i].rstrip("\r\n")
		amrs[i] = amrs[i].rstrip("\r\n")
		d["amr"] = amrs[i]
		d["sent"] = sentences[i]
		pairs.append(d)
		
	with open(output_file + '.json', 'wb') as f:
		json.dump(pairs, f, indent=2)
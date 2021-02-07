import sys
sys.path.append('/home/s1720003/AMR/penman-master/')
import penman
import re
import argparse

def create_arg_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required = True, type=str, help="File with AMRs")
    parser.add_argument("-amr", default = 'linearized.txt', type=str, help="Output AMR file")
    parser.add_argument("-snt", default = 'snt.txt', type=str, help="Output text file")
    parser.add_argument("-out", type=str)
    args = parser.parse_args()
    
    return args

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = string.lower()
    return string.strip()

def read_amr(filename):
    print("Reading ", filename)

    with open(filename, "r") as f:
        lines = f.readlines()
    sentences = [sentence for sentence in lines if sentence.startswith('# ::snt')]
    # Eliminate unnecessary characters
    for i in range(0, len(sentences)):
        sentences[i] = sentences[i][8:]     
        # sentences[i] = clean_str(sentences[i])
    
    print("Number of sentences extracted: ", len(sentences))
    # Retrieve all graph object
    graphs = penman.load(filename)
    
    return graphs, sentences
    
if __name__ == '__main__':
    args = create_arg_parser()
    input_file = args.f
    amr_file = args.amr
    snt_file = args.snt
    out_file = args.out
    amrs, sents = read_amr(input_file)

    with open(snt_file, 'w') as f:
        for s in sents:
            f.write(clean_str(s))
            f.write("\n")
    print("Written to ", snt_file)

    with open(amr_file, 'w') as f:
        for amr in amrs:
            g = str(amr)
            g = g.replace('\n', '')
            g = g.replace('\t', '')
            g = ' '.join(g.split())
            f.write(str(g))
            f.write('\n')
    with open(out_file, 'w') as f:
        for amr, snt in zip(amrs, sents):
            g = str(amr)
            g = g.replace('\n', '')
            g = g.replace('\t', '')
            g = ' '.join(g.split())
            f.write(str(g))
            f.write('\t')
            f.write(snt)
            # f.write('\n')
            
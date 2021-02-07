from vocab_utils import Vocab
import argparse
import namespace_utils
import os, sys
import tensorflow as tf

def main(_):
    print(FLAGS)
    word_vocab = Vocab(FLAGS.word_vec_path, fileformat='txt2')
    print('word_vocab: {}'.format(word_vocab.word_vecs.shape))
    print(word_vocab.vocab_size)
    with open("all_words_civil.txt", "r") as f:
        civil_words = f.readlines()
    with open("all_words_civil_idx.txt", "w") as f:
        for w in civil_words:
            f.write(w + "\t" + str(word_vocab.to_index_sequence(w)) + "\n")      
    # with open("all_words_civil.txt", "r") as f:
    #     civil_words = f.readlines()
    # with open("all_words_civil_idx.txt", "w") as f:
    #     for w in civil_words:
    #         f.write(w + "\t" + str(word_vocab.to_index_sequence(w)) + "\n")            

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, help='Configuration file.')

    #os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
    #os.environ["CUDA_VISIBLE_DEVICES"]="2"

    print("CUDA_VISIBLE_DEVICES " + os.environ['CUDA_VISIBLE_DEVICES'])
    FLAGS, unparsed = parser.parse_known_args()


    if FLAGS.config_path is not None:
        print('Loading the configuration from ' + FLAGS.config_path)
        FLAGS = namespace_utils.load_namespace(FLAGS.config_path)

    sys.stdout.flush()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
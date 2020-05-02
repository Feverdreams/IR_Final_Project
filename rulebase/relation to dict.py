from collections import defaultdict
from sentpair import cdroot
import pickle


def map(trans, relations, dst):
    with open(trans, 'r') as file:

        translations = file.readlines()

    for _ in range(len(translations)):

        translations[_] = translations[_][:-1]

    rela_pairs = defaultdict(list)

    for i in range(len(relations)):

        rela_pairs[relations[i][:-1]] = translations[i].split('#')[:-1]
    #print(rela_pairs)

    out = open(dst, 'wb')

    pickle.dump(rela_pairs, out)
    out.close()

    '''
    rd = open(dst, 'rb')
    print(pickle.load(rd))
    '''

def main():
    cdroot()
    quefile = 'rela_tran_res\\FreebaseQA_fb_extract.txt'

    with open(quefile, 'r') as file:

        relations = file.readlines()

    map('rela_tran_res\\FreebaseQA_fb_human_relation.txt', relations, 'rela_tran_res\\pickle.translated_relations')


if __name__ == '__main__':
    main()
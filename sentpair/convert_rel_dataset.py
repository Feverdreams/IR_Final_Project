# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-04-17 22:47
import os

from sptool.ioutil import load_json

from sentpair import cdroot


def convert(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    dataset = load_json(src)
    with open(dst, 'w') as out:
        for each in dataset['Questions']:
            out.write(f'{each["RawQuestion"]}\t{each["Parses"][0]["InferentialChain"]}\n')


def main():
    cdroot()
    for split in ['train', 'dev', 'eval']:
        convert(f'data/FreebaseQA-{split}.json', f'data/rel/{split}.tsv')


if __name__ == '__main__':
    main()

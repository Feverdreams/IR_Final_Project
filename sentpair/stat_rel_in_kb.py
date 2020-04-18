# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-04-17 22:36
from collections import Counter

from sptool.ioutil import save_json

from sentpair import cdroot

cdroot()

stat = Counter()
with open('data/FreebaseQA_fb_extract/FreebaseQA_fb_extract.txt') as src:
    for idx, line in enumerate(src):
        line = line.strip()
        if not line:
            continue
        s, p, o = line.split('\t')
        stat[p] += 1
        if idx % 10000:
            print(f'\r{idx} {p} {len(stat)}', end='')

save_json(stat, 'data/rel.json')

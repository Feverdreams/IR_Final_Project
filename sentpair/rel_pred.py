# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-04-17 22:44
from hanlp.components.classifiers.transformer_classifier import TransformerClassifier

from sentpair import cdroot

cdroot()

classifier = TransformerClassifier()
save_dir = 'data/model/rel_albert_large'
classifier.fit('data/rel/train.tsv', 'data/rel/dev.tsv', save_dir, 'albert_xxlarge', max_length=64, epochs=10)
classifier.evaluate('data/rel/train.tsv', save_dir=save_dir)

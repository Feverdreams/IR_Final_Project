# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-04-17 22:19


def cdroot():
    """
    cd to project root, so models are saved in the root folder
    """
    import os
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    os.chdir(root)

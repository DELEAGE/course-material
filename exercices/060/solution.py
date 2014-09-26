# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 12:15:05 2014


@author: DeleageF
"""
al = ('abcdefghijklmnopqrstuvwxyz')
import itertools
l1 = (itertools.chain(*(itertools.combinations('al', x+1) for x in range(2))))
for elem in l1:
    print(l1)

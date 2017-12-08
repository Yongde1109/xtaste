# -*- coding: utf-8 -*-
#__author__ = 'wangzy'

import pandas as pd
import os
import argparse
import string

DICTIONARY = {}



def train(train_folder):

    for root, dirs, files in os.walk(train_folder):

        for file in files:
            if file.find('.xlsx') > -1:
                data = pd.read_excel(os.path.join(os.path.expanduser(root),\
                                                  file), header=None)
                for index, row in data.iterrows():
                    DICTIONARY[row[0]] = row[1]


def translate(translate_folder):

    for root, _, files in os.walk(translate_folder):

        for file in files:
            if file.find('.xlsx') > -1:

                data = pd.read_excel(os.path.join(os.path.expanduser(root), \
                                                  file), header=None)

                for index, row in data.iterrows():
                    words = row[0].split(' ')
                    results = []
                    for word in words:
                        if word in DICTIONARY:
                            results.append(DICTIONARY[word])
                        else:
                            results.append(word)
                    print(row[0] + '\t'+ ' '.join(results))



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--train", type=str,
                    help="train folder")

    parser.add_argument("--translate", type=str,
                        help="translate folder")

    args = parser.parse_args()
    train(args.train)
    translate(args.translate)

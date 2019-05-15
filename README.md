# linguistics-tools

A collection of scripts related to linguistics, language processing, and language learning that I wanted to make available.

# Treedown Parser

## Instalation

This script needs [`svgling`](https://github.com/rawlins/svgling) and [`ipython`](https://ipython.org/install.html) to work properly. They can be installed as described on their respective pages or by the following commands:

~~~~
pip install svgling
pip install ipython
~~~~

## Usage

This script accepts two file names. The first is the Treedown representation of the tree to be processed and the second is the path and filename where the svg file for the tree will be saved.

~~~~
>>> python parseTreeDown.py example-tree.txt output.svg
~~~~

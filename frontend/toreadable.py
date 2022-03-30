from colorama import Fore, Style, init
import os

if os.name == "nt":
    init(convert=True, autoreset=True)
else:
    init(convert=False, autoreset=True)


def trie_to_list(trie, prolist, depth):
    if trie == {}:
        return

    if isinstance(trie, str):
        prolist.append([])
        prolist[depth].append(trie)
        return

    for (key, value) in trie.items():
        for c in range(depth + 1):
            prolist.append([])

        prolist[depth].append(key)
        trie_to_list(value, prolist, depth + 1)


def export(trie):
    prolist = []
    trie_to_list(trie, prolist, 0)
    prolist = [x for x in prolist if x != []]
    return prolist

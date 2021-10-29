#PDB

 #shitf+alt+A - comment multiple lines

import keyword
def contains_keyword(*args):
    for item in args:
        
        if keyword.iskeyword(item):
            return True
        """ else:
            return False """

contains_keyword('mallik','import')
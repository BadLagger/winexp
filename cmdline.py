class Cmdline:
    def __init__(self, line, ckey='-'):
        self.cdict = {}
        lastkey = ''
        for el in line:
            if el[0] == ckey:
                    if len(lastkey) == 0:
                        lastkey = el.lstrip(ckey)
                    else:
                        self.cdict[lastkey] = True
                        lastkey = ''
            else:
                if len(lastkey) != 0:
                    self.cdict[lastkey] = el
                lastkey = ''
                
        if  len(lastkey) != 0:
            self.cdict[lastkey] = True
    
    def exist(self, cmd):
        return False if self.cdict.get(cmd) == None else True
    
    def get(self, cmd):
        return self.cdict.get(cmd)
        
    def number(self):
        return len(self.cdict)
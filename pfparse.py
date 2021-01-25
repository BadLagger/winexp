class Pfparser:
    def __init__(self, path):
        self.path = path
        self.vocabulary = {}
        for line in open(self.path, encoding='utf-8'):
            plist = line.split(':')
            if len(plist) > 1:
                key = plist[0].lower()
                var = plist[1].strip().strip('\n')
                self.vocabulary[key] = var
    
    def get(self, prm=''):
        if len(prm) == 0:
            return self.vocabulary
        return self.vocabulary.get(prm)
import inspect

class addscript:
    def addscript(self, item):
        script = inspect.getsource(item)
        script = script[script.index('\n'):]
        m = 100
        for a in script.split('\n'):
            if a != '':
                c = 0
                while c < len(a) and a[c] == ' ':
                    c += 1
                if c < m:
                    m = c
        script = script.replace('\n' + ' ' * m, '\n')
        if script != '':
            while script[0] == '\n':
                script = script[1:]
        item.__script__ = script
        return item
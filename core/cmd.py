def cmd(core):
    __mode__ = '>'
    __err__ = 'None'
    while core.run:
        
        if __mode__ == '>':
            __com__ = input('> ')
            if __com__.replace(' ', '') != '':
                while __com__[0] == ' ':
                    __com__ = __com__[1:]
            if __com__ == '':
                __mode__ = '<'
            else:
                try: exec(__com__)
                except BaseException as error:
                    print(f'error: {error}')
                    __err__ = error
        
        if __mode__ == '<':
            __com__ = input('< ')
            if __com__.replace(' ', '') != '':
                while __com__[0] == ' ':
                    __com__ = __com__[1:]
            if __com__ == '':
                __mode__ = '>'
            else:
                try: print(eval(__com__))
                except BaseException as error:
                    print(f'error: {error}')
                    __err__ = error
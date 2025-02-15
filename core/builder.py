block = None

def builde(__c__, script):
    
    global core
    core = __c__
    
    if script != '':
        __script__ = '    ... \n' + script
        __script__ = __script__.replace('\n', '\n    ')
        __script__ = 'class block(core.block): \n' + __script__
        __script__ = 'global block \n' + __script__
        __script__ = 'global core \n' + __script__
        if core.error_log: print(__script__)
        exec(__script__)
        block.__script__ = script
        return block()
    else:
        return core.block()
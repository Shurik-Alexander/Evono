class log():
    
    split_line  = '================================================'
    
    def __init__(self, file='log.txt', name=None):
        self.file_name = file
        self.file = open(file, 'a', encoding='utf-8')
        self.name = name
    
    def split(self):
        self.file.write(self.split_line + '\n')
        self.file.close()
        self.file = open(self.file_name, 'a', encoding='utf-8')
        
    def add(self, info):
        line = str()
        if self.name != None:
            line += f'{self.name}: '
        line += info
        self.file.write(line + '\n')
        self.file.close()
        self.file = open(self.file_name, 'a', encoding='utf-8')
    
    def error(self, info):
        line = str()
        if self.name != None:
            line += f'error {self.name}: '
        else:
            line += f'error: '
        line += info
        self.file.write(line + '\n')
        self.file.close()
        self.file = open(self.file_name, 'a', encoding='utf-8')
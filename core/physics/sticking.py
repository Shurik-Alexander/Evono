class sticking:
    def sticking(self, id):
    
        block = self.scene[id]
        
        if block.sticky == False:
            return False
        
        if block.speed_x != 0:
            return False
        
        if block.speed_y != 0:
            return False
        
        if len(self.touch_down(id)) > 0:
            return True
            
        if len(self.touch_right(id)) > 0:
            return True
    
        if len(self.touch_left(id)) > 0:
            return True
    
        if len(self.touch_up(id)) > 0:
            return True
            
        return False
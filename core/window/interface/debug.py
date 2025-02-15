def debug(physics_box, text):

    text.add('')

    id = physics_box.get(physics_box.mouse.x, physics_box.mouse.y)
        
    info = f'{physics_box.mouse.x}  {physics_box.mouse.y}'
    text.add(f'{info}')
        
    info = id
    text.add(f'id {info}')

    info = len(physics_box.scene)
    text.add(f'> {info} <')
        
    if True:
        text.add('')

        text.add(f'Дистанция:')

        info = physics_box.ray_right(physics_box.mouse.x, physics_box.mouse.y)
        text.add(f'  право {info}')
        
        info = physics_box.ray_left(physics_box.mouse.x, physics_box.mouse.y)
        text.add(f'  лево {info}')
        
        info = physics_box.ray_up(physics_box.mouse.x, physics_box.mouse.y)
        text.add(f'  верх {info}')
        
        info = physics_box.ray_down(physics_box.mouse.x, physics_box.mouse.y)
        text.add(f'  низ {info}')

    if True:
        if id != None:
            text.add('')
            
            text.add(f'Соседи:')

            info = physics_box.touch_up(id)
            text.add(f'  верх {info}')

            info = physics_box.touch_down(id)
            text.add(f'  низ {info}')

            info = physics_box.touch_right(id)
            text.add(f'  право {info}')

            info = physics_box.touch_left(id)
            text.add(f'  лево {info}')
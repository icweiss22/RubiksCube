from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    # validation
    encodedCube = Cube(parms.get('cube'))
    
    validationMessage = encodedCube.cubeValidation(parms)['status']
    if validationMessage != 'ok':
        result['status'] = validationMessage
        return result
    
    directions = parms.get('dir', None)
    if directions is None or directions == '':
        directions = 'F'
    elif not directions.isalpha() or not all(i in set('FfRrBbLlUu') for i in directions):
        result['status'] = 'error: invalid direction parameter'
        return result
    
    result['status'] = 'ok'
    result['cube'] = encodedCube.rotate(directions)
                        
    return result

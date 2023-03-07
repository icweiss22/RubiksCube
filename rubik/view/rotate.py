from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    # validation
    if Cube.cubeValidation(None,parms).get('status') != 'ok':
        return Cube.cubeValidation(None,parms)
    
    encodedCube = Cube(parms.get('cube'))
    directions = parms.get('dir', None)
    if directions is None or directions == '':
        directions = 'F'
    elif not directions.isalpha() or not all(i in set('FfRrBbLlUu') for i in directions):
        result['status'] = 'error: invalid direction parameter'
        return result
    
    result['status'] = 'ok'
    result['cube'] = encodedCube.rotate(directions)
                        
    return result

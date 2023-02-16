from rubik.model.cube import Cube
import collections

def rotate(parms):
    """Return rotated cube""" 
    result = {}
    
    # validation
    if _cubeValidation(parms).get('status') != 'ok':
        return _cubeValidation(parms)
    
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

def _cubeValidation(params):
    result = {}

    try:
        cubeParam = params.get('cube', None)
        
        # cubeParam is empty    
        if cubeParam is None:
            result['status'] = 'error: cube param is required'
            
        # cubeParam is alphanumeric
        elif not cubeParam.isalnum():
            result['status'] = 'error: cube param must be alphanumeric'
        
        # cubeParam is 54 characters
        elif len(cubeParam) != 54:
            result['status'] = 'error: there must be exactly 54 characters in the cube param'
            
        # cubeParam must have exactly 6 unique colors
        elif len(collections.Counter(cubeParam)) != 6:
            result['status'] = 'error: there must be exactly 6 different colors'
            
        # cubeParam must have unique centers (5,14,23,32,41,50), but subtract 1 bc index starts at 0
        elif len(set(cubeParam[i] for i in [4, 13, 22, 31, 40, 49])) != 6:
            result['status'] = 'error: each face center must have a unique color'
    
        # valid
        else:
            result['status'] = 'ok'
            
        return result
    except:
        
        result['status'] = 'error: unknown error. please ensure cube param is a 54-length string'

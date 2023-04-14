OFFSETS = {'f': 0, 'r': 9, 'b': 18, 'l': 27, 'u': 36, 'd': 45} # indices that the face starts at
CONNECTED = {   'f': ((42, 43, 44), (9, 12, 15), (47, 46, 45), (35, 32, 29)),   'r': ((44, 41, 38), (18, 21, 24), (53, 50, 47), (8, 5, 2)),
                'b': ((38, 37, 36), (27, 30, 33), (51, 52, 53), (17, 14, 11)),  'l': ((36, 39, 42), (0, 3, 6), (45, 48, 51), (26, 23, 20)),
                'u': ((20, 19, 18), (11, 10, 9), (2, 1, 0), (29, 28, 27)),      'd': ((6, 7, 8), (15, 16, 17), (24, 25, 26), (33, 34, 35))}
from rubik.model.constants import * # @UnusedWildImport

class Cube:
    '''
    Cube: class, instance of a state machine, maintain internal state
    Methods: __init__ - constructs cube from a serialized string
            get - yields serialized string of internal representation
            rotate - performs rotations on the cube per 'dir' key
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
        self._solution = ''
            
    def get(self):
        return self._cube
    
    def getSolution(self):
        return self._solution
    
    def setSolution(self, newSolution):
        self._solution = newSolution
        
            
    def cubeValidation(self):
        returnMessage = ''
    
        try:
            
            # cubeParam is empty    
            if self is None:
                returnMessage = 'error: cube param is required'
                
            cubeParam = self.get()
            
            # cubeParam is alphanumeric
            if not cubeParam.isalnum():
                returnMessage = 'error: cube param must be alphanumeric'
            
            # cubeParam is 54 characters
            elif len(cubeParam) != 54:
                returnMessage = 'error: there must be exactly 54 characters in the cube param'
                
            # cubeParam must have exactly 6 unique colors
            elif len(set(cubeParam)) != 6:
                returnMessage = 'error: there must be exactly 6 different colors'
                
            elif not(all(cubeParam.count(char) == 9 for char in set(cubeParam))):
                returnMessage = 'error: there must be 9 occurences of each color'
                
            # cubeParam must have unique centers (5,14,23,32,41,50), but subtract 1 bc index starts at 0
            elif len(set(cubeParam[i] for i in [4, 13, 22, 31, 40, 49])) != 6:
                returnMessage = 'error: each face center must have a unique color'
        
            # valid
            else:
                returnMessage = 'ok'
                
            return returnMessage
        except:
            return 'error: unknown error. please ensure cube param is a 54-length string'
        
    # directions parameter >= 0, [FfRrBbLlUu]
    # if recordRotation is 1, note it in the solutions
    def rotate(self, directions):
        for direction in directions:
            offset = OFFSETS[str(direction).lower()]
            clockwise = str(direction).isupper()
            self._rotateCurrentFace(offset, clockwise)
            self._rotateConnectedFaces(direction, clockwise)
            self._solution += direction
                                
        return self._cube
    
    def _rotateCurrentFace(self, offset, clockwise): # 0-5, f-r-b-l-u-d
        #save copy of current face, using offset
        c = list(self._cube)[offset:offset+9] # copy of list, shortened for brevity
        c = [c[6], c[3], c[0], c[7], c[4], c[1], c[8], c[5], c[2]]
        if not clockwise: # if counter clockwise, reverse the array
            c.reverse()
        d = list(self._cube)
        d[offset:offset+9] = c
        self._cube = ''.join(d)

        
    def _rotateConnectedFaces(self, direction, clockwise):   
        
        # turn self._matrixCube into an array
        rotatingCube = list(self._cube)
        
        connected = zip(*CONNECTED[str(direction).lower()])
        for a, b, c, d in connected:
            e = rotatingCube[a]
            # CLOCKWISE
            if clockwise:
                # move colors around
                rotatingCube[a] = rotatingCube[d]
                rotatingCube[d] = rotatingCube[c]
                rotatingCube[c] = rotatingCube[b]
                rotatingCube[b] = e
            # COUNTER CLOCKWISE
            else:
                # move colors around
                rotatingCube[a] = rotatingCube[b]
                rotatingCube[b] = rotatingCube[c]
                rotatingCube[c] = rotatingCube[d]
                rotatingCube[d] = e
                
        self._cube = ''.join(rotatingCube)
        
    def rotateWithOffset(self, offset, direction): # accepts offsets 0-3
        faces = {0: ('F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'),
                 1: ('R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u', 'D', 'd'),
                 2: ('B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u', 'D', 'd'),
                 3: ('L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u', 'D', 'd')}
    
        face_map = {'F': 0, 'f': 1, 'R': 2, 'r': 3, 'B': 4, 'b': 5, 'L': 6, 'l': 7, 'U': 8, 'u': 9, 'D': 10, 'd': 11}
        
        for char in direction:
            face = face_map[char]
            self.rotate(faces[offset][face])
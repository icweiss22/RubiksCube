import re
OFFSETS = {'f': 0, 'r': 9, 'b': 18, 'l': 27, 'u': 36} # indices that the face starts at
CONNECTED = {   'f': ((42, 43, 44), (9, 12, 15), (47, 46, 45), (35, 32, 29)),   'r': ((44, 41, 38), (18, 21, 24), (53, 50, 47), (8, 5, 2)),
                'b': ((38, 37, 36), (27, 30, 33), (51, 52, 53), (17, 14, 11)),  'l': ((36, 39, 42), (0, 3, 6), (45, 48, 51), (26, 23, 20)),
                'u': ((20, 19, 18), (11, 10, 9), (2, 1, 0), (29, 28, 27))}


class Cube:
    '''
    Cube: class, instance of a state machine, maintain internal state
    Methods: __init__ - constructs cube from a serialized string
            get - yields serialized string of internal representation
            rotate - performs rotations on the cube per 'dir' key
    '''

    def __init__(self, encodedCube):
        self._cube = encodedCube
            
    def get(self):
        return self._cube
        
    # directions parameter >= 0, [FfRrBbLlUu]
    def rotate(self, directions):
        for direction in directions:
            offset = OFFSETS[str(direction).lower()]
            clockwise = str(direction).isupper()
            self._rotateCurrentFace(offset, clockwise)
            self._rotateConnectedFaces(direction, clockwise)
                                
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
            
        
        
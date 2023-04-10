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
            
        
    def makeCrossGeneric(self):
        if not(self.get()[DTM] == self.get()[DML] == self.get()[DMR] == self.get()[DBM] == self.get()[DMM]):     # we only do generic cross to get a bottom cross in the start  
            
            while any(self.get()[DMM] != self.get()[block] for block in [UTM,UML,UMR,UBM]):
                currentDMM = self.get()[DMM]
                
                # Front
                while self.get()[UBM] != currentDMM:
                    F, f, R, r, B, b, L, l, U, u, D, d = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'
                    if any(currentDMM == self.get()[i] for i in [12,32,46]):
                        while self.get()[UBM] != currentDMM:
                            self.rotate(F)
                    elif any(currentDMM == self.get()[i] for i in [1,3,5,7]):
                        if currentDMM == self.get()[3]:
                            self.rotate(U + l)
                        else:
                            while currentDMM != self.get()[5]:
                                self.rotate(F)
                            self.rotate(u + R)
                    else:
                        break
                        
                # Right
                while self.get()[UMR] != currentDMM:
                    offset = 9
                    F, f, R, r, B, b, L, l, U, u, D, d = 'R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u', 'D', 'd'
                    if any(currentDMM == self.get()[i] for i in [5,21,50]):
                        while self.get()[UMR] != currentDMM:
                            self.rotate(F)
                    elif any(currentDMM == self.get()[i] for i in [10,12,14,16]):
                        if currentDMM == self.get()[12]:
                            self.rotate(U + l)
                        else:
                            while currentDMM != self.get()[14]:
                                self.rotate(F)
                            self.rotate(u + R)
                    else:
                        break
                
                # Back
                while self.get()[UTM] != currentDMM:
                    F, f, R, r, B, b, L, l, U, u, D, d = 'B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u', 'D', 'd'
                    if any(currentDMM == self.get()[i] for i in [14,30,52]):
                        while self.get()[UTM] != currentDMM:
                            self.rotate(F)
                    elif any(currentDMM == self.get()[i] for i in [19,21,23,25]):
                        if currentDMM == self.get()[21]:
                            self.rotate(U + l)
                        else:
                            while currentDMM != self.get()[23]:
                                self.rotate(F)
                            self.rotate(u + R)
                    else:
                        break
                        
                # Left
                while self.get()[UML] != currentDMM:
                    F, f, R, r, B, b, L, l, U, u, D, d = 'L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u', 'D', 'd'
                    if any(currentDMM == self.get()[i] for i in [3,23,48]):
                        while self.get()[UML] != currentDMM:
                            self.rotate(F)
                    elif any(currentDMM == self.get()[i] for i in [28,30,32,34]):
                        if currentDMM == self.get()[30]:
                            self.rotate(U + l)
                        else:
                            while currentDMM != self.get()[32]:
                                self.rotate(F)
                            self.rotate(u + R)
                    else:
                        break
                    
                
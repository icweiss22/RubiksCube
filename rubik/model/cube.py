import re

Front=0
Right=1
Back=2
Left=3
Up=4
Down=5
OFFSETS = {'f': 0, 'r': 1, 'b': 2, 'l': 3, 'u': 4}

# subtract 1 from numbers on slides
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
        r = list(encodedCube)
        frontFace = [[r[0], r[1], r[2]],[r[3], r[4], r[5]],[r[6], r[7], r[8]]]
        rightFace = [[r[9], r[10], r[11]],[r[12], r[13], r[14]],[r[15], r[16], r[17]]]
        backFace = [[r[18], r[19], r[20]],[r[21], r[22], r[23]],[r[24], r[25], r[26]]]
        leftFace = [[r[27], r[28], r[29]],[r[30], r[31], r[32]],[r[33], r[34], r[35]]]
        upFace = [[r[36], r[37], r[38]],[r[39], r[40], r[41]],[r[42], r[43], r[44]]]
        downFace = [[r[45], r[46], r[47]],[r[48], r[49], r[50]],[r[51], r[52], r[53]]]
        self._matrixCube = [ frontFace, rightFace, backFace, leftFace, upFace, downFace ]
        # matrix cube is a list of 6 lists, each of these 6 lists have 3 arrays, and each of these 3 arrays has 3 numbers
            
    def get(self):
        return self._cube
        
    # directions parameter >= 0, [FfRrBbLlUu]
    def rotate(self, directions):
        for direction in directions:
            offset = OFFSETS[str(direction).lower()]
            clockwise = str(direction).isupper()
            self._rotateCurrentFace(offset, clockwise)
            self._rotateConnectedFaces(direction, clockwise)
                                
        self._cube = re.sub('[^a-zA-Z]+', '', str(self._matrixCube))
        return self._cube
    
    def _rotateCurrentFace(self, offset, clockwise): # 0-5, f-r-b-l-u-d
        if clockwise:
            curr = self._matrixCube[offset] # current face, list of 3 arrays (3 numbers in each)
            curr[0] = [curr[2][0], curr[1][0], curr[0][0]]
            curr[1] = [curr[2][1], curr[1][1], curr[0][1]]
            curr[2] = [curr[2][2], curr[1][2], curr[0][2]]
        else:
            curr = self._matrixCube[offset] # current face, list of 3 arrays (3 numbers in each)
            curr[0] = [curr[0][2], curr[1][2], curr[2][2]]
            curr[1] = [curr[0][1], curr[1][1], curr[2][1]]
            curr[2] = [curr[0][0], curr[1][0], curr[2][0]]
            
        self._cube =  re.sub('[^a-zA-Z]+', '', str(self._matrixCube))

        
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
        
        '''
        if offset == 0: # front connected faces
            leftCopy = self._matrixCube[Left].copy()
            upCopy = self._matrixCube[Up].copy()
            rightCopy = self._matrixCube[Right].copy()
            downCopy = self._matrixCube[Down].copy()
        
        if clockwise:
            self._matrixCube[Up][2] = [leftCopy[2][2], leftCopy[1][2], leftCopy[0][2]]
            self._matrixCube[Right][0][0] = upCopy[2][0]
            self._matrixCube[Right][1][0] = upCopy[2][1]
            self._matrixCube[Right][2][0] = upCopy[2][2]
            self._matrixCube[Down][0] = [rightCopy[2][0], rightCopy[1][0], rightCopy[0][0]]
            self._matrixCube[Left][0][2] = downCopy[0][0]
            self._matrixCube[Left][1][2] = downCopy[0][1]
            self._matrixCube[Left][2][2] = downCopy[0][2]
        else:
            self._matrixCube[Up][2] = [rightCopy[0][0], rightCopy[1][0], rightCopy[2][0]]
            self._matrixCube[Right][0][0] = downCopy[0][2]
            self._matrixCube[Right][1][0] = downCopy[0][1]
            self._matrixCube[Right][2][0] = downCopy[0][0]
            self._matrixCube[Down][0] = [leftCopy[0][2], leftCopy[1][2], leftCopy[2][2]]
            self._matrixCube[Left][0][2] = upCopy[2][2]
            self._matrixCube[Left][1][2] = upCopy[2][1]
            self._matrixCube[Left][2][2] = upCopy[2][0]
        '''
            
        
        
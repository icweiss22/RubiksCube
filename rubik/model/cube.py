OFFSETS = {'f': 0, 'r': 9, 'b': 18, 'l': 27, 'u': 36, 'd': 45} # indices that the face starts at
CONNECTED = {   'f': ((42, 43, 44), (9, 12, 15), (47, 46, 45), (35, 32, 29)),   'r': ((44, 41, 38), (18, 21, 24), (53, 50, 47), (8, 5, 2)),
                'b': ((38, 37, 36), (27, 30, 33), (51, 52, 53), (17, 14, 11)),  'l': ((36, 39, 42), (0, 3, 6), (45, 48, 51), (26, 23, 20)),
                'u': ((20, 19, 18), (11, 10, 9), (2, 1, 0), (29, 28, 27)),      'd': ((6, 7, 8), (15, 16, 17), (24, 25, 26), (33, 34, 35))}


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
        cross = [self.get()[37], self.get()[39], self.get()[41], self.get()[43]]
        if any(i != self.get()[49] for i in cross):
            while True:
                # Front
                if self.get()[43] != self.get()[49]:
                    offset = 0
                    F, f, R, r, B, b, L, l, U, u, D, d = 'F', 'f', 'R', 'r', 'B', 'b', 'L', 'l', 'U', 'u', 'D', 'd'
                # Right
                elif self.get()[41] != self.get()[49]:
                    offset = 9
                    F, f, R, r, B, b, L, l, U, u, D, d = 'R', 'r', 'B', 'b', 'L', 'l', 'F', 'f', 'U', 'u', 'D', 'd'
                # Back
                elif self.get()[37] != self.get()[49]:
                    offset = 18
                    F, f, R, r, B, b, L, l, U, u, D, d = 'B', 'b', 'L', 'l', 'F', 'f', 'R', 'r', 'U', 'u', 'D', 'd'
                # Left
                elif self.get()[39] != self.get()[49]:
                    offset = 27
                    F, f, R, r, B, b, L, l, U, u, D, d = 'L', 'l', 'F', 'f', 'R', 'r', 'B', 'b', 'U', 'u', 'D', 'd'
                
                # Front-Up-Middle
                if self.get()[offset + 1] == self.get()[49]:
                    self.rotate(f + U + l + u)
                # Front-Left-Center
                elif self.get()[offset + 3] == self.get()[49]:
                    self.rotate(U + l + u)
                # Front-Right-Center
                elif self.get()[offset + 5] == self.get()[49]:
                    self.rotate(u + R + U)
                # Front-Center
                elif self.get()[offset + 7] == self.get()[49]:
                    self.rotate(f + u + R + U)
                # Front-Right
                elif self.get()[(offset + 12) % 36] == self.get()[49]:
                    self.rotate(f)
                # Front-Left
                elif self.get()[(offset + 32) % 36] == self.get()[49]:
                    self.rotate(F)
                # Front-Down
                elif offset == 0:
                    if self.get()[46] == self.get()[49]:
                        self.rotate(F + F)
                    if self.get()[50] == self.get()[49]:
                        self.rotate(d + F + F)
                    if self.get()[52] == self.get()[49]:
                        self.rotate(d + d + F + F)
                    if self.get()[48] == self.get()[49]:
                        self.rotate(D + F + F)
                # Right-Down
                elif offset == 9:
                    if self.get()[46] == self.get()[49]:
                        self.rotate(D + F + F)
                    if self.get()[50] == self.get()[49]:
                        self.rotate(F + F)
                    if self.get()[52] == self.get()[49]:
                        self.rotate(d + F + F)
                    if self.get()[48] == self.get()[49]:
                        self.rotate(d + d + F + F)
                # Back-Down
                elif offset == 18:
                    if self.get()[46] == self.get()[49]:
                        self.rotate(d + d + F + F)
                    if self.get()[50] == self.get()[49]:
                        self.rotate(D + F + F)
                    if self.get()[52] == self.get()[49]:
                        self.rotate(F + F)
                    if self.get()[48] == self.get()[49]:
                        self.rotate(d + F + F)
                # Left-Down
                elif offset == 27:
                    if self.get()[46] == self.get()[49]:
                        self.rotate(d + F + F)
                    if self.get()[50] == self.get()[49]:
                        self.rotate(d + d + F + F)
                    if self.get()[52] == self.get()[49]:
                        self.rotate(D + F + F)
                    if self.get()[48] == self.get()[49]:
                        self.rotate(F + F)
                        
                # Right
                if self.get()[(offset + 12) % 36] == self.get()[49]:
                    self.rotate(u + U + f + u)
                elif self.get()[(offset + 14) % 36] == self.get()[49]:
                    self.rotate(u + u + B + U)
                elif self.get()[(offset + 16) % 36] == self.get()[49]:
                    self.rotate(u + r + u + B + U)
                # Back
                elif self.get()[(offset + 21) % 36] == self.get()[49]:
                    self.rotate(u + u + U + r + u)
                elif self.get()[(offset + 23) % 36] == self.get()[49]:
                    self.rotate(u + u + u + L + U)
                elif self.get()[(offset + 25) % 36] == self.get()[49]:
                    self.rotate(u + u + b + u + L + U)
                # Left
                elif self.get()[(offset + 30) % 36] == self.get()[49]:
                    self.rotate(U + U + b + u)
                elif self.get()[(offset + 32) % 36] == self.get()[49]:
                    self.rotate(U + u + F + U)
                elif self.get()[(offset + 34) % 36] == self.get()[49]:
                    self.rotate(U + l + u + F + U)
                        
                cross = [self.get()[37], self.get()[39], self.get()[41], self.get()[43]]
                if all(i == self.get()[49] for i in cross):
                    break        
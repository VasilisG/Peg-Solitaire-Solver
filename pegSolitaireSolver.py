class Node:
    def __init__(self,matrix,parent):
        self.matrix = matrix
        self.parent = parent

    def getMatrix(self):
        return self.matrix

    def getParent(self):
        return self.parent

    def showMatrix(self):
        print("\n".join("".join(elem) for elem in self.matrix))

    def isWinningState(self):
        return "".join(list(map(lambda item: "".join(item), self.matrix))).count('X') == 1 and self.matrix[3][3] == 'X'

    def isValidMove(self, x, y):
        length = len(self.matrix)
        return (0 <= x < length) and (0 <= y < length) and (self.matrix[x][y] == 'O')

    def findAllEmptyPositions(self):
        length = len(self.matrix)
        positions = [[x,y] for x in range(length) for y in range(length) if self.matrix[x][y] == 'X']
        return positions

    def getValidMovesForPosition(self, x, y):
        validPositionNodes = []
        length = len(self.matrix)
        if self.isValidMove(x,y-2) and self.matrix[x][y-1] == 'X':
            newMatrix = [[self.matrix[i][j] for j in range(length)] for i in range(length)]
            newMatrix[x][y], newMatrix[x][y-2] = newMatrix[x][y-2], newMatrix[x][y]
            newMatrix[x][y-1] = 'O'
            node = Node(newMatrix, self)
            validPositionNodes.append(node)
        if self.isValidMove(x+2,y) and self.matrix[x+1][y] == 'X':
            newMatrix = [[self.matrix[i][j] for j in range(length)] for i in range(length)]
            newMatrix[x][y], newMatrix[x+2][y] = newMatrix[x+2][y], newMatrix[x][y]
            newMatrix[x+1][y] = 'O'
            node = Node(newMatrix, self)
            validPositionNodes.append(node)
        if self.isValidMove(x,y+2) and self.matrix[x][y+1] == 'X':
            newMatrix = [[self.matrix[i][j] for j in range(length)] for i in range(length)]
            newMatrix[x][y], newMatrix[x][y+2] = newMatrix[x][y+2], newMatrix[x][y]
            newMatrix[x][y+1] = 'O'
            node = Node(newMatrix, self)
            validPositionNodes.append(node)
        if self.isValidMove(x-2,y) and self.matrix[x-1][y] == 'X':
            newMatrix = [[self.matrix[i][j] for j in range(length)] for i in range(length)]
            newMatrix[x][y], newMatrix[x-2][y] = newMatrix[x-2][y], newMatrix[x][y]
            newMatrix[x-1][y] = 'O'
            node = Node(newMatrix, self)
            validPositionNodes.append(node)
        return validPositionNodes

    def generateChildren(self):
        children = []
        positions = self.findAllEmptyPositions()
        for position in positions:
            x = position[0]
            y = position[1]
            validPositions = self.getValidMovesForPosition(x,y)
            children.extend(validPositions)
        return children

class MatrixHelper:
    def createMatrix(self):
        matrix = [['X' for i in range(7)] for j in range(7)]
        matrix[3][3] = 'O'
        self.fixBorders(matrix)
        return matrix

    def fixBorder(self, matrix, xPos, yPos, xSize, ySize):
        for i in range(xPos, xPos + xSize):
            for j in range(yPos, yPos + ySize):
                matrix[i][j] = '-'

    def fixBorders(self, matrix):
        self.fixBorder(matrix, 0, 0, 2, 2)
        self.fixBorder(matrix, 0, 5, 2, 2)
        self.fixBorder(matrix, 5, 0, 2, 2)
        self.fixBorder(matrix, 5, 5, 2, 2)

class Solver:
    def __init__(self):
        matrixHelper = MatrixHelper()
        self.matrix = matrixHelper.createMatrix()
        self.startNode = Node(self.matrix, None)
        self.finalStateAchieved = False

    def showPath(self, endNode):
        path = []
        currentNode = endNode
        while True:
            if currentNode.getParent() is None:
                break
            else:
                path.append(currentNode)
                currentNode = currentNode.getParent()
        path = path[::-1]
        print('Total moves: ' + str(len(path)), end='\n\n')
        counter = 1
        for node in path:
            print('Step ' + str(counter) + ' :')
            node.showMatrix()
            print()
            counter += 1

    def dfs(self, node):
        if self.finalStateAchieved:
            return
        if node.isWinningState():
            print('Winning state achieved.');
            self.showPath(node)
            self.finalStateAchieved = True
        else:
            children = node.generateChildren()
            if len(children) > 0:
                for child in children:
                    self.dfs(child)

    def solve(self):
        self.dfs(self.startNode)

solver = Solver()
solver.solve()
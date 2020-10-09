# THIS IS A LINKED LIST IMPLEMENTATION

# CREATING THE NODE CLASSS

class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def setNextNode(self, nextNode):
        self.nextNode = nextNode

    def getNextNode(self):
        return self.nextNode

    def getData(self):
        return self.data

    def __str__(self):
        return "[Activity: {}]".format(self.data)


class UndoStack:
    def __init__(self, limit=1000):
        self.lastAction = None
        self.limit = limit
        self.size = 0

    def getSize(self):
        return self.size

    def hasSpace(self):
        return self.limit > self.size

    def isEmpty(self):
        return self.size == 0

    def pushToUndoStack(self, data):
        if self.hasSpace():
            newAction = Node(data)
            newAction.setNextNode(self.lastAction)
            self.lastAction = newAction
            self.size += 1
            print(f"Adding {data} to the undo stack")
        else:
            print(f"No space!! {data} was not added to the undo stack")

    def undoLastAction(self):
        if not self.isEmpty():
            actionToUndo = self.lastAction
            self.size -= 1
            print(f"Undo successful")
        else:
            ("No action to undo")

    def checkStack(self):
        if not self.isEmpty():
            return self.lastAction.getData()
        else:
            return None

    def __repr__(self):
        outputString = ""
        actionToDisplay = self.lastAction
        while actionToDisplay:
            outputString += "\n -->" + str(actionToDisplay)
            actionToDisplay = actionToDisplay.getNextNode()
        return "Stack Summary: {}\n".format(outputString)


activity = UndoStack(5)

activity.pushToUndoStack("A")
activity.pushToUndoStack("B")
activity.pushToUndoStack("C")
activity.pushToUndoStack("D")
activity.pushToUndoStack("E")
activity.pushToUndoStack("F")
activity.pushToUndoStack("G")


activity.undoLastAction()
activity.undoLastAction()
activity.undoLastAction()


print(activity)

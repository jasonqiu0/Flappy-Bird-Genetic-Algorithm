import math

"""
i0 = vertical distance of bird from top obstacle
i1 = horizontal distance of bird from obstacle
i2 = horizontal distance of bird from bottom obstacle
i3 = bias
"""
class Node:
    def __init__(self, id_number):
        self.id = id_number # i0 i1 i2 i3
        self.layer = 0 # input nodes, layer 1 = output node
        self.input_value = 0 # weighted inputs
        self.output_value = 0 
        self.connections = []

    def activate(self):
        def sigmoid(x):
            return 1/(1+math.exp(-x))
        
        if self.layer == 1: #if the layer which the node is on is in the output layer
            self.output_value = sigmoid(self.input_value) 
        """
        loop through all connection in the connections list,
        for each connection in the list, add the product of the connection's weight and node's output value
        to the input value variable of the destination node associated with the connection
        
        """
        for i in range(0, len(self.connections)): 
            self.connections[i].to_node.input_value += self.connections[i].weight * self.output_value
    
    def clone(self):
        clone = Node(self.id)
        clone.id = self.id
        clone.layer = self.layer
        return clone

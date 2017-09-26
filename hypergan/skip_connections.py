import hyperchamber as hc
import tensorflow as tf

class SkipConnections:
    """
    Skip connections allow for cross-graph connections by shape.

    For example:

    ```python
        skip_connections.set('layer_filter', net) # net is 64x64x3
        skip_connections.set('layer_filter', net2) # net2 is 128x128x3
        skip_connections.get('layer_filter', [128, 128, 3]) #returns net2
        skip_connections.get('layer_filter', [64, 64, 3]) #returns net
    ```
    """
    def __init__(self):
        self.connections = {}

    def get(self, name, shape=None):
        if shape:
            shape = [int(x) for x in shape]
        connections = hc.Config(self.connections)
        if name in connections:
            conns = connections[name]
        else:
            conns = []
        print(conns)
        for con in conns:
            if con[0] == shape:
                return con[1]
        return None

    def set(self, name, value):
        shape = value.get_shape()
        if name not in self.connections:
            self.connections[name] = []
        self.connections[name].append([[int(x) for x in shape], value])
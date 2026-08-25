import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from pyqtgraph.Qt import QtCore
import pyqtgraph.opengl as gl

if 'darwin' in sys.platform:
    fmt = QtGui.QSurfaceFormat()
    fmt.setRenderableType(fmt.RenderableType.OpenGL)
    fmt.setProfile(fmt.OpenGLContextProfile.CoreProfile)
    fmt.setVersion(4, 1)
    QtGui.QSurfaceFormat.setDefaultFormat(fmt)

app = pg.mkQApp("GLMeshItem Example")
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLMeshItem')
w.setCameraPosition(distance=40)

'''
g = gl.GLGridItem()
g.scale(2,2,1)
w.addItem(g)
'''

## Example 3:
## sphere

md = gl.MeshData.sphere(rows=10, cols=20)
m3 = gl.GLMeshItem(meshdata=md, smooth=True, color=(0.0, 0,5, 0.5, 1), shader="shaded")
w.addItem(m3)


## Example 2:
## Array of vertex positions, three per face
verts = np.empty((36, 3, 3), dtype=np.float32)
theta = np.linspace(0, 2*np.pi, 37)[:-1]
verts[:,0] = np.vstack([2*np.cos(theta), 2*np.sin(theta), [0]*36]).T
verts[:,1] = np.vstack([4*np.cos(theta+0.2), 4*np.sin(theta+0.2), [-1]*36]).T
verts[:,2] = np.vstack([4*np.cos(theta-0.2), 4*np.sin(theta-0.2), [1]*36]).T

    
## Colors are specified per-vertex
colors = np.random.random(size=(verts.shape[0], 3, 4))
colors[:, :, 0] = 0
colors[:, :, 1] = 0
colors[:, :, 2] = np.random.uniform(0.3, 1, size=(verts.shape[0], 3)) # Want Random Blues
m2 = gl.GLMeshItem(vertexes=verts, vertexColors=colors, smooth=True, shader='shaded', 
                   drawEdges=True, edgeColor=(0, 0.5, 0.5, 1))
m2.rotate(25, 0, 1, 0)
w.addItem(m2)

def update_rotation():
    m2.rotate(2, 1, 1, 1)

# TODO Make a function that upon an input, will momentarily implement these two changes, then revert back to normal.
#m2.scale(2, 2, 2)
#m3.scale(1,1,1)

timer = QtCore.QTimer()
timer.timeout.connect(update_rotation)
timer.start(16)




if __name__ == '__main__':
    pg.exec()


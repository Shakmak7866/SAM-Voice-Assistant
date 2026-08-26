import sys
import time
import math
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
w.setCameraPosition(distance=30)
w.setBackgroundColor(0.9,0.9,0.9,0.9)

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

curr_rot = 0
pulse_start = 0
pulse_peak = 0.5
is_interrupted = False

# This right here is determining the size, correct?
# Then the longer the sound, the longer the duration
pulse_dur = 0.75

def update_rotation():
    global curr_rot, pulse_start, is_interrupted

    curr_rot += 1

    elapsed = time.time() - pulse_start

    # We will replace this later with PyAudio sound
    # Have the target_peak be equal to the level of sound that is coming
    if is_interrupted:
        curr_rot += 2
        progress = elapsed / pulse_dur
        scale_factor = 1 + pulse_peak * math.sin(progress * math.pi)
        if elapsed >= pulse_dur:
            is_interrupted = False
    elif elapsed < pulse_dur:
        progress = elapsed / pulse_dur
        scale_factor = 1 + pulse_peak * math.sin(progress * math.pi)
        curr_rot += 2
    else:
        scale_factor = 1

    m2.resetTransform()
    m2.rotate(25,0,1,0)
    m2.rotate(curr_rot, 1, 1, 1)
    m2.scale(scale_factor, scale_factor, scale_factor,)

    m3.resetTransform()
    m3.scale(scale_factor, scale_factor, scale_factor,)

timer = QtCore.QTimer()
timer.timeout.connect(update_rotation)
timer.start(16)



def pulse(ev):
    global pulse_start, is_interrupted
    elapsed = time.time() - pulse_start

    if elapsed < pulse_dur and pulse_start != 0:
        is_interrupted = True
    else:
        is_interrupted = False
        pulse_start = time.time()


w.mousePressEvent = pulse


    


if __name__ == '__main__':
    pg.exec()

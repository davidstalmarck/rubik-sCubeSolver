# needs to be in same directory as quaternions.py
from quaternions import Quaternion
import numpy as np
from matplotlib import pyplot as plt

class CubeAxes(plt.Axes):
    """Axes for displaying a cube"""
    # reference face perpendicular to z at z = 1+1
    refface = np.array([[1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1], [1, 1, 1]])

    # six rotors for referential face
    rotations = [Quaternion.from_theta_vector(theta, np.array([1, 0, 0])) for theta in (np.pi/2, -np.pi/2)]
    rotations += [Quaternion.from_theta_vector(theta, np.array([0, 1, 0])) for theta in (np.pi/2, -np.pi/2)]
    rotations += [Quaternion.from_theta_vector(theta, np.array([0, 1, 0])) for theta in (np.pi, 0)]

    # temporary colours
    colours = ["white", "blue", "red", "green", "orange", "yellow"]

    def __init__(self, fig, rect=[0, 0, 1, 1], *args, **kwargs):
        kwargs.update(dict(xlim=(-2.5, 2.5), ylim=(-2.5, 2.5), frameon=False, xticks=[], yticks=[], aspect='equal'))
        super(CubeAxes, self).__init__(fig, rect, *args, **kwargs)
        self.xaxis.set_major_formatter(plt.NullFormatter())
        self.yaxis.set_major_formatter(plt.NullFormatter())

        # starting rotation
        self.current_rot = Quaternion.from_theta_vector((np.pi / 6), (1, 1, 0))

    def drawcube(self):
        """draw cube rotated by theta around vector """
        # rotate faces
        Rs = [(self.current_rot * rot).as_rotation_matrix() for rot in self.rotations]
        faces = [np.dot(self.refface, R.T) for R in Rs]

        # project faces
        faces_proj = [face[:, :2] for face in faces]
        zorder = [face[:4, 2].sum() for face in faces]

        # make polygons if not already made, in that case update them
        if not hasattr(self, '_polys'):
            self._polys = [plt.Polygon(faces_proj[i], fc=self.colours[i], alpha=0.9, zorder=zorder[i]) for i in range(6)]
            for i in range(6):
                self.add_patch(self._polys[i])

        else:
            for i in range(6):
                self._polys[i].set_xy(faces_proj[i])
                self._polys[i].set_zorder(zorder[i])
                
        self.figure.canvas.draw()


# to draw:
fig = plt.figure(figsize=(4, 4))
ax = CubeAxes(fig)
fig.add_axes(ax)
ax.drawcube()
ax.show()
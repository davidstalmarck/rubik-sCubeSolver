import numpy as np

class Quaternion:
    """ Quaternion, member of H"""
    
    def __init__(self, a):
        self.a = np.asarray(a, dtype=float)

    @classmethod
    def from_theta_vector(cls, theta, vector):
        """make quaternion from rotation angle theta and axis UNIT vector"""
        theta = np.asarray(theta)
        vector = np.asarray(vector)

        norm = np.sqrt(np.sum([k*k for k in vector]))
        a = np.concatenate([np.cos(0.5*theta)], (np.sin(0.5*theta) * vector) / norm)
        return cls(a)

    def __repr__(self):
        return self.a.__repr__()
    
    def __add__(self, q2):
        """ add self to quaternion q2"""
        return self.__class__(self.a + q2.a)

    def __sub__(self, q2):
        """subtract quaternion q2 from self"""
        return self.__class__(self.a - q2.a)

    def __mul__(self, q2):
        """multiply self with quaternion q2"""
        prods = self.a[:,None] * q2.a
        return self.__class__([ prods[0, 0] - prods[1, 1] - prods[2, 2] - prods[3, 3],
                                prods[0, 1] + prods[1, 0] + prods[2, 3] - prods[3, 2],
                                prods[0, 2] - prods[1, 3] + prods[2, 0] + prods[3, 1],
                                prods[0, 3] + prods[1, 2] - prods[2, 1] + prods[3, 0]])
    
    def __scmul__(self, lmbd):
        """multiply self with scalar lambda"""
        return self.__class__(self.a * lmbd)
    
    def __inv__(self):
        """return inverse of self"""
        fac = 1/np.sum(self.a * self.a)
        polarities = np.asarray([1, -1, -1, -1])
        return self.__class__(fac*polarities*self.a)

    def __norm__(self):
        """return euclidean norm of self"""
        return np.sqrt(np.sum(self.a * self.a))

    def __vers__(self):
        """return versor (representation scaled to norm 1) of self"""
        return self.__class__(self.a / self.__norm__())
    
    def __real__(self):
        """return float of the real part of self"""
        return float(self.a[0])
    
    def __vec__(self):
        """returns numpy array of the vector part of self"""
        return np.asarray(self.a[1:])

    def as_theta_vector(self):
        """return theta-vector representation of (normalized) self"""
        # get theta
        n = self.__norm__()
        t = 2 * np.arccos(self.a[0] / n)

        # get colinear unit vector
        v = np.array(self.a[1:], order="F", copy=True)
        v /= np.sqrt(np.sum(v ** 2, 0))

        return float(t), [float(val) for val in v]

    def as_rotation_matrix(self):
        """return the rotation matrix representation of (normalized) self"""
        t, v = self.as_theta_vector()
        c = np.cos(t)
        s = np.sin(t)

        return np.array([[v[0] * v[0] * (1.0 - c) + c, v[0] * v[1] * (1.0 - c) - v[2] * s, v[0] * v[2] * (1.0 - c) + v[1] * s],
                         [v[1] * v[0] * (1.0 - c) + v[2] * s, v[1] * v[1] * (1.0 - c) + c, v[1] * v[2] * (1.0 - c) - v[0] * s],
                         [v[2] * v[0] * (1.0 - c) - v[1] * s, v[2] * v[1] * (1.0 - c) + v[0] * s, v[2] * v[2] * (1.0 - c) + c]])


q1 = Quaternion([0, 1, 0, 0])
q2 = Quaternion([0, 0, 1, 0])
test = q1.__mul__(q2)
q3 = Quaternion([1,1,1,1]).__vers__()
# print(test.__mul__(Quaternion([0,0,0,1])))
# print(q1.__scmul__(3))
# print(q3)
print(Quaternion([1, 1, 1, 1]).__vec__())
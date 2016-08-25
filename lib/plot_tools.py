import numpy as np
import matplotlib.pyplot as plt
import seaborn
from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib.patches import FancyArrowPatch

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


def initialize_2d_plot(x_min=-1,x_max=8,y_min=-1,y_max=8):
    plot_name = plt.gca()
    plot_name.set_xlim([x_min,x_max])
    plot_name.set_ylim([y_min,y_max])
    plot_name.axhline(0, color='black')
    plot_name.axvline(0, color='black')
    return plot_name

def draw_2d_vector(np_array,plot,tail=np.array([0,0])):
    u_1 = np_array[0]
    u_2 = np_array[1]
    tail_1 = tail[0]
    tail_2 = tail[1]
    plot.arrow(tail_1,tail_2,u_1,u_2, head_width=0.25, head_length=0.25)

def draw_2d_vector_addition(np_array_1,np_array_2,plot):
    u_1 = np_array_1[0]
    u_2 = np_array_1[1]
    v_1 = np_array_2[0]
    v_2 = np_array_2[1]
    plot.arrow(0,0,u_1,u_2, head_width=0.25, head_length=0.25)    
    plot.arrow(u_1,u_2,v_1,v_2, head_width=0.25, head_length=0.25)    
    
def draw_2d_vector_multiplication(scalar,np_array,plot):
    for i in range(scalar):
        tail = i*np_array
        draw_2d_vector(np_array,plot,i*np_array)
        
def initialize_3d_plot(x_min=-1,x_max=8,y_min=-1,y_max=8,z_min=-1,z_max=8,elev=3.,azim=10):
    fig = plt.figure(figsize=(10,10))
    ax = fig.gca(projection='3d')
    ax.set_xlim(x_min,x_max)
    ax.set_ylim(y_min,y_max)
    ax.set_zlim(z_min,z_max)
    ax.set_aspect("equal")
    ax.view_init(elev=elev,azim=azim)
    return ax
    
def draw_plane(ax,x_min=-1,x_max=8,y_min=-1,y_max=8, plane='XY'):
    X = np.arange(x_min,x_max, 0.25)
    Y = np.arange(y_min,y_max, 0.25)
    X, Y = np.meshgrid(X, Y)
    ZERO = np.sqrt(0*X +  0*Y)
    if plane == 'XY':
        surf = ax.plot_wireframe(X, Y, ZERO, rstride=3, cstride=3, linewidths=.25)
    elif plane == 'XZ':
        surf = ax.plot_wireframe(X, ZERO, Y, rstride=3, cstride=3, linewidths=.25) 
    else:
        surf = ax.plot_wireframe(ZERO, X, Y, rstride=3, cstride=3, linewidths=.25) 
    
def draw_3d_vector(ax,x,y,z):
    vec = Arrow3D([0,x],[0,y],[0,z], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    ax.add_artist(vec)        
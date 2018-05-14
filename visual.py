"""
A module to allow interactive plotting in a Jupyter notebook of quantities and mesh 
associated with an ANUGA domain.
"""

import numpy as np
import matplotlib.pyplot as plt

class Jupyter_plotter:
  """
  A class to wrap ANUGA domain centroid values for stage, height, elevation
  xmomentunm and ymomentum, and triangulation information.
  """
  
  def __init__(self, domain):
    
    import matplotlib.tri as tri
    self.nodes = domain.nodes
    self.triangles = domain.triangles

    self.triang = tri.Triangulation(self.nodes[:,0], self.nodes[:,1], self.triangles)
    
    self.elev  = domain.quantities['elevation'].centroid_values
    self.depth = domain.quantities['height'].centroid_values
    self.stage = domain.quantities['stage'].centroid_values
    self.xmom  = domain.quantities['xmomentum'].centroid_values
    self.ymom  = domain.quantities['ymomentum'].centroid_values
    self.domain = domain
    
  def _make_depth_vis(self, figsize, dpi):
  
    name = self.domain.get_name()
    time = self.domain.get_time() 

    fig = plt.figure(figsize=figsize, dpi=dpi)

    plt.title('Time {0:0>4}'.format(time))
    
    self.triang.set_mask(self.depth>0.01)
    plt.tripcolor(self.triang, 
              facecolors = self.elev,
              cmap='Greys_r')
    
    self.triang.set_mask(self.depth<0.01)
    plt.tripcolor(self.triang, 
              facecolors = self.depth,
              cmap='viridis')

    plt.colorbar()
    
    return    
    
  def make_depth_png(self):

    figsize=(10,6)
    dpi = 80
    name = self.domain.get_name()
    time = self.domain.get_time()

    self._make_depth_vis(figsize,dpi);
    
    plt.savefig(name+'_{0:0>4}.png'.format(int(time)))
    plt.close()
    
    return    

  def make_depth_plot(self):
  
    figsize=(5,3)
    dpi = 80
    
    self._make_depth_vis(figsize,dpi)
    
    plt.show()
    
    return

  def make_depth_animation(domain):
    import numpy as np
    import glob
    from matplotlib import image, animation
    from matplotlib import pyplot as plt

    
    img_files = sorted(glob.glob("channel1_*.png"))

    figsize=(10,6)

    fig = plt.figure(figsize=figsize, dpi=80)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')  # so there's not a second set of axes
    im = plt.imshow(image.imread(img_files[0]))

    def init():
      im.set_data(image.imread(img_files[0]))
      return im,

    def animate(i):
      image_i=image.imread(img_files[i])
      im.set_data(image_i)
      return im,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                            frames=len(img_files), interval=200, blit=True)

    plt.close()
  
    return anim

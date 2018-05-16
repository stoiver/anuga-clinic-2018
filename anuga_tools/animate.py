"""
A module to allow interactive plotting in a Jupyter notebook of quantities and mesh 
associated with an ANUGA domain and SWW file.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

class Domain_plotter:
  """
  A class to wrap ANUGA domain centroid values for stage, height, elevation
  xmomentunm and ymomentum, and triangulation information.
  """
  
  def __init__(self, domain, plot_dir = '_plot'):
    
    self.plot_dir = plot_dir
    self.make_plot_dir()
    
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
    
  def _depth_frame(self, figsize, dpi):
 
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
    
  def save_depth_frame(self):

    figsize=(10,6)
    dpi = 80
    plot_dir = self.plot_dir
    name = self.domain.get_name()
    time = self.domain.get_time()

    self._depth_frame(figsize,dpi);
    
    if plot_dir is None:
        plt.savefig(name+'_{0:0>10}.png'.format(int(time)))
    else:
        plt.savefig(os.path.join(plot_dir, name+'_{0:0>10}.png'.format(int(time))))
    plt.close()
    
    return    

  def plot_depth_frame(self):
  
    figsize=(5,3)
    dpi = 80
    
    self._depth_frame(figsize,dpi)
    
    plt.show()
    
    return

  def make_depth_animation(self):
    import numpy as np
    import glob
    from matplotlib import image, animation
    from matplotlib import pyplot as plt

    plot_dir = self.plot_dir
    name = self.domain.get_name()
    time = self.domain.get_time() 
    
    if plot_dir is None:
        expression = name+'_*.png'
    else:
        expression = os.path.join(plot_dir, name+'_*.png')
    img_files = sorted(glob.glob(expression))

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

  def make_plot_dir(self, clobber=True):
    """
    Utility function to create a directory for storing a sequence of plot
    files, or if the directory already exists, clear out any old plots.  
    If clobber==False then it will abort instead of deleting existing files.
    """

    plot_dir = self.plot_dir
    if plot_dir is None:
      return
    else:
      import os
      if os.path.isdir(plot_dir):
          if clobber:
              os.system("rm %s/*" % plot_dir)
          else:
              raise IOError('*** Cannot clobber existing directory %s' % plot_dir)
      else:
          os.system("mkdir %s" % plot_dir)
      print "Figure files for each frame will be stored in " + plot_dir

class SWW_plotter:
  """
  A class to wrap ANUGA swwfile centroid values for stage, height, elevation
  xmomentunm and ymomentum, and triangulation information.
  """
  
  def __init__(self, swwfile = 'domain.sww'):
    
    
    import matplotlib.tri as tri
    from anuga import plot_utils
    self.p=plot_utils.get_output(swwfile)
    self.p2=plot_utils.get_centroids(p)

    self.nodes_x = p.x
    self.nodes_y = p.y
    self.triangles = p.vols

    self.triang = tri.Triangulation(self.nodes_x, self.nodes_y, self.triangles)
    
    self.elev  = p2.elev
    self.depth = p2.height
    self.stage = p2.stage
    self.xmom  = p2.xmom
    self.ymom  = p2.ymom
    self.xvel  = p2.xvel
    self.yvel  = p2.yvel
    
    self.time  = p2.time
    
    
  def _depth_frame(self, figsize, dpi, frame):
 
    name = self.p.filename
    time = self.time[frame] 

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
    
  def save_depth_frame(self, frame=-1):

    figsize=(10,6)
    dpi = 160
    name = self.p.filename
    time = self.time[frame] 

    self._depth_frame(figsize,dpi,frame);
    
    if plot_dir is None:
        plt.savefig(name+'_{0:0>10}.png'.format(int(time)))
    else:
        plt.savefig(os.path.join(plot_dir, name+'_{0:0>10}.png'.format(int(time))))
    plt.close()
    
    return    

  def plot_depth_frame(self, frame=-1):
  
    figsize=(5,3)
    dpi = 160
    
    self._depth_frame(figsize,dpi,frame)
    
    plt.show()
    
    return

  def make_depth_animation(self):
    import numpy as np
    import glob
    from matplotlib import image, animation
    from matplotlib import pyplot as plt

    
    name = self.p.filename
    time = self.time[frame]  
    
    figsize=(10,6)

    fig = plt.figure(figsize=figsize, dpi=80)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')  # so there's not a second set of axes
    
    self.plot_depth_frame(0)
    

    def init():
      im = self.plot_depth_frame(0)
      return im,

    def animate(i):
      im = self.plot_depth_frame(i)
      return im,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                            frames=len(self.time), interval=200, blit=True)

    plt.close()
  
    return anim





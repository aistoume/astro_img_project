# Astro Image Plot Package
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm

def PlotLinearImg(img):
    colormap = cm.inferno
    colormap.set_bad(color='black') # set color for NaN value to black
    plt.imshow(img, origin = 'lower', cmap = colormap)
    plt.colorbar()
    
def PlotLogImg(img):
    colormap = cm.inferno
    colormap.set_bad(color='black') # set color for NaN value to black
    plt.imshow(img, origin = 'lower', cmap = colormap, 
           norm=LogNorm(1, 3e3)) #display range from 1 to 3000 in log10 scale
    plt.colorbar()

def PlotGrayImg(img):
    plt.imshow(img, origin = 'lower', cmap = 'gray', vmin=-1, vmax=1) #display range from -1 to 1
    plt.colorbar()
    
def SubplotImg(ax, img):
    colormap = cm.inferno
    colormap.set_bad(color='black') # set color for NaN value to black
    ax.imshow(img, origin = 'lower', cmap = colormap)
    
def PlotConv2dKernels(kernels, m):
    kernel_size = len(kernels)
    for i in range(kernel_size):
        k = kernels[i].reshape(m, m)
        print(k)
        print('sum =', sum(sum(k)))
        fig = plt.figure(figsize = (6, 4))
        plt.imshow(k, origin = 'lower', cmap = 'gray', vmin=-1, vmax=1) #display range from -1 to 1
        plt.colorbar()
    
def main():
    print("Import Plot Array Img as main")
    
if __name__ == '__main__':
    main()
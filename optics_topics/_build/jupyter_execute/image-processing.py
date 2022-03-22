#!/usr/bin/env python
# coding: utf-8

# # Image Processing
# 

# ## Section table of contents
# 
# ```{tableofcontents}
# ```

# ## Set up Environment
# I suppose I better import some modules:
# * scipy
# * numpy
# * matplotlib

# In[1]:



import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from scipy import ndimage, fft


# In[3]:


from PIL import Image 
image = Image.open('../images/HNI_0079.JPG')
image


# In[4]:


print(image.size)


# In[5]:


imarray = np.asarray(image)
tint_imarray = imarray[:,:,0]
plt.imshow( tint_imarray)


# Hmmm, load

# In[6]:


im = image.load()
im[0,0]


# In[7]:


import matplotlib.image as mpimg

gehry = mpimg.imread('../images/HNI_0079.JPG')
#print(gehry)
imgplt = plt.imshow(gehry)


# Uh, let's make it gray, why not.

# In[8]:


grayimage = image.convert("L")
grayimage


# In[9]:


res = fft.fft2(grayimage)


# In[10]:


res.shape


# In[11]:


print(res)


# ## Image Data
# 

# box of numbers
# 
# ![lenna](../images/lenna.png)
# 

# ## Filters/Kernels
# 

# ## Convolution

# ## Fourier Transform

# In[ ]:





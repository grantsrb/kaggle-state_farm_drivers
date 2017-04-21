import threading
import time
import numpy as np
import scipy.misc as sci
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from multiprocessing.pool import ThreadPool

pool = ThreadPool(processes=1)

count = 1
base_time = time.time()
def fxn(count):
    for i in range(count):
        time.sleep(1)
    print(time.time()-base_time)
    return count

async = pool.apply_async(fxn,(count,))
async_result = async.get()
print(async_result)
print('hey')

#
# threads = []
# for i in range(4):
#     t = threading.Thread(target=fxn,args=(count,))
#     count+=1
#     threads.append(t)
#     t.start()
# for thread in threads:
#     thread.join()
#     print(thread)
#
#


def foo(bar, baz):
  print('hello {0}'.format(bar))
  return 'foo' + baz

pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo

print('Hey ' + str(time.time()-base_time))

return_val = async_result.get()  # get the return value from your function.
print(return_val)




# path = '../../../test_jpgs/test.jpg'
#
# def convert_images_1(paths, resize_dims, img_depth=3):
#     images = np.empty((len(paths),resize_dims[0],resize_dims[1],img_depth),dtype=np.float32)
#     for i,path in enumerate(paths):
#         img = mpimg.imread(path)
#         images[i] = sci.imresize(img, resize_dims)
#     return images
#
# def convert_images_2(paths, resize_dims, img_depth=3):
#     images = []
#     for i,path in enumerate(paths):
#         img = mpimg.imread(path)
#         images.append(sci.imresize(img, resize_dims))
#     return np.array(images,dtype=np.float32)
#
#
# base_time = time.time()
# paths = [path for i in range(40)]
# imgs = convert_images_1(paths,(110,110))
# print('execution ' + str(time.time()-base_time))
# plt.imshow(imgs[0])
# plt.show()
# base_time = time.time()
# imgs = convert_images_2(paths,(110,110))
# print('execution ' + str(time.time()-base_time))

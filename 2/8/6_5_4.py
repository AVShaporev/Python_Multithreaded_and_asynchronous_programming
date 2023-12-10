'''
В реальном использовании не стараются делать синхронизацию этапов в одной целевой задаче с повтором. В действительности стараются делать простую и прозрачную реализацию без лишних усложнений. Вот несколько примеров "боевой" реализации барьера в реальных проектах:

4. PyCUDA: барьер используется в PyCUDA для синхронизации потоков, выполняющих вычисления на графических процессорах:
'''


import pycuda.driver as cuda
import pycuda.gpuarray as gpuarray
import pycuda.autoinit
import numpy as np

def compute(array):
    block_size = (16, 16, 1)
    grid_size = ((array.shape[0] - 1) // block_size[0] + 1,
                 (array.shape[1] - 1) // block_size[1] + 1,
                 (array.shape[2] - 1) // block_size[2] + 1)
    barrier = cuda.Barrier(grid_size[0] * grid_size[1] * grid_size[2])

    kernel_code = """
        __global__ void compute_kernel(float *data, int width, int height, int depth) {
            int i = blockIdx.x * blockDim.x + threadIdx.x;
            int j = blockIdx.y * blockDim.y + threadIdx.y;
            int k = blockIdx.z * blockDim.z + threadIdx.z;
            int index = k * height * width + j * width + i;
            if (i < width && j < height && k < depth) {
                // Вычисления
            }
            __syncthreads();
            barrier.Sync();
        }
    """
    module = cuda.compiler.SourceModule(kernel_code)
    compute_kernel = module.get_function("compute_kernel")
    compute_kernel(gpuarray.to_gpu(array), np)
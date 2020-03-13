from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension
import os

# if using pip virtualenv, specify the opencv path manually
opencv_inc_dir = '/home/yiwei/project/6DOF/opencv-3.4.2/include' # directory containing OpenCV header files
opencv_lib_dir = '/home/yiwei/project/6DOF/opencv-3.4.2/lib' # directory containing OpenCV library files
conda_env = ''
#if not explicitly provided, we try to locate OpenCV in the current Conda environment
#conda_env = os.environ['CONDA_PREFIX']  # for conda environment
if len(conda_env) > 0 and len(opencv_inc_dir) == 0 and len(opencv_lib_dir) == 0:
	print("Detected active conda environment:", conda_env)
	
	opencv_inc_dir = conda_env + '/include' 
	opencv_lib_dir = conda_env + '/lib' 

	print("Assuming OpenCV dependencies in:")
	print(opencv_inc_dir)
	print(opencv_lib_dir)

if len(opencv_inc_dir) == 0:
	print("Error: You have to provide an OpenCV include directory. Edit this file.")
	exit()
if len(opencv_lib_dir) == 0:
	print("Error: You have to provide an OpenCV library directory. Edit this file.")
	exit()

setup(
	name='esac',
	ext_modules=[CppExtension(
		name='esac', 
		sources=['esac.cpp','thread_rand.cpp'],
		include_dirs=[opencv_inc_dir],
		library_dirs=[opencv_lib_dir],
		libraries=['opencv_core','opencv_calib3d'],
		extra_compile_args=['-fopenmp']
		)],		
	cmdclass={'build_ext': BuildExtension})

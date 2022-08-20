from setuptools import setup, find_packages

setup(
    name='MyPackageName',
    version='1.0.0',
    url='https://github.com/RegisAmon/violence-detection.git',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=['numpy==1.20.3' , 'pyheif==0.5.1' , 'requests==2.26.0' , 'clip-by-openai' , 'matplotlib==3.4.2' , 'torch==1.7.1' , 'whatimage==0.0.3' , 'streamlit==0.89.0' , 'Pillow==8.3.2' , 'opencv-python==4.5.3.56' , 'pyaml' , 'jupyter' ,'python-multipart'],
)

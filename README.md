# Javis Project

### Requirements
    - cuda toolkit
        $ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
        $ sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
        $ wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
        $ sudo dpkg -i cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
        $ sudo cp /var/cuda-repo-ubuntu2204-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
        $ sudo apt-get update
        $ sudo apt-get -y install cuda

    - pytorch
        $ conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia

    - scikit-learn 
        $ conda install -c anaconda scikit-learn

    - tensorflow
        $ conda install -c conda-forge tensorflow

    - pyopencl        
        $ conda install -c conda-forge pyopencl

    - opencl driver
        - prevent to "pyopencl._cl.LogicError: clGetPlatformIDs failed: PLATFORM_NOT_FOUND_KHR"
        $ sudo apt-get install -y nvidia-opencl-dev

    - ocl-icd-system: OpenCL defines an Installable Client Driver (ICD)
        - Make your system-wide implementation visible by installing ocl-icd-system conda package.    
        $ conda install -c conda-forge ocl-icd-system

    - jupyter-lab
        $ pip install jupyterlab

    - pandas
        $ conda install pandas

    - matplot
        $ conda install -c conda-forge matplotlib
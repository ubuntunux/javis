# Javis Project

### PyConsole
- Memo with Google Drive
```
자주 사용하는 파일 및 디렉토리 탭누르면 자동 완성
Shift + Space  cmd 모드 or 파이썬모드 전환
멀티쓰레드로 작업
Queue에 작업을 요청하면 진행하는 방식 ( 예를 들면 svn cleanup, svn update, svn revert 등 여러명령을 한번에 시켜놓으면 순차적으로 처리 )
Windows, Linux 모두 동일한 명령어 사용
Kivy or OpenGL Based 
함수를 wrapping하여 사용하는 방식

def dir():
if os.isWindows:
return os.system('dir')
else:
return os.system('ls')
기본적으로 python console을 그대로 사용한다
```

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
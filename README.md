# Introduction

This document provides instructions on installation of Qualisys CGM2 workflow using Project Automation Framework (PAF).
For details about CGM2 please refer to [https://pycgm2.github.io/](https://pycgm2.github.io/) .

# Requirements

- QTM version 2.17 or 2018.1 and all later versions
- No other licence required 

# Installation
There are two ways to install it. Prefered method is using Anaconda 2 environment. Other option is to install Python separately.

## Anaconda
1. Download and install the [Python3 64bit](https://www.anaconda.com/distribution/) version of Anaconda. 

2. Create a new environment that uses a 32bit Python 2.7 using the following commands in Anaconda prompt:  
    - `set CONDA_FORCE_32BIT=1`  
    - `conda create -n pycgm2 python=2.7`  
    - `activate pycgm2`  
    Just remember to set `CONDA_FORCE_32BIT=` (set empty) if you want to return to the root 64bit environment.

3. Install pyCGM2:
    - Clone  development branch of [pyCGM2 repository](https://github.com/pyCGM2/pyCGM2/tree/development).
    - Open Anaconda prompt at the local folder where pyCGM2 is cloned to and type `pip install -e .` Make sure the pycgm2 environment is active. If not, activate it by `activate pycgm2` in Anaconda prompt at the local folder where pyCGM2 is cloned to.

## Python
1. Download and install [Python 2.7.16 (32 bit)](https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi).   

2. Set enviroment path to `C:\Python27` and `C:\Python27\Scripts`:
    - Click the Windows "Start" icon, type "Environment" and select "Edit the system environment variables".
    - Click "Environment variables"
    - Select "Path" from System variables and click "Edit"
    - Add `C:\Python27` and `C:\Python27\Scripts` and click OK on all dialogs.  

3. Install pyCGM2:
    - Clone  development branch of [pyCGM2 repository](https://github.com/pyCGM2/pyCGM2/tree/development).
    - Open command prompt at the local folder where pyCGM2 is cloned to and type `pip install -e .` 

## Common steps
4. Download [Mokka](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/b-tk/Mokka-0.6.2_win64.zip):
    - Unzip Mokka and add location of Mokka.exe to "Path" environment variable.

5. Clone the PAF project from [this repository](https://github.com/qualisys/qualisys_CGM2_workflow).   
    Note: Test data are included in Data folder.



# Running the workflow from QTM

1. Open QTM
2. Open the CGM2 project created in step 5 above
3. Go to Tools > Project options > Folder options and set the path to Python. If using Anaconda select the pycgm2 environments python executable when using Anaconda (type `where python` in Anaconda prompt to locate correct Python.exe). If using stand alone python it is typically at `C:\Python27\python.exe`. 
4. Navigate to subsession in the Project data tree
5. On Details pane select desired CGM2 Model
6. Click "Start processing"

This process will sucessively:  
  - Generate session.xml
  - Export c3d files
  - Detect static and dynamic trials according the attribute *type* of the *session.xml* node : *measurement*
  - Detect events according Zeni's algorithm 
  - Automatically open Mokka for event verification
  - Export plots as pdf pages (stored at subsession folder > processed)

# Running the workflow from the command line

1. First run the workflow from QTM to make sure c3d files and session.xml have been exported.
2. Open Anaconda prompt (or Windows command prompt if using standalone python) and use 'cd' to go to [QTM project folder]\Templates\Scripts\src\CGM2
3. Start processing: `python CGM_workflow.py --working-directory "..."` (Replace ... with the complete path to the working folder in QTM, i.e. the folder where .qtm and .c3d files are located.).
4. The resulting PDF report will be stored in a subfolder of the working folder.

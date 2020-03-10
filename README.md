# Introduction

This document provides instructions on installation of Qualisys CGM2 workflow using Project Automation Framework (PAF).
For details about CGM2 please refer to [https://pycgm2.github.io/](https://pycgm2.github.io/) .

# Requirements

1. Install [Python 2.7.16 (32 bit)](https://www.python.org/ftp/python/2.7.16/python-2.7.16.msi) .
	Note: If you use Anaconda, download and install the [Python3 64bit](https://www.anaconda.com/distribution/) version.
	You need to create a new environment that uses a 32bit python 2.7 using the following commands:
		Open Anaconda Prompt and type:
			`set CONDA_FORCE_32BIT=1`
			`conda create -n pycgm2 python=2.7`
			`conda activate pycgm2`
		Just remember to set CONDA_FORCE_32BIT= (set empty) if you are going to use the root environment 64bit 

2. Set PATH to C:\Python27 and C:\Python27\Scripts
	Note: Skip this step when using Anaconda.
	
3. Install pyCGM2
   - Clone the branch [development](https://github.com/pyCGM2/pyCGM2/tree/development) of pyCGM2
   - From local folder where pyCGM2 is cloned to type  `python setup.py develop` 

4. Download [Mokka](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/b-tk/Mokka-0.6.2_win64.zip)
	- Unzip Mokka and set PATH to the .exe in environment variables
	
5. Clone the PAF project from: **CGM2 TODO!!!!!!!**
	Note: Test data are included in Data folder.

# Running the workflow

1. Open QTM
2. Select the CGM2 project created in step 5
3. Navigate to subsession.
4. On Details pane select desired CGM2 Model
5. Click "Start processing"

This process will sucessively :
  - generate session.xml
  - export c3d
  - detect static and dynamic trials according the attribute *type* of the *session.xml* node : *measurement*
  - detect event according Zeni's algorithm 
  - automatically open Mokka for event verification
  - export plots as pdf (stored at subsession folder > processed)
  

 

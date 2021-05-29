## Requisite 

- python3
- ffmpeg

- Debian/Ubuntu

```sudo apt update```

```sudo apt install ffmpeg -y```

- Centos/Fedora/Redhat

```sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm```

```sudo dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm```

```sudo dnf -y install ffmpeg``` 

- Windows

Install with choco (open powershell run as administrator):
```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))```

```choco install ffmpeg```
Or unzip ffmpeg.zip

- MACOS

Install with brew:

```brew install ffmpeg```

## Overview

Script for rotate video 180*

## Quickstart

- ```pip install -r requirements.txt```

- launch the script for create the folder

- copy your videos *.MP4 on input folder

- launch the script again for rotate videos ```python3 rotate.py```

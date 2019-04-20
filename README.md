# Intelligent Facial Recognition System

[![GitHub release](https://img.shields.io/badge/release-v2.0-brightgreen.svg)](https://github.com/nature1995/Face_Recognition_System/releases)
[![Language python](https://img.shields.io/badge/python-3.5-red.svg)](https://www.python.org)
[![Language python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org)
[![Build Status](https://travis-ci.com/nature1995/Face-Recognition-System.svg?branch=master)](https://travis-ci.com/nature1995/Face-Recognition-System)
[![License](https://img.shields.io/dub/l/vibe-d.svg)](https://opensource.org/licenses/MIT)

This is a project of the facial recognition with Movidius on RaspberryPi 3B+ platform. It also uses Django and Django REST framework which providing the web platform. The project would like to build a safety and intelligent face recognition system in AI era.

If you appreciate the content 📖, support projects visibility, give 👍| ⭐| 👏

# Compatibility
The code is tested using Tensorflow r1.7 and Movidius NCSDK2 under Debin 2018-06-27（Kernel version:4.14） with django 2.1.5 and Python 3.5 & 3.6. 

# File architecture
```
django_venv/  # django virtual env for RPI
face_recognition_model/  # Movidius NCS code     
iot_control/  # iot control code
ran-django-template/  # django platform using my own model
requirements.txt  # requirements for run the code
```

# How to run it
1. Install requirements
```
pip install -r requirements.txt
```
2. **Install Neural Compute Application Zoo**

    Method attached below.

3. **Install rpi-mjpg-streamer**

    Method attached below.

4. Run ran-django-template
```
cd ran-django-template
python manage.py runserver 0.0.0.0:8000
```

5. Run face_recognition_model
```
cd face_recognition_model
make run
```

6. Run iot_control
```
cd iot_control
python iot_controller.py
```
**Admin Account**

``` 
python manage.py createsuperuser

username: ranxiaolang
email: YOUR EMAIL  
password: ranxiaolang  
```
Access the web page though this link: http://127.0.0.1:8000/admin .  

# Real Product Images
 ![image](https://github.com/nature1995/Face_Recognition_System/raw/master/image/2.jpg)
 ![image](https://github.com/nature1995/Face_Recognition_System/raw/master/image/3.jpg)

# Requirements

* Logitech HD Webcam C270
* Micro SD Card 32G
* Raspberry Pi 3 B+
* Intel Movidius Neural Compute Stick

The code requires [Python 3.5](https://www.python.org/download/releases/3.5/) or [Python 3.6](https://www.python.org/download/releases/3.6/), [Tensorflow 1.7](https://www.tensorflow.org/install/) or later, as well as the following python libraries: 

* Pillow
* django
* django-allauth  0.37.1
* django-widget-tweaks  1.4.3
* pip  18.0
* qrcode  6.0
* setuptools  40.4.3
* djangorestframework    
* markdown            
* django-filter 

Those modules can be installed using: `pip3 install xxx` or `pip install xxx` .

**Follow How to run it**

## Neural Compute Application Zoo

This repository is a place for any interested developers to share their projects (code and Neural Network content) that make use of the Intel® Movidius™ Neural Compute Stick (Intel® Movidius™ NCS) and associated [Intel® Movidius™ Neural Compute Software Development Kit](http://www.github.com/movidius/ncsdk).

You can use the following url([NC App Zoo](https://github.com/movidius/ncappzoo)) or git command to use the ncsdk2 branch of the NC App Zoo repo:

```bash
git clone -b ncsdk2 https://github.com/movidius/ncappzoo.git
```

## Install Django and Django REST framework

pip3 -V

sudo pip3 install -U setuptools

sudo pip3 install -U django

sudo pip3 install -U djangorestframework

sudo pip3 install -U django-filter

sudo pip3 install -U markdown

sudo pip3 install -U requests

## Install Adafruit_Python_DHT library

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT

sudo python3 setup.py install

cd

## Install Adafruit_Python_BMP library

git clone https://github.com/adafruit/Adafruit_Python_BMP.git

cd Adafruit_Python_BMP

sudo python3 setup.py install

cd

## Install psutil (process and system utilities)

sudo pip3 install psutil

# Install rpi-mjpg-streamer

Instructions and helper scripts for running mjpg-streamer on Raspberry Pi.

## A. Setup mjpg-streamer

### Enable Raspberry Pi Camera module from raspi-config

```
$ sudo raspi-config
```

### Install necessary packages for mjpg-streamer

```
$ sudo apt-get update
$ sudo apt-get install build-essential libjpeg8-dev imagemagick libv4l-dev git cmake uvcdynctrl
```

### Build mjpg-streamer

```
$ sudo ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h
$ git clone https://github.com/jacksonliam/mjpg-streamer
$ cd mjpg-streamer/mjpg-streamer-experimental
$ cmake -DCMAKE_INSTALL_PREFIX:PATH=.. .
$ make install
```

## B. Run mjpg-streamer

### 1. Clone this repository

```
$ git clone https://github.com/meinside/rpi-mjpg-streamer.git
```

### 2-a. Run mjpg-streamer from the shell directly

```
# copy & edit run-mjpg-streamer.sh to your environment or needs
$ cp rpi-mjpg-streamer/run-mjpg-streamer.sh.sample somewhere/run-mjpg-streamer.sh
$ vi somewhere/run-mjpg-streamer.sh

# then run
$ somewhere/run-mjpg-streamer.sh
```

### 2-b. Or run mjpg-streamer as a service

#### systemd

```
# copy & edit systemd/mjpg-streamer.service file,
$ sudo cp rpi-mjpg-streamer/systemd/mjpg-streamer.service.sample /lib/systemd/system/mjpg-streamer.service
$ sudo vi /lib/systemd/system/mjpg-streamer.service

# then register as a service
$ sudo systemctl enable mjpg-streamer.service

# or remove it
$ sudo systemctl disable mjpg-streamer.service

# and start/stop it
$ sudo systemctl start mjpg-streamer.service
$ sudo systemctl stop mjpg-streamer.service
```

## C. Connect

Connect through the web browser:

![image](https://github.com/nature1995/Face_Recognition_System/raw/master/image/IFRS.png)

Most modern browsers(including mobile browsers like Safari and Chrome) will show the live stream immediately.

# Notice

## Virtualenv
**Method 1**
```
pip3 install virtualenv   
```
Copy django_venv and activate   
```
source venv/bin/activate    
```

**Method 2**  
```
pip install -r requirements.txt
```
## sqlite3 数据库文件db.sqlite3 权限 666

chmod 666 db.sqlite3

## django 所在文件夹 权限 775

chmod 777 xxx

# Citation

Just can be used for non-business projects. If you use ran-django-template, please give me a star. Thanks!



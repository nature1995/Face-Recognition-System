# Intelligent Face Recognition System
This is a TensorFlow project of the face recognizer with Movidius on RaspberryPi 3B+ platform. The project also uses Django and Tencent Cloud which providing the web platform. The project would like to build a safety and intelligent face recognition system in AI era.

# Compatibility
The code is tested using Tensorflow r1.7 and Movidius NCSDK2 under Debin 2018-06-27（Kernel version:4.14） with django 2.1.1 and Python 3.5. 

# Real Product Images
 ![image](https://github.com/nature1995/Face_Recognition_System/raw/master/image/2.jpg)
 ![image](https://github.com/nature1995/Face_Recognition_System/raw/master/image/1.jpg)
 ![image](https://github.com/nature1995/Face_Recognition_System/raw/master/image/3.jpg)

# Requirements

* Logitech HD Webcam C270
* Micro SD Card 32G
* Raspberry Pi 3 B+
* Intel Movidius Neural Compute Stick

The code requires [Python 3.5](https://www.python.org/download/releases/3.5/), [Tensorflow 1.7](https://www.tensorflow.org/install/), as well as the following python libraries: 

* Pillow
* django
* django-allauth  0.37.1
* django-widget-tweaks  1.4.3
* pip  18.0
* qrcode  6.0
* setuptools  40.4.3

Those modules can be installed using: `pip3 install xxx`.

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

# Notice

## Virtualenv

pip3 install virtualenv

Run Virtualenv

source venv/bin/activate

## sqlite3 数据库文件db.sqlite3 权限 666

chmod 666 db.sqlite3

## django 所在文件夹 权限 775

chmod 777 xxx

# Citation

Just can be used for non-business projects. 



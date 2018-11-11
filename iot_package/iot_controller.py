import time
import datetime
import Adafruit_DHT
import sys
import requests
import RPi.GPIO as GPIO
import sqlite3
import spidev


DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN  = 24
GPIO.setmode(GPIO.BCM)
ROOM_SENSOR_PIN = 27
DOOR_SENSOR_PIN = 23
GPIO.setup(ROOM_SENSOR_PIN, GPIO.IN)
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Initialize SQLite
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# LDR channel on MCP3008
LIGHT_CHANNEL = 0

# GPIO Setup
GPIO.setmode(GPIO.BCM)
LIGHT_PIN = 25

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 976000

# Light Level Threshold
threshold = 100



def runController():
    now = datetime.datetime.now()
    dt = now.replace(microsecond=0)
    print(dt)
    print('Temperature: {0:0.1f} C'.format(tmp))
    print('Humidity:    {0:0.1f} %'.format(hmd))
    setDtState(dt)
    setTmpState(tmp)
    setHmdState(hmd)
    roomState = readingRoomSensor()
##    currentMode = getCurrentMode()
    if roomState == 1:
        setRoomState('yes')
    else:
        setRoomState('no')
    doorState = readingDoorSensor()
    if doorState == 1:
        setDoorState('open')
    else:
        setDoorState('closed')
        

##    if currentMode == 'auto':
##        runAutoMode()
##    elif currentMode == 'manual':
##        runManualMode()
##    return True

### Function to read LDR connected to MCP3008
##def readLDR():
##    light_level = ReadChannel(LIGHT_CHANNEL)
##    if light_level == 0:
##        lux = 0
##    else:
##        lux = ConvertLux(light_level, 2)
##    return lux
##
### Function to convert LDR reading to Lux
##def ConvertLux(data, places):
##    R = 10 #10k-ohm resistor connected to LDR
##    volts = (data * 3.3) / 1023
##    volts = round(volts, places)
##    lux = 500 * (3.3 - volts) / (R * volts)
##    return lux
##
### Function to read SPI data from MCP3008 chip
##def ReadChannel(channel):
##    adc = spi.xfer2([1, (8 + channel) << 4, 0])
##    data = ((adc[1]&3) << 8) + adc[2]
##    return data
##
### Get current mode from DB
##def getCurrentMode():
##    cur.execute('SELECT * FROM myapp_mode')
##    data = cur.fetchone()  # (1, 'auto')
##    return data[1]
##
### Get current state from DB
##def getCurrentState():
##    cur.execute('SELECT * FROM myapp_state')
##    data = cur.fetchone()  # (1, 'on')
##    return data[1]
##
### Store current state in DB
##def setCurrentState(val):
##    query = 'UPDATE myapp_state set name = "'+val+'"'
##    cur.execute(query)
##
##def switchOnLight(PIN):
##    GPIO.setup(PIN, GPIO.OUT)
##    GPIO.output(PIN, True)
##
##def switchOffLight(PIN):
##    GPIO.setup(PIN, GPIO.OUT)
##    GPIO.output(PIN, False)
##
##def runManualMode():
##    # Get current state from DB
##    currentState = getCurrentState()
##    if currentState == 'on':
##        print('Manual - On')
##        switchOnLight(LIGHT_PIN)
##    elif currentState == 'off':
##        print('Manual - Off')
##        switchOffLight(LIGHT_PIN)
##
##def runAutoMode():
##    # Read LDR
##    lightlevel = readLDR()
##    if lightlevel < threshold:
##        print('Auto - On (lux=%d)' % lightlevel)
##        switchOnLight(LIGHT_PIN)
##    else:
##        print('Auto - Off (lux=%d)' % lightlevel)
##        switchOffLight(LIGHT_PIN)
        
        
        
def setDtState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/dt/1/', data=values)


def setTmpState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/tmp/1/', data=values)


def setHmdState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/hmd/1/', data=values)
########################################################################


def readingRoomSensor():
    if GPIO.input(ROOM_SENSOR_PIN):
        print('motion detected')
        return 1
    else:
        return 0


def readingDoorSensor():
    if GPIO.input(DOOR_SENSOR_PIN):
        print('door opened')
        return 1
    else:
        return 0


def setRoomState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/room/1/', data=values)


def setDoorState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/iot/rasp/door/1/', data=values)


while True:
    try:
        hmd, tmp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
        if hmd is None or tmp is None:
            time.sleep(2)
            continue
        runController()        
        time.sleep(5)
    except KeyboardInterrupt:
        spi.close()
        GPIO.cleanup()
        exit()


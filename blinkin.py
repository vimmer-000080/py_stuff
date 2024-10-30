import serial
import time

# Replace with the correct serial port (e.g., /dev/ttyACM0)
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Wait for Arduino to reset
time.sleep(2)

# Turn LED on (send '1' to the Arduino)
arduino.write(b'1')
print("LED turned ON")

# Wait for 2 seconds
time.sleep(2)

# Turn LED off (send '0' to the Arduino)
arduino.write(b'0')
print("LED turned OFF")

# Close the serial connection
arduino.close()


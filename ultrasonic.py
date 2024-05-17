import RPi.GPIO as GPIO
import time

# Set up GPIO mode and disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins
GPIO_TRIG = 16
GPIO_ECHO = 26

# Set up GPIO pins as output and input
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Ensure the trigger pin is set low initially
GPIO.output(GPIO_TRIG, GPIO.LOW)
print("Waiting for sensor to settle")
time.sleep(2)  # Wait for sensor to settle

# Function to measure distance
def measure_distance():
    # Trigger the ultrasonic sensor
    GPIO.output(GPIO_TRIG, GPIO.HIGH)
    time.sleep(0.00001)  # Send a 10 microsecond pulse
    GPIO.output(GPIO_TRIG, GPIO.LOW)

    # Record the start and stop times
    start_time = time.time()
    stop_time = time.time()

    # Wait for echo to start
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    # Wait for echo to end
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # Calculate time difference and convert to distance
    pulse_duration = stop_time - start_time
    distance = pulse_duration * 17150  # Speed of sound at room temperature (~20°C)

    return distance

try:
    while True:
        distance = measure_distance()
        print("Distance: %.2f cm" % distance)
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
finally:
    GPIO.cleanup()

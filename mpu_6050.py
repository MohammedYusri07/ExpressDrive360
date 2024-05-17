from mpu6050 import mpu6050
import time
import math

# Initialize MPU6050 sensor
mpu = mpu6050(0x68)  # Replace with your MPU6050 address if different

# Define variables for previous time and speed
prev_time = time.time()
prev_accel_x = 0

# Define threshold for minimum acceleration to consider movement
threshold_acceleration = 0.1  # Adjust as needed

while True:
    try:
        # Get current time
        curr_time = time.time()
        # Calculate time elapsed since last reading
        delta_time = curr_time - prev_time
        
        # Retrieve accelerometer data
        accel_data = mpu.get_accel_data()
        # Acceleration in X-axis (m/s^2)
        accel_x = accel_data['x']
        # Calculate total acceleration magnitude
        acceleration_magnitude = math.sqrt(accel_data['x'] ** 2 + accel_data['y'] ** 2 + accel_data['z'] ** 2)
        
        # Check if total acceleration exceeds threshold
        if acceleration_magnitude > threshold_acceleration:
            # Calculate speed using the current acceleration
            # Speed (m/s) = Current acceleration * Time interval
            speed = accel_x * delta_time
            
            # Update previous acceleration for next iteration
            prev_accel_x = accel_x
            
            # Print speed and acceleration in X-axis
            print("Speed: {:.2f} m/s".format(speed))
            print("Acceleration (X-axis): {:.2f} m/s^2".format(accel_x))
            print("-----------------------------")
        
        # Update previous time for next iteration
        prev_time = curr_time
        
        # Wait for 0.1 second (adjust as needed)
        time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("Exiting...")
        break
    except Exception as e:
        print("Error:", e)
from mpu6050 import mpu6050
import time
import math

# Initialize MPU6050 sensor
mpu = mpu6050(0x68)  # Replace with your MPU6050 address if different

# Define variables for previous time, initial movement detection, and initial values
prev_time = time.time()
is_moving_y = False
is_moving_x = False

# Initialize speeds
current_speed_y = 0.0
current_speed_x = 0.0

# Define thresholds for minimum accelerations along the y and x axes to consider movement
threshold_acceleration_y = 0.1  # Adjust as needed
threshold_acceleration_x = 0.1  # Adjust as needed

while True:
    try:
        # Get current time
        curr_time = time.time()
        # Calculate time elapsed since last reading
        delta_time = curr_time - prev_time
        
        # Retrieve accelerometer data
        accel_data = mpu.get_accel_data()
        # Acceleration in Y-axis (m/s^2)
        accel_y = accel_data['y']
        # Acceleration in X-axis (m/s^2) - interchanged direction
        accel_x = -accel_data['x']
        
        # Check if acceleration along y-axis exceeds threshold
        if accel_y > threshold_acceleration_y:
            is_moving_y = True
        else:
            is_moving_y = False
        
        # Check if acceleration along x-axis exceeds threshold
        if accel_x > threshold_acceleration_x:
            is_moving_x = True
        else:
            is_moving_x = False
        
        # If the sensor is moving in the +y direction, calculate and print speed
        if is_moving_y:
            # Calculate speed change using the current acceleration
            speed_change_y = accel_y * delta_time
            
            # Update current speed
            current_speed_y += speed_change_y
            
            # Ensure the speed doesn't go below 0
            if current_speed_y < 0:
                current_speed_y = 0.0
            
            # Convert speed to km/h
            speed_kmh_y = current_speed_y * 3.6
            
            # Print speed and acceleration in Y-axis
            print("Speed (Y-axis): {:.2f} km/h".format(speed_kmh_y))
            print("Acceleration (Y-axis): {:.2f} m/s^2".format(accel_y))
            print("-----------------------------")
        else:
            # Decelerate if the sensor is not moving in the +y direction
            if current_speed_y > 0:
                # Assuming a deceleration factor (can be adjusted)
                deceleration_y = 0.5 * delta_time  # Adjust as needed
                current_speed_y -= deceleration_y
                if current_speed_y < 0:
                    current_speed_y = 0.0
                
                # Print deceleration in Y-axis
                print("Speed (Y-axis): {:.2f} km/h".format(current_speed_y * 3.6))
                print("Deceleration (Y-axis): {:.2f} m/s^2".format(deceleration_y))
                print("-----------------------------")
            else:
                print("Speed (Y-axis): 0.00 km/h")
                print("Acceleration (Y-axis): 0.00 m/s^2")
                print("-----------------------------")
        
        # If the sensor is moving in the +x direction, calculate and print speed
        if is_moving_x:
            # Calculate speed change using the current acceleration
            speed_change_x = accel_x * delta_time
            
            # Update current speed
            current_speed_x += speed_change_x
            
            # Ensure the speed doesn't go below 0
            if current_speed_x < 0:
                current_speed_x = 0.0
            
            # Convert speed to km/h
            speed_kmh_x = current_speed_x * 3.6
            
            # Print speed and acceleration in X-axis
            print("Speed (X-axis): {:.2f} km/h".format(speed_kmh_x))
            print("Acceleration (X-axis): {:.2f} m/s^2".format(accel_x))
            print("-----------------------------")
        else:
            # Decelerate if the sensor is not moving in the +x direction
            if current_speed_x > 0:
                # Assuming a deceleration factor (can be adjusted)
                deceleration_x = 0.5 * delta_time  # Adjust as needed
                current_speed_x -= deceleration_x
                if current_speed_x < 0:
                    current_speed_x = 0.0
                
                # Print deceleration in X-axis
                print("Speed (X-axis): {:.2f} km/h".format(current_speed_x * 3.6))
                print("Deceleration (X-axis): {:.2f} m/s^2".format(deceleration_x))
                print("-----------------------------")
            else:
                print("Speed (X-axis): 0.00 km/h")
                print("Acceleration (X-axis): 0.00 m/s^2")
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

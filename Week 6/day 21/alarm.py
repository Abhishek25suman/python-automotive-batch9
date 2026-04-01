import random
import time

speed_limit = 60    
is_speeding = False  # To track if the alert is active

def get_speed():
    # Gets a random number for speed
    return random.uniform(30, 100)

while True:
    speed = get_speed()
    print(f"Speed: {speed:.1f} km/h")
    
    # Check if speed is too high
    if speed > speed_limit:
        
        # Check if we should trigger the alert
        if not is_speeding:
            print("Alarm: !!! TOO FAST !!!")
            
            is_speeding = True
            break  
        
    time.sleep(1)  # Wait 1 second
    
print("Message: STOP! Speed limit hit.")
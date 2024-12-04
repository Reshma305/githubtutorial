import RPi.GPIO as GPIO

# Pin setup
SERVO_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Initialize PWM
servo = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz
servo.start(0)

def move_arm(angle):
    """Move robotic arm to a specified angle."""
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    servo.ChangeDutyCycle(duty)
    GPIO.output(SERVO_PIN, False)
    servo.ChangeDutyCycle(0)

# Example: Move to 90 degrees
move_arm(90)

# Cleanup
servo.stop()
GPIO.cleanup()

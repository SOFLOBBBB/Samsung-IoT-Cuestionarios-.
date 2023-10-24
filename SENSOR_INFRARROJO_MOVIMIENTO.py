from gpiozero import MotionSensor
import time

pir = MotionSensor(4)
print("Waiting for PIR to settle")
pir.wait_for_no_motion()
while True:
    print("Ready")
    pir.wait_for_motion()
    print("Motion detected!")
    time.sleep(1)

from src.waste_detection import classify_waste
from src.weight_sensor import get_weight
from src.bag_dispenser import dispense_bag

def main():
    print("Smart Litter Dispenser Initialized.")
    while True:
        waste_type = classify_waste("datasets/images/live_waste.jpg")
        weight = get_weight()
        if waste_type == "Non-Biodegradable" and weight > 0:
            print(f"Detected {waste_type}. Dispensing bag...")
            dispense_bag(weight)
        else:
            print(f"Detected {waste_type}. No action required.")

if __name__ == "__main__":
    main()

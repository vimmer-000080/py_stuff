import random
import time
import threading


class Bus:
    """My name is bus I love to take a shit"""

    def __init__(self, route_no, origin, destination, distance_read):
        self.route_no = route_no
        self.origin = origin
        self.destination = destination
        self.speed = 0
        self.average_speed = 0
        self.distance = 0
        self.distance_read = distance_read

    def simulate_bus_speed(self, duration):
        # Speed in kilometers per hour
        speed = 0
        max_speed = 60
        time_step = 1  # Time step in seconds

        sum_of_speed = 0
        for _ in range(duration):
            # Generate random acceleration or deceleration
            acceleration = random.gauss(
                0, 2
            )  # Random acceleration/deceleration between -2 and 2 km/h per second
            acceleration *= 2

            # Ensure speed stays within limits
            speed = max(0, min(max_speed, speed + acceleration))

            # print(f"Bus Speed: {speed:.3f} km/h")
            time.sleep(time_step)
            sum_of_speed += speed
        self.average_speed = sum_of_speed / duration
        self.distance = 3 * self.average_speed  # Updating distance

    def distance_covered(self):
        # Gives the distance covered by Bus using simple x = vt relation
        # Reminding that the time for each Bus demo is 3s
        # So, x = 3*simulate_bus_speed(self, 3)

        distance = 3 * self.average_speed
        return distance

    def ETA(self):
        # ETA refers to the estimated time of arrival of the bus
        # Here we consider the Bus stop to be the last station/stop
        # So ETA will be (remaining distance)/(average speed)
        try:
            estimated_time = (self.distance_read - self.distance) / self.average_speed
            return estimated_time
        except:
            return 10


# Function to create Bus objects from CSV using Pandas
def create_buses_from_csv(csv_file):
    buses = []
    df = pandas.read_csv(csv_file)  # Read CSV into Pandas DataFrame
    for index, row in df.iterrows():
        bus = Bus(
            row["route_no"],
            row["origin"],
            row["destination"],
            float(row["distance"].replace("KM", "").strip()),
        )
        buses.append(bus)
    return buses


def simulate_buses(buses, duration):
    threads = []
    for bus in buses:
        thread = threading.Thread(target=bus.simulate_bus_speed, args=(duration,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# Usage
csv_file = "bmtc_dump.csv"  # Replace with your CSV file path
buses = create_buses_from_csv(csv_file)
simulate_buses(buses, 3)  # Assuming a duration of 3 seconds for simulation

# Printing distance covered and ETA for each bus
for bus in buses:
    print(
        f"Bus {bus.route_no}: Distance Covered: {round(bus.distance_covered(), 3)} km, ETA: {abs(round(bus.ETA(), 2))	} minutes"
    )
    time.sleep(0.5)


# This funciton will spit out Fibonacci numbers
#
def Fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)


def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)

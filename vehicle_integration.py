import json
import subprocess
import os
from datetime import datetime
from typing import Dict, List, Optional

class VehicleIntegration:
    """Python integration layer for COBOL Vehicle System"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.vehicle_file = os.path.join(data_dir, "vehicles.json")
        self.cobol_input = os.path.join(data_dir, "cobol_input.dat")
        self.cobol_output = os.path.join(data_dir, "cobol_output.dat")
    
    def create_vehicle(self, vehicle_data: Dict) -> Dict:
        """Create vehicle record for COBOL processing"""
        vehicle = {
            "id": vehicle_data.get("id"),
            "brand": vehicle_data.get("brand"),
            "model": vehicle_data.get("model"),
            "year": vehicle_data.get("year"),
            "color": vehicle_data.get("color", ""),
            "price": vehicle_data.get("price", 0.0),
            "timestamp": datetime.now().isoformat()
        }
        return vehicle
    
    def create_car(self, car_data: Dict) -> Dict:
        """Create car record extending vehicle"""
        car = self.create_vehicle(car_data)
        car.update({
            "type": "car",
            "doors": car_data.get("doors", 4),
            "fuel_type": car_data.get("fuel_type", "Petrol"),
            "transmission": car_data.get("transmission", "Manual"),
            "mileage": car_data.get("mileage", 0)
        })
        return car
    
    def create_truck(self, truck_data: Dict) -> Dict:
        """Create truck record extending vehicle"""
        truck = self.create_vehicle(truck_data)
        truck.update({
            "type": "truck",
            "capacity": truck_data.get("capacity", 0),
            "axles": truck_data.get("axles", 2),
            "cargo_type": truck_data.get("cargo_type", "General"),
            "weight": truck_data.get("weight", 0)
        })
        return truck
    
    def create_motorcycle(self, bike_data: Dict) -> Dict:
        """Create motorcycle record extending vehicle"""
        bike = self.create_vehicle(bike_data)
        bike.update({
            "type": "motorcycle",
            "engine_cc": bike_data.get("engine_cc", 0),
            "bike_type": bike_data.get("bike_type", "Standard")
        })
        return bike
    
    def save_vehicles(self, vehicles: List[Dict]) -> None:
        """Save vehicles to JSON file"""
        with open(self.vehicle_file, 'w') as f:
            json.dump(vehicles, f, indent=2)
        print(f"Saved {len(vehicles)} vehicles to {self.vehicle_file}")
    
    def load_vehicles(self) -> List[Dict]:
        """Load vehicles from JSON file"""
        if os.path.exists(self.vehicle_file):
            with open(self.vehicle_file, 'r') as f:
                return json.load(f)
        return []
    
    def export_to_cobol_format(self, vehicle: Dict) -> str:
        """Export vehicle data in COBOL-compatible format"""
        lines = []
        lines.append(f"{vehicle['id']:05d}")
        lines.append(f"{vehicle['brand']:<20}")
        lines.append(f"{vehicle['model']:<20}")
        lines.append(f"{vehicle['year']:04d}")
        
        if vehicle.get('type') == 'car':
            lines.append(f"CAR")
            lines.append(f"{vehicle['doors']:01d}")
            lines.append(f"{vehicle['fuel_type']:<10}")
        elif vehicle.get('type') == 'truck':
            lines.append(f"TRUCK")
            lines.append(f"{vehicle['capacity']:05d}")
            lines.append(f"{vehicle['axles']:01d}")
        
        return "\n".join(lines)
    
    def write_cobol_input(self, vehicles: List[Dict]) -> None:
        """Write input file for COBOL program"""
        with open(self.cobol_input, 'w') as f:
            for vehicle in vehicles:
                f.write(self.export_to_cobol_format(vehicle) + "\n")
        print(f"Written COBOL input to {self.cobol_input}")
    
    def get_vehicle_stats(self, vehicles: List[Dict]) -> Dict:
        """Calculate statistics from vehicle data"""
        stats = {
            "total": len(vehicles),
            "cars": sum(1 for v in vehicles if v.get('type') == 'car'),
            "trucks": sum(1 for v in vehicles if v.get('type') == 'truck'),
            "motorcycles": sum(1 for v in vehicles if v.get('type') == 'motorcycle'),
            "avg_year": sum(v['year'] for v in vehicles) / len(vehicles) if vehicles else 0
        }
        return stats

def main():
    integration = VehicleIntegration()
    
    # Create sample vehicles
    vehicles = []
    
    car1 = integration.create_car({
        "id": 10001,
        "brand": "Toyota",
        "model": "Camry",
        "year": 2024,
        "color": "Silver",
        "price": 35000.00,
        "doors": 4,
        "fuel_type": "Petrol",
        "transmission": "Automatic"
    })
    vehicles.append(car1)
    
    truck1 = integration.create_truck({
        "id": 10002,
        "brand": "Ford",
        "model": "F-150",
        "year": 2024,
        "color": "Blue",
        "price": 45000.00,
        "capacity": 5000,
        "axles": 2,
        "cargo_type": "General"
    })
    vehicles.append(truck1)
    
    bike1 = integration.create_motorcycle({
        "id": 10003,
        "brand": "Yamaha",
        "model": "R15",
        "year": 2023,
        "color": "Red",
        "price": 8000.00,
        "engine_cc": 155,
        "bike_type": "Sport"
    })
    vehicles.append(bike1)
    
    # Save and display
    integration.save_vehicles(vehicles)
    integration.write_cobol_input(vehicles)
    
    stats = integration.get_vehicle_stats(vehicles)
    print("\n=== Vehicle Statistics ===")
    print(f"Total Vehicles: {stats['total']}")
    print(f"Cars: {stats['cars']}")
    print(f"Trucks: {stats['trucks']}")
    print(f"Motorcycles: {stats['motorcycles']}")
    print(f"Average Year: {stats['avg_year']:.0f}")

if __name__ == "__main__":
    main()

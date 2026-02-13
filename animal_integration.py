import json
import subprocess
import os
from typing import Dict, List, Optional
from datetime import datetime

class AnimalIntegration:
    """Python integration layer for Java Animal System"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.animal_file = os.path.join(data_dir, "animals.json")
        self.java_input = os.path.join(data_dir, "java_input.json")
        self.java_output = os.path.join(data_dir, "java_output.json")
    
    def create_animal(self, animal_data: Dict) -> Dict:
        """Create base animal record"""
        animal = {
            "name": animal_data.get("name"),
            "age": animal_data.get("age"),
            "species": animal_data.get("species"),
            "created_at": datetime.now().isoformat()
        }
        return animal
    
    def create_dog(self, dog_data: Dict) -> Dict:
        """Create dog record extending animal"""
        dog = self.create_animal(dog_data)
        dog.update({
            "type": "dog",
            "breed": dog_data.get("breed"),
            "trained": dog_data.get("trained", False),
            "sound": "Woof! Woof!"
        })
        return dog
    
    def create_cat(self, cat_data: Dict) -> Dict:
        """Create cat record extending animal"""
        cat = self.create_animal(cat_data)
        cat.update({
            "type": "cat",
            "indoor": cat_data.get("indoor", True),
            "lives_left": cat_data.get("lives_left", 9),
            "sound": "Meow!"
        })
        return cat
    
    def create_bird(self, bird_data: Dict) -> Dict:
        """Create bird record extending animal"""
        bird = self.create_animal(bird_data)
        bird.update({
            "type": "bird",
            "wing_span": bird_data.get("wing_span", 0.0),
            "can_fly": bird_data.get("can_fly", True),
            "sound": "Chirp! Chirp!"
        })
        return bird
    
    def save_animals(self, animals: List[Dict]) -> None:
        """Save animals to JSON file"""
        with open(self.animal_file, 'w') as f:
            json.dump(animals, f, indent=2)
        print(f"Saved {len(animals)} animals to {self.animal_file}")
    
    def load_animals(self) -> List[Dict]:
        """Load animals from JSON file"""
        if os.path.exists(self.animal_file):
            with open(self.animal_file, 'r') as f:
                return json.load(f)
        return []
    
    def export_to_java_format(self, animals: List[Dict]) -> None:
        """Export animal data for Java processing"""
        java_data = {
            "animals": animals,
            "timestamp": datetime.now().isoformat(),
            "count": len(animals)
        }
        with open(self.java_input, 'w') as f:
            json.dump(java_data, f, indent=2)
        print(f"Exported to Java format: {self.java_input}")
    
    def simulate_animal_action(self, animal: Dict, action: str) -> str:
        """Simulate animal actions"""
        name = animal['name']
        animal_type = animal.get('type', 'animal')
        
        actions = {
            "eat": f"{name} is eating",
            "sleep": f"{name} is sleeping",
            "sound": f"{name} says: {animal.get('sound', 'Unknown')}",
            "bark": f"{name} is barking" if animal_type == "dog" else None,
            "meow": f"{name} is meowing" if animal_type == "cat" else None,
            "fly": f"{name} is flying" if animal_type == "bird" else None
        }
        
        return actions.get(action, f"{name} performs {action}")
    
    def get_animal_stats(self, animals: List[Dict]) -> Dict:
        """Calculate statistics from animal data"""
        stats = {
            "total": len(animals),
            "dogs": sum(1 for a in animals if a.get('type') == 'dog'),
            "cats": sum(1 for a in animals if a.get('type') == 'cat'),
            "birds": sum(1 for a in animals if a.get('type') == 'bird'),
            "avg_age": sum(a['age'] for a in animals) / len(animals) if animals else 0
        }
        return stats
    
    def filter_by_type(self, animals: List[Dict], animal_type: str) -> List[Dict]:
        """Filter animals by type"""
        return [a for a in animals if a.get('type') == animal_type]
    
    def find_by_name(self, animals: List[Dict], name: str) -> Optional[Dict]:
        """Find animal by name"""
        for animal in animals:
            if animal['name'].lower() == name.lower():
                return animal
        return None

def main():
    integration = AnimalIntegration()
    
    # Create sample animals
    animals = []
    
    dog1 = integration.create_dog({
        "name": "Buddy",
        "age": 3,
        "species": "Canine",
        "breed": "Golden Retriever",
        "trained": True
    })
    animals.append(dog1)
    
    cat1 = integration.create_cat({
        "name": "Whiskers",
        "age": 2,
        "species": "Feline",
        "indoor": True,
        "lives_left": 9
    })
    animals.append(cat1)
    
    bird1 = integration.create_bird({
        "name": "Tweety",
        "age": 1,
        "species": "Avian",
        "wing_span": 15.5,
        "can_fly": True
    })
    animals.append(bird1)
    
    # Save and display
    integration.save_animals(animals)
    integration.export_to_java_format(animals)
    
    print("\n=== Animal Actions ===")
    for animal in animals:
        print(integration.simulate_animal_action(animal, "sound"))
        print(integration.simulate_animal_action(animal, "eat"))
    
    stats = integration.get_animal_stats(animals)
    print("\n=== Animal Statistics ===")
    print(f"Total Animals: {stats['total']}")
    print(f"Dogs: {stats['dogs']}")
    print(f"Cats: {stats['cats']}")
    print(f"Birds: {stats['birds']}")
    print(f"Average Age: {stats['avg_age']:.1f}")

if __name__ == "__main__":
    main()

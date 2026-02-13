import json
import subprocess
import os
import math
from typing import Dict, List, Optional, Tuple
from datetime import datetime

class ShapeIntegration:
    """Python integration layer for C++ Shape System"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.shape_file = os.path.join(data_dir, "shapes.json")
        self.cpp_input = os.path.join(data_dir, "cpp_input.dat")
        self.cpp_output = os.path.join(data_dir, "cpp_output.dat")
    
    def create_shape(self, shape_data: Dict) -> Dict:
        """Create base shape record"""
        shape = {
            "color": shape_data.get("color"),
            "name": shape_data.get("name"),
            "created_at": datetime.now().isoformat()
        }
        return shape
    
    def create_circle(self, circle_data: Dict) -> Dict:
        """Create circle record extending shape"""
        circle = self.create_shape(circle_data)
        radius = circle_data.get("radius", 0.0)
        circle.update({
            "type": "circle",
            "radius": radius,
            "area": math.pi * radius * radius,
            "perimeter": 2 * math.pi * radius
        })
        return circle
    
    def create_rectangle(self, rect_data: Dict) -> Dict:
        """Create rectangle record extending shape"""
        rectangle = self.create_shape(rect_data)
        length = rect_data.get("length", 0.0)
        width = rect_data.get("width", 0.0)
        rectangle.update({
            "type": "rectangle",
            "length": length,
            "width": width,
            "area": length * width,
            "perimeter": 2 * (length + width),
            "is_square": length == width
        })
        return rectangle
    
    def create_triangle(self, tri_data: Dict) -> Dict:
        """Create triangle record extending shape"""
        triangle = self.create_shape(tri_data)
        s1 = tri_data.get("side1", 0.0)
        s2 = tri_data.get("side2", 0.0)
        s3 = tri_data.get("side3", 0.0)
        s = (s1 + s2 + s3) / 2
        area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
        triangle.update({
            "type": "triangle",
            "side1": s1,
            "side2": s2,
            "side3": s3,
            "area": area,
            "perimeter": s1 + s2 + s3
        })
        return triangle
    
    def save_shapes(self, shapes: List[Dict]) -> None:
        """Save shapes to JSON file"""
        with open(self.shape_file, 'w') as f:
            json.dump(shapes, f, indent=2)
        print(f"Saved {len(shapes)} shapes to {self.shape_file}")
    
    def load_shapes(self) -> List[Dict]:
        """Load shapes from JSON file"""
        if os.path.exists(self.shape_file):
            with open(self.shape_file, 'r') as f:
                return json.load(f)
        return []
    
    def export_to_cpp_format(self, shape: Dict) -> str:
        """Export shape data in C++ compatible format"""
        lines = []
        lines.append(f"{shape['type'].upper()}")
        lines.append(f"{shape['color']}")
        
        if shape['type'] == 'circle':
            lines.append(f"{shape['radius']:.2f}")
        elif shape['type'] == 'rectangle':
            lines.append(f"{shape['length']:.2f}")
            lines.append(f"{shape['width']:.2f}")
        elif shape['type'] == 'triangle':
            lines.append(f"{shape['side1']:.2f}")
            lines.append(f"{shape['side2']:.2f}")
            lines.append(f"{shape['side3']:.2f}")
        
        return "\n".join(lines)
    
    def write_cpp_input(self, shapes: List[Dict]) -> None:
        """Write input file for C++ program"""
        with open(self.cpp_input, 'w') as f:
            for shape in shapes:
                f.write(self.export_to_cpp_format(shape) + "\n")
        print(f"Written C++ input to {self.cpp_input}")
    
    def calculate_total_area(self, shapes: List[Dict]) -> float:
        """Calculate total area of all shapes"""
        return sum(shape.get('area', 0.0) for shape in shapes)
    
    def calculate_total_perimeter(self, shapes: List[Dict]) -> float:
        """Calculate total perimeter of all shapes"""
        return sum(shape.get('perimeter', 0.0) for shape in shapes)
    
    def get_shape_stats(self, shapes: List[Dict]) -> Dict:
        """Calculate statistics from shape data"""
        stats = {
            "total": len(shapes),
            "circles": sum(1 for s in shapes if s.get('type') == 'circle'),
            "rectangles": sum(1 for s in shapes if s.get('type') == 'rectangle'),
            "triangles": sum(1 for s in shapes if s.get('type') == 'triangle'),
            "total_area": self.calculate_total_area(shapes),
            "total_perimeter": self.calculate_total_perimeter(shapes)
        }
        return stats
    
    def filter_by_color(self, shapes: List[Dict], color: str) -> List[Dict]:
        """Filter shapes by color"""
        return [s for s in shapes if s['color'].lower() == color.lower()]
    
    def find_largest_area(self, shapes: List[Dict]) -> Optional[Dict]:
        """Find shape with largest area"""
        if not shapes:
            return None
        return max(shapes, key=lambda s: s.get('area', 0.0))

def main():
    integration = ShapeIntegration()
    
    # Create sample shapes
    shapes = []
    
    circle1 = integration.create_circle({
        "color": "Red",
        "name": "Circle",
        "radius": 5.0
    })
    shapes.append(circle1)
    
    rect1 = integration.create_rectangle({
        "color": "Blue",
        "name": "Rectangle",
        "length": 4.0,
        "width": 6.0
    })
    shapes.append(rect1)
    
    tri1 = integration.create_triangle({
        "color": "Green",
        "name": "Triangle",
        "side1": 3.0,
        "side2": 4.0,
        "side3": 5.0
    })
    shapes.append(tri1)
    
    # Save and display
    integration.save_shapes(shapes)
    integration.write_cpp_input(shapes)
    
    print("\n=== Shape Details ===")
    for shape in shapes:
        print(f"{shape['type'].title()}: {shape['color']}")
        print(f"  Area: {shape['area']:.2f}")
        print(f"  Perimeter: {shape['perimeter']:.2f}")
    
    stats = integration.get_shape_stats(shapes)
    print("\n=== Shape Statistics ===")
    print(f"Total Shapes: {stats['total']}")
    print(f"Circles: {stats['circles']}")
    print(f"Rectangles: {stats['rectangles']}")
    print(f"Triangles: {stats['triangles']}")
    print(f"Total Area: {stats['total_area']:.2f}")
    print(f"Total Perimeter: {stats['total_perimeter']:.2f}")
    
    largest = integration.find_largest_area(shapes)
    if largest:
        print(f"\nLargest Shape: {largest['type'].title()} with area {largest['area']:.2f}")

if __name__ == "__main__":
    main()

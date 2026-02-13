#include <iostream>
#include <string>
#include <cmath>
using namespace std;

// Base class
class Shape {
protected:
    string color;
    string name;
    
public:
    Shape(string c, string n) : color(c), name(n) {}
    
    virtual double area() = 0;
    virtual double perimeter() = 0;
    virtual void draw() = 0;
    
    void display() {
        cout << "Shape: " << name << endl;
        cout << "Color: " << color << endl;
    }
    
    string getColor() {
        return color;
    }
    
    void setColor(string c) {
        color = c;
    }
};

// Subclass 1
class Circle : public Shape {
private:
    double radius;
    
public:
    Circle(string c, double r) : Shape(c, "Circle"), radius(r) {}
    
    double area() override {
        return 3.14159 * radius * radius;
    }
    
    double perimeter() override {
        return 2 * 3.14159 * radius;
    }
    
    void draw() override {
        cout << "Drawing a circle with radius " << radius << endl;
    }
    
    double getRadius() {
        return radius;
    }
};

// Subclass 2
class Rectangle : public Shape {
private:
    double length;
    double width;
    
public:
    Rectangle(string c, double l, double w) : Shape(c, "Rectangle"), length(l), width(w) {}
    
    double area() override {
        return length * width;
    }
    
    double perimeter() override {
        return 2 * (length + width);
    }
    
    void draw() override {
        cout << "Drawing a rectangle " << length << "x" << width << endl;
    }
    
    bool isSquare() {
        return length == width;
    }
};

// Subclass 3
class Triangle : public Shape {
private:
    double side1, side2, side3;
    
public:
    Triangle(string c, double s1, double s2, double s3) 
        : Shape(c, "Triangle"), side1(s1), side2(s2), side3(s3) {}
    
    double area() override {
        double s = (side1 + side2 + side3) / 2;
        return sqrt(s * (s - side1) * (s - side2) * (s - side3));
    }
    
    double perimeter() override {
        return side1 + side2 + side3;
    }
    
    void draw() override {
        cout << "Drawing a triangle" << endl;
    }
};

int main() {
    Circle circle("Red", 5.0);
    Rectangle rect("Blue", 4.0, 6.0);
    Triangle tri("Green", 3.0, 4.0, 5.0);
    
    cout << "=== Circle ===" << endl;
    circle.display();
    circle.draw();
    cout << "Area: " << circle.area() << endl;
    cout << "Perimeter: " << circle.perimeter() << endl << endl;
    
    cout << "=== Rectangle ===" << endl;
    rect.display();
    rect.draw();
    cout << "Area: " << rect.area() << endl;
    cout << "Perimeter: " << rect.perimeter() << endl;
    cout << "Is Square: " << (rect.isSquare() ? "Yes" : "No") << endl << endl;
    
    cout << "=== Triangle ===" << endl;
    tri.display();
    tri.draw();
    cout << "Area: " << tri.area() << endl;
    cout << "Perimeter: " << tri.perimeter() << endl;
    
    return 0;
}

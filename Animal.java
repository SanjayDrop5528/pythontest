// Base class
abstract class Animal {
    protected String name;
    protected int age;
    protected String species;
    
    public Animal(String name, int age, String species) {
        this.name = name;
        this.age = age;
        this.species = species;
    }
    
    public void eat() {
        System.out.println(name + " is eating");
    }
    
    public void sleep() {
        System.out.println(name + " is sleeping");
    }
    
    public abstract void makeSound();
    
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Species: " + species);
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
}

// Subclass 1
class Dog extends Animal {
    private String breed;
    private boolean trained;
    
    public Dog(String name, int age, String breed) {
        super(name, age, "Canine");
        this.breed = breed;
        this.trained = false;
    }
    
    public void makeSound() {
        System.out.println(name + " says: Woof! Woof!");
    }
    
    public void bark() {
        System.out.println(name + " is barking loudly");
    }
    
    public void fetch() {
        System.out.println(name + " is fetching the ball");
    }
    
    public void train() {
        trained = true;
        System.out.println(name + " has been trained");
    }
    
    public String getBreed() {
        return breed;
    }
}

// Subclass 2
class Cat extends Animal {
    private boolean indoor;
    private int livesLeft;
    
    public Cat(String name, int age, boolean indoor) {
        super(name, age, "Feline");
        this.indoor = indoor;
        this.livesLeft = 9;
    }
    
    public void makeSound() {
        System.out.println(name + " says: Meow!");
    }
    
    public void meow() {
        System.out.println(name + " is meowing softly");
    }
    
    public void scratch() {
        System.out.println(name + " is scratching the furniture");
    }
    
    public void purr() {
        System.out.println(name + " is purring contentedly");
    }
    
    public boolean isIndoor() {
        return indoor;
    }
}

// Subclass 3
class Bird extends Animal {
    private double wingSpan;
    private boolean canFly;
    
    public Bird(String name, int age, double wingSpan) {
        super(name, age, "Avian");
        this.wingSpan = wingSpan;
        this.canFly = true;
    }
    
    public void makeSound() {
        System.out.println(name + " says: Chirp! Chirp!");
    }
    
    public void fly() {
        if (canFly) {
            System.out.println(name + " is flying with wingspan: " + wingSpan + "cm");
        }
    }
    
    public void chirp() {
        System.out.println(name + " is chirping melodiously");
    }
    
    public double getWingSpan() {
        return wingSpan;
    }
}

// Main class
public class AnimalDemo {
    public static void main(String[] args) {
        Dog dog = new Dog("Buddy", 3, "Golden Retriever");
        Cat cat = new Cat("Whiskers", 2, true);
        Bird bird = new Bird("Tweety", 1, 15.5);
        
        System.out.println("=== Dog ===");
        dog.displayInfo();
        dog.makeSound();
        dog.eat();
        dog.bark();
        dog.fetch();
        
        System.out.println("\n=== Cat ===");
        cat.displayInfo();
        cat.makeSound();
        cat.sleep();
        cat.meow();
        cat.purr();
        
        System.out.println("\n=== Bird ===");
        bird.displayInfo();
        bird.makeSound();
        bird.fly();
        bird.chirp();
    }
}

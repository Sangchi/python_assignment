// Parent class (superclass)
class Animal {
    String name="elephent";
    Animal(){
        System.out.println("parent constructor");
    }
    void eat() {
        System.out.println("This animal eats grass.");
    }
}

// Child class (subclass) inheriting from Animal class
class Animal2 extends Animal {
    String name1="Dog";
    Animal2(){
        
        System.out.println("child constructor");
    }
    void eat() {
        System.out.println("The dog barks.");
    }
}

// Main class to test single inheritance
public class single_inheritence {
    public static void main(String[] args) {
        Animal2 myDog = new Animal2(); // Create an object of the Dog class
        myDog.eat(); // Call the eat() method from the Animal class (inherited)
        myDog.eat(); // Call the bark() method from the Dog class
    }
}


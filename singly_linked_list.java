// Node class represents each node in the linked list
class Node {
    int data; // Data stored in the node
    Node next; // Reference to the next node in the list

    // Constructor to initialize the node with data
    public Node(int data) {
        this.data = data;
        this.next = null; // By default, the next node is set to null
    }
}

// LinkedList class contains methods to manipulate the linked list
class LinkedList {
    Node head; // Reference to the first node in the list

    // Constructor to initialize an empty linked list
    public LinkedList() {
        this.head = null; // Initially, the list is empty, so the head is set to null
    }

    // Method to insert a new node at the end of the linked list
    public void insert(int data) {
        Node newNode = new Node(data); // Create a new node with the given data

        // If the list is empty, make the new node the head of the list
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            // Traverse the list to find the last node
            while (current.next != null) {
                current = current.next;
            }
            // Add the new node to the last node's next reference
            current.next = newNode;
        }
    }

    // Method to display the elements of the linked list
    public void display() {
        Node current = head; // Start from the head of the list
        // Traverse the list and print the data of each node
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next; // Move to the next node
        }
        System.out.println(); // Print a new line after displaying all elements
    }
}

// Main class to test the LinkedList implementation
public class singly_linked_list{
    public static void main(String[] args) {
        LinkedList list = new LinkedList(); // Create a new linked list
        list.insert(1); // Insert elements into the linked list
        list.insert(2);
        list.insert(3);
        list.insert(4);

        System.out.println("Linked List elements: ");
        list.display(); // Display the elements of the linked list
    }
}

// Node class represents each node in the linked list
class Node {
  late int data; // Data stored in the node
  Node? next; // Reference to the next node in the list

  // Constructor to initialize the node with data
  Node(int data) {
    this.data = data;
    this.next = null; // By default, the next node is set to null
  }
}

// LinkedList class contains methods to manipulate the linked list
class LinkedList {
  Node? head; // Reference to the first node in the list

  // Method to insert a new node at the end of the linked list
  void insert(int data) {
    Node newNode = Node(data); // Create a new node with the given data

    // If the list is empty, make the new node the head of the list
    if (head == null) {
      head = newNode;
    } else {
      Node? current = head;
      // Traverse the list to find the last node
      while (current!.next != null) {
        current = current.next;
      }
      // Add the new node to the last node's next reference
      current.next = newNode;
    }
  }

  // Method to display the elements of the linked list
  void display() {
    Node? current = head; // Start from the head of the list
    // Traverse the list and print the data of each node
    while (current != null) {
      print(current.data);
      current = current.next; // Move to the next node
    }
  }
}

// Main function to test the LinkedList implementation
void main() {
  LinkedList list = LinkedList(); // Create a new linked list
  list.insert(1); // Insert elements into the linked list
  list.insert(2);
  list.insert(3);
  list.insert(4);

  print("Linked List elements:");
  list.display(); // Display the elements of the linked list
}

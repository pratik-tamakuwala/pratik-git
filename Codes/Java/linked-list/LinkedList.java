package Listing1;

public class LinkedList {
	Node head;	
	
	public void insertData(int a) {
		
		Node node = new Node();
		node.val = a;
		node.next = null;
		
		if(head==null) {
			head = node;
		}
		
		else {
			Node n = head;
			while(n.next!=null) {
				
				n = n.next;
			}
			n.next = node;
		}
	}
	
	public void insertAtBegin(int a) {
		Node node = new Node();
		node.next = null;
		node.val = a;
		if(head==null) {
			head = node;
		}
		else {
			node.next = head;
			head = node;
		}
		
	}
	
	public void insetAtLocation(int d, int val) {
		Node node = new Node();
		node.next = null;
		node.val = val;
		if(d==0) {
		if(head==null) {
			head = node;
		}
		else {
			node.next = head;
			head = node;
		}
	  }
		else {
			Node n = head;
			while(d!=1) {
				n = n.next;
				d--;
			}
			node.next = n.next;
			n.next = node;
			
		}
	}
	public void deleteatLast() {
		Node n = head;
		if(head==null) {
			System.out.println("Linked List Empty");
		}
		
		if(head.next==null) {
			head = null;
			
		}
		else {
		while(n.next.next!=null) {
			n = n.next;
		}
		n.next = null;
	}
	}
	
	public void deleteAtBegin() {
		Node n = head;
		if(head==null) {
			System.out.println("Linked list Empty");
		}
		else if(head.next==null) {
			head = null;
		}
		else {
			head = head.next;
		}
	}
	
	public void deleteatLocation(int location) {
		Node n = head;
		Node n2 = head.next;
		if(location ==0) {
			deleteAtBegin();
			
		}
		else {
			for (int i = 0; i < location-1; i++) {
				n = n.next;				
				n2 = n2.next; 
			}
			if( n2==null)
				System.out.println("Wrog index number, Size is not sifficient");
			
			else
				n.next = n2.next;	
		}
		
		
	}
		
	public void show() {
		Node node = head;
		if(node==null) {
			System.out.println("Linked List Empty");
		}
		else {
		while(node.next!=null) {
			System.out.print(node.val+",");
			node = node.next;
			
		}
		System.out.println(node.val);
	}
	}
	
	
}

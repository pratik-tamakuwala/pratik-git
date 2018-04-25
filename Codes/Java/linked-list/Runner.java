package Listing1;

public class Runner {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedList li = new LinkedList();
		li.insertAtBegin(187);
		li.insertData(5);
		li.insertData(1);
		li.insertData(2);
		li.insertAtBegin(12);
		li.show();
		li.insetAtLocation(1,10);
		li.show();
		li.deleteatLocation(2);
		li.show();
		li.deleteatLocation(2);
		li.show();
		li.deleteatLocation(3);
		li.show();
		li.deleteatLocation(2);
		li.show();
		li.deleteatLocation(2);
		li.show();
		
		
	}

}

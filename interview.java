// 1.1
boolean isUniqueChars(String str) {
	if (str.length() > 128) return false;

	// there are 128 characters in the ASCII character set
	boolean[] char_set = new boolean[128];
	for (int i = 0; i < str.length; i++) {
		int val = str.charAt(i);
		if (char_set[val]) {
			return false;
		}
		char_set[val] = true;
	}
	return true;
}

// 1.2
String sort(String s) {
	char[] chars = s.toCharArray();
	Arrays.sort(chars);
	return new String(chars);
}

boolean isPermutation(String str_1, String str_2) {
	if (string_1.length() != string_2.length()) return false;
	return sort(str_1).equals(sort(str_2)
}

// 1.3
String urlify(String s) {
	// replace all spaces in a string with '%20'
	// parse string and find spaces
	// if at the end, then remove spaces
	char[] chars = s.toCharArray();

}



// ch 3 implementation
public class MyStack<T> {
	private static class StackNode<T> {
		private T data;
		private StackNode<T> next;

		public StackNode(T data) {
			this.data = data;
		}
	}

	private StackNode<T> top;

	public T pop() {
		if (top == null) throw new EmptyStackException();
		T item = top.data;
		top = top.next;
		return item;
	}

	public void push(T item) {
		StackNode<T> newTop = new StackNode<T>(item);
		newTop.next = top;
		top = newTop;
	}

	public T peek() {
		if (top == null) throw new EmptyStackException();
		return top.data;
	}

	public boolean isEmpty() {
		return top == null;
	}
}

public class MyQueue<T> {
	public static class QueueNode<T> {
		private T data;
		private QueueNode<T> next;

		public QueueNode(T data) {
			this.data = data;
		}
	}

	private QueueNode<T> front;
	private QueueNode<T> back;

	public T dequeue() {
		if (front == null) throw new EmptyQueueException();
		T data = front.data;
		front = front.next;
		// two item list, and removing front item, need to set back to null
		if (front.next == null) {
			back = null;
		}
		return data;
	}

	public T enqueue(T item) {
		QueueNode<T> newBack = new QueueNode<T>(item);
		if (back != null) {
			back.next = newBack;
		}
		back = newBack;
		// if there's only one item in the list
		if (front == null) {
			front = back;
		}
	}

	public T front() {
		if (front == null) throw new EmptyQueueException();
		return front.data;
	}

	boolean isEmpty() {
		return front == null;
	}
}

// ch 4 implementation
void preOrderTraversal(TreeNode node) {
	if (node != null) {
		visit(node);
		preOrderTraversal(node.left);
		preOrderTraversal(node.right);
	}
}

void inOrderTraversal(TreeNode node) {
	if (node != null) {
		inOrderTraversal(node.left);
		visit(node);
		inOrderTraversal(node.right);
	}
}

void postOrderTraversal(TreeNode node) {
	if (node != null) {
		preOrderTraversal(node.left);
		preOrderTraversal(node.right);
		visit(node);
	}
}

// working solution for DFS
class Node {
        
    private String data;
    private List<Node> adjacent;

    public Node(String data) {
        this.data = data;
        this.adjacent = new ArrayList<Node>();
    }
    
    public void addNode(String data) {
        Node newNode = new Node(data);
        this.adjacent.add(newNode);
    }
    
    // DFS where you print every node as you access it
    public static void dfs(Node root) {
        if (root == null) return;
        System.out.println(root.data);
        for (Node n:root.adjacent) {
            dfs(n);
        }
    }

    public static void main (String[] args) throws java.lang.Exception
    {    
        Node myNode = new Node("donald trump");
        myNode.addNode("is the worst");
        myNode.addNode("dump trump");
        Node.dfs(myNode);
    }

}

// attempting solution for BFS
public class Queue<T> {

	private static class QueueNode<T> {
		private String data;
		private QueueNode<String> next;

		public QueueNode(String data) {
			this.data = data;
			this.visited = false;
			this.adjacent = new ArrayList<QueueNode>();
		}
	}

	private QueueNode<String> first;
	private QueueNode<String> last;

	public static void enqueue(String data) {
		QueueNode n = new QueueNode<String>(data);
		if (last != null) {
			last.next = n;
		}
		last = n;
		this.adjacent.add(n);
		if (first == null) {
			first = last;
		}
	}

	// remove first 
	public static QueueNode dequeue() {
		if (first == null) throw new NoSuchElementException();
		QueueNode node = first;
		first = first.next;
		this.adjacent.remove(0);
		if (first == null) {
			last = null;
		}
		return node;
	}

	public static void top() {
		if (first == null) throw new NoSuchElementException();
		return first.data;
	}

	public boolean isEmpty() {
		return first == null;
	}

	public static void bfs(Node root) {
		if (root == null) return;
		Queue q = new Queue();
		q.enqueue(root);
		System.out.println(root);
		root.visited = true;
		while (!q.isEmpty()) {
			Node n = q.dequeue();
			System.out.println(n);
			n.visited = true;
			foreach (Node n in n.adjacent) {
				System.out.println(n);
				n.visited = true;
				q.enqueue(n);
			}
		}		
	}

	public static void main (String[] args) throws java.lang.Exception {
		QueueNode mynode = new QueueNode();
	}

}

// //Installed node modules: jquery underscore request express jade shelljs passport http sys lodash async mocha chai sinon sinon-chai moment connect validator restify ejs ws co when helmet wrench brain mustache should backbone forever debug

// class Node {
//     constructor(val) {
//         this.data = val;
//         this.children = [];
//     }
//     addNode(node) {
//         this.children.push(node);
//     }
// }

// const dfs = (n) => {
//     if (n.data === null) {
//         return;
//     }
//     console.log(n.data);
//     for (let i = 0; i < n.children.length; i++) {
//         dfs(n.children[i]);
//     }
// }

// let a = new Node('pantsuit');
// let b = new Node('queef');
// let c = new Node('madonna');
// let d = new Node('harambe');
// let e = new Node('chancellor dirks\' unibrow');
// let f = new Node('queef');

// //  a
// // / \ \
// // b c e
// // /
// // d

// a.addNode(b);
// a.addNode(c);
// b.addNode(d);
// a.addNode(e);

// dfs(a)



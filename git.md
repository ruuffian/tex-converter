# Heap Sort

## Description
Heap Sort is based on the Heap *Data-Structure*, specifically the **Max** heap. 
A naive approach to this problem would be to first load all array elements into a Min/Max heap and then remove off the top of the heap. Depending on the insert direction into the new <img src="https://render.githubusercontent.com/render/math?math=output"> array. This can order the array in either descending or ascending. 

Heap Sort consists of 2 parts: 
1. Build Heap 
2. Shrink Heap

### Build Heap
The **first** step is the build the heap. The word transform here is better since we are modifying the input array. They way this is done is at first we consider the first element. The heap property is fulfilled up-to index <img src="https://render.githubusercontent.com/render/math?math=1">, not including thus far. Now we consider index <img src="https://render.githubusercontent.com/render/math?math=1">. If this element is greater than the parent element then it is exchanged until the heap property is fulfilled. 

#### Array Child/Parent Calculations 
In an array-based heap each index represents the <img src="https://render.githubusercontent.com/render/math?math=i%5E%7B%5Ctext%7Bth%7D%7D"> node in a tree which is tree that is reversed in level order*. 


<img src="https://render.githubusercontent.com/render/math?math=%0A%5Ctext%7Bparent%7D_i%20%3D%20%5Cfrac%7B%5Ctext%7Bchild%20-%201%7D%7D%7B2%7D%0A">


<img src="https://render.githubusercontent.com/render/math?math=%0A%5Ctext%7Bchild%7D_L%20%3D%20%5Ctext%7Bparent%7D_i%20%2A%202%0A">


<img src="https://render.githubusercontent.com/render/math?math=%0A%5Ctext%7Bchild%7D_R%20%3D%20%5Ctext%7Bparent%7D_i%20%2A%202%20%2B%201%0A">


The <img src="https://render.githubusercontent.com/render/math?math=-1"> for parent calculation exists to make sure integer div produces the correct index for parent.   

Level order traversal is named in a named in a manner that exposes its description.  

#### Build Heap Code
```java
public static <T extends Comparable<T>> void heapify(T[] table){  
    int n = 1; //since by definition a single element heap is a heap  
 	while(n < table.length) {  
        int child = n;  
 		int parent = (child - 1) / 2;  
 		while(parent >= 0 && table[parent].compareTo(table[child]) < 0){  
            swap(table, child, parent);  
 			child = parent;  
 			parent = (child - 1) / 2;  
 		}  
        n++;  
 	}
}
```
##### Code Comments
Notice in <img src="https://render.githubusercontent.com/render/math?math=%5Ctext%7Bheapify%7D%28%29"> elements will only need to be moved up and never down and thus we only need to get parent's index.

### Shrink Heap
The Shrink heap is where the heap from **build heap** is turned into a sorted array.
The first step is to take the first element from the built heap and swap it with the element in the back. Now array<img src="https://render.githubusercontent.com/render/math?math=%5Bn-1%2C%20n%5D"> is sorted where <img src="https://render.githubusercontent.com/render/math?math=n"> is the size of the array. 

The array<img src="https://render.githubusercontent.com/render/math?math=%5B0%2C%20n-1%5D"> needs to be reheaped and the swapping can happen again. So the element at array<img src="https://render.githubusercontent.com/render/math?math=%5Bn-1%5D"> is swapped with array<img src="https://render.githubusercontent.com/render/math?math=%5B0%5D"> and the heap reformatted, the element is floated down to its correct position. 

These 2 processes occur until the array is full sorted.

#### Shrink Code

```java
public static <T extends Comparable<T>> void shrinkHeap(T[] table){  
    int n = table.length;  
 	while(n > 0){  
		n--;  
		swap(table, 0, n); //pushes largest element to the backend pos  
		int parent = 0;  
		while(true){  
			int left = parent * 2 + 1;  
			if(left >= n){  
					break;  
			}  
			int right = left + 1;  
			int maxChild = left;  
			if(right < n && table[right].compareTo(table[left]) > 0){  
				maxChild = right;  
			}  
			if(table[parent].compareTo(table[maxChild]) < 0){  
				swap(table, parent, maxChild);  
				parent = maxChild;  
			}  
			else{  
				break; //heap is restored  
			}  
		}  
    }  
}
```

##### Code Analysis
E
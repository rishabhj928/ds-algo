
class MinHeap:
    def __init__(self, cap):
        self.heap_size = 0
        self.capacity = cap
        self.harr = [0]*cap
    
    def parent(self, i):
        return int((i-1)/2)
    
    def left(self, i):
        return int((2*i)+1)
    
    def right(self, i):
        return int((2*i)+2)
    
    def getMin(self):
        return self.harr[0]
    
    def insertKey(self, key):
        if self.heap_size == self.capacity:
            return
        self.heap_size += 1
        i = self.heap_size - 1
        self.harr[i] = key

        while i!=0 and self.harr[self.parent(i)] > self.harr[i]:
            self.harr[self.parent(i)], self.harr[i] = self.harr[i], self.harr[self.parent(i)]
            i = self.parent(i)

    def decreaseKey(self, i, newval):
        self.harr[i] = newval
        while i!=0 and self.harr[self.parent(i)] > self.harr[i]:
            self.harr[self.parent(i)], self.harr[i] = self.harr[i], self.harr[self.parent(i)]
            i = self.parent(i)
    
    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heap_size and self.harr[l] < self.harr[i]:
            smallest = l
        if r < self.heap_size and self.harr[r] < self.harr[smallest]:
            smallest = r
        if smallest != i:
            self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
            self.minHeapify(smallest)

    def extractMin(self):
        if self.heap_size < 0:
            return
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.harr[0]
        
        root = self.harr[0]
        self.harr[0] = self.harr[self.heap_size-1]
        self.heap_size -= 1
        self.minHeapify(0)
        return root

    def deleteKey(self, key):
        self.decreaseKey(key, 0)
        self.extractMin()

if __name__ == "__main__":
    mheap = MinHeap(11)
    mheap.insertKey(3)
    mheap.insertKey(2)
    mheap.deleteKey(1)
    mheap.insertKey(15)
    mheap.insertKey(5)
    mheap.insertKey(4)
    mheap.insertKey(45)
    print(mheap.extractMin())
    print(mheap.getMin())
    mheap.decreaseKey(2,1)
    print(mheap.getMin())
    
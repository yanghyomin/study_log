# 2026-06-17

class circle_queue:
  def __init__(self,size):
    self.size = size
    self.arr = [None] * size
    self.front = 0
    self.rear = 0

  def isEmpty(self):
    return self.front == self.rear


  def isFull(self):
    return self.front == (self.rear + 1) % self.size

  def enqueue(self,data):
    self.isFull()
    self.arr[self.rear] = data
    self.rear = (self.rear + 1) % self.size

  def dequeue(self):
    self.isEmpty()
    data = self.arr[self.front]
    self.arr[self.front] = None
    self.front = (self.front + 1) % self.size
    return data
  

# 테스트 실행문
arr1 = circle_queue(5)
arr1.enqueue(1)
arr1.enqueue(2)
arr1.enqueue(3)
arr1.enqueue(4)
arr1.enqueue(5)
print(arr1.dequeue())
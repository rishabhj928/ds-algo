
class PhotosClient:
    def __init__(self, n: int) -> None:
        self.track = [False] * n
    def ack(self, x: int) -> None:
        self.track[x-1] = True
    def getMax(self) -> int:
        i = 0
        while i < len(self.track) and self.track[i]:
            i += 1
        return i

if __name__ == "__main__":
    pc = PhotosClient(10)
    pc.ack(1)
    print(pc.getMax())
    pc.ack(2)
    print(pc.getMax())
    pc.ack(4)
    print(pc.getMax())
    pc.ack(5)
    print(pc.getMax())
    pc.ack(3)
    print(pc.getMax())
    pc.ack(7)
    print(pc.getMax())
    pc.ack(6)
    print(pc.getMax())
    pc.ack(10)
    print(pc.getMax())
    pc.ack(9)
    print(pc.getMax())
    pc.ack(8)
    print(pc.getMax())
    

class ChrismasLights:
    def __init__(self, count: int):
        self.pos = 0
        self.count = count
        self.moveRight = True

    def get_next(self) -> list[str]:
        lights = [' '] * (self.count)
        left = 0
        right = self.count - 1
        lights[left] = '1'
        lights[right] = '1'

        if self.pos == 0:
            self.pos += 1
            lights[self.pos] = '*'
            return lights

        if self.pos == 1 and self.moveRight == False:
            self.moveRight = True
        if self.pos == right - 1:
            self.moveRight = False
        
        if self.moveRight:
            self.pos += 1;
        else:
            self.pos -= 1;
        lights[self.pos] = '*'            
                            
        return lights


if __name__ == "__main__":
    cl = ChrismasLights(8)

    for i in range(11):
        lights = cl.get_next()
        print(lights)

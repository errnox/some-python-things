class Canvas(object):
    """Repesents a 'virtual' canvas that is necessary for the circle to
    be drawn on.
    """
    def __init__(self, width=80, height=80, fill_char=' '):
        self.fill_char = fill_char
        self.line = []
        self.array = []
        # self.array = [list([i for i in range(width)]) for j in range(height)]
        for w in range(width):
            self.line.append(self.fill_char)
        for h in range(height):
            self.array.append(list(self.line))

    def draw_point(self, x, y, char='x'):
        for idx1, line in enumerate(self.array):
            if idx1 == y:
                for idx2, idxchar in enumerate(self.array[idx1]):
                    if idx2 == x:
                        self.array[idx1][idx2] = char
                        break

    def delete_point(self, x, y, char='x'):
        """Convenience method"""
        self.draw_point(x, y, self.fill_char)

    def pprint(self):
        for line in self.array:
            print line


class Circle(object):
    def __init__(self, x, y, center_x, center_y, char='x', canvas=None):
        self.x = x
        self.y = y
        self.center_x = center_x
        self.center_y = center_y
        self.canvas = canvas
        self.char = char

    def draw_circle_points(self, x, y, center_x, center_y, char):
        self.canvas.draw_point(center_x + x, center_y + y, char)
        self.canvas.draw_point(center_x - x, center_y - y, char)
        self.canvas.draw_point(center_x + x, center_y - y, char)
        self.canvas.draw_point(center_x - x, center_y + y, char)

        if self.x != self.y:
            self.canvas.draw_point(center_x + y, center_y + x, char)
            self.canvas.draw_point(center_x - y, center_y - x, char)
            self.canvas.draw_point(center_x + y, center_y - x, char)
            self.canvas.draw_point(center_x - y, center_y + x, char)

    def draw(self, center_x, center_y, radius, char='x'):
        if center_x:
            self.center_x = center_x
        if center_y:
            self.center_y = center_y

        x = 0
        yin = radius
        yout = radius

        din = 1 - radius
        deltaEin = 3
        deltaSEin  = -2 * radius + 5
        dout = 1 - radius
        deltaEout = 3
        deltaSEout = -2 * radius + 5

        for y in range(yin, yout):
            self.draw_circle_points(x, y, center_x, center_y, char)

        while yout > x:
            if din < 0:
                din = din + deltaEin
                deltaEin = deltaEin +2
                deltaSEin = deltaSEin + 2
            else:
                din = din + deltaSEin
                deltaEin = deltaEin + 2
                deltaSEin = deltaSEin + 4
                yin = yin - 1
            if dout <= 0:
                dout = dout + deltaEout
                deltaEout = deltaEout + 2
                deltaSEout = deltaSEout + 2
            else:
                dout = dout + deltaSEout
                deltaEout = deltaEout + 2
                deltaSEout = deltaSEout + 4
                yout = yout - 1
            x = x + 1
            for y in range(yin, yout):
                self.draw_circle_points(x, y, center_x, center_y, char)


class Square(object):
    """Represents a square.

    Features:
    - The border characters can be set individually.
    - The fill charachter can be set.
    """
    def __init__(self, width=80, height=40, char='#', fill_char=' ',
                 top_char=None,  bottom_char=None, left_char=None,
                 right_char=None):
        self.char = char
        self.fill_char = fill_char

        if top_char != None:
            self.top_char = top_char
        else:
            self.top_char = char

        if bottom_char != None:
            self.bottom_char = bottom_char
        else:
            self.bottom_char = char

        if left_char != None:
            self.left_char = left_char
        else:
            self.left_char = char

        if right_char != None:
            self.right_char = right_char
        else:
            self.right_char = char

        self.width = width
        self.height = height
        self.lines =[]

    # @staticmethod
    def autocomment(*args, **kwargs):
        def wrapper():
            # print 'Executing method: ' + args[0].__name__
            return args[0]
        return wrapper()

    @autocomment
    def render(self):
        top_line = self.top_char * self.width
        bottom_line = self.bottom_char * self.width
        inner_line = self.left_char + self.fill_char *(self.width - 2) + self.right_char
 
        lines = top_line + '\n'
        for i in range(self.height - 2):
            lines = lines + inner_line + '\n'
        lines += bottom_line + '\n'

        return lines


if __name__ == '__main__':
    square = Square(width=50, height=20, char='\033[0;47mx\033[m',
                    fill_char='\033[5;42mz\033[m')
    print square.render()

    # TEST
    center_x = 20
    center_y = 30

    # TEST
    # canvas = Canvas(40, 60)
    # canvas.draw_point(10, 25)
    # canvas.pprint()

    # TEST
    canvas = Canvas(40, 60)
    circle = Circle(10, 4, 20, 30, '#', canvas)
    # circle.draw_circle_points()
    circle.draw(10, 10, 9)
    canvas.pprint()

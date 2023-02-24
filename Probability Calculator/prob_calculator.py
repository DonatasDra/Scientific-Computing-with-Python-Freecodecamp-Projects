import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        for key in  kwargs:
            tmp = 0
            while tmp != kwargs[key]:
                self.contents.append(key)
                tmp += 1

    def draw(self, draws):
        if draws >= len(self.contents):
            return self.contents
        draws_list = list()
        tmp = 0
        while tmp != draws:
            draw = random.randrange(len(self.contents))
            draws_list.append(self.contents[draw])
            self.contents.pop(draw)
            tmp += 1
        return draws_list




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    tmp = 0
    success_count = 0
    expected = list()
    contentsCopy = copy.deepcopy(hat.contents)
    while tmp != num_experiments:
        expected = copy.copy(expected_balls)
        output = hat.draw(num_balls_drawn)
        hat.contents = copy.deepcopy(contentsCopy)
        for ball in output:
            if ball in expected and expected[ball] != 0:
                try:
                    expected[ball] -= 1
                except:
                    continue
        if sum(expected.values()) == 0:
            success_count+=1
        tmp += 1
    return success_count/num_experiments
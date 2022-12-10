class Device:
    def __init__(self):
        self.register = 1
        self.cycles = 0
        self.screen = ''

    def execute_seq(self, seq):
        sample = range(20, 221, 40)
        register_values = []

        for instruction in seq.split('\n'):
            match instruction.split():
                case ["addx", x]:
                    x = int(x)
                    for i in range(2):
                        self.cycle()
                        if self.cycles in sample:
                            register_values.append(self.register)
                    self.register += x
                case ["noop"]:
                    self.cycle()
                    if self.cycles in sample:
                        register_values.append(self.register)
        signal_strengths = [x * y for x, y in zip(list(sample), register_values)]
        return sum(signal_strengths)

    def cycle(self):
        column = self.cycles % 40
        if column == 0:
            self.screen += '\n'
        elif self.register in range(column-1, column+2):
            self.screen += "#"
        else:
            self.screen += '.'
        self.cycles += 1

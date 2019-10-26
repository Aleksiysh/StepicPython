class multifilter:
    def judge_half(self, pos, neg):
        return self.pos >= self.neg
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(self, pos, neg):
        return self.pos > 0
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(self, pos, neg):
        return self.neg == 0
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        # self.pos, self.neg = 0, 0
        self.funcs = funcs
        self.iterable = iterable
        self.judge = judge
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        for i in self.iterable:
            self.pos = 0
            self.neg = 0
            for f in self.funcs:
                if f(i):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self, self.pos, self.neg):
                yield i
        # возвращает итератор по результирующей последовательности


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]

print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))

pass

# Author - Tomasz Kosiński (azewiusz@gmail.com)
# A multiplication inversion example
import math
from datetime import datetime
import z3


def integer2base(num, base):
    result = []
    digit = num % base
    div = num // base
    while div >= 1:
        result.append(digit)
        digit = div % base
        div = div // base
    result.append(digit)
    result = result[::-1]
    return result


def base2integer(num, base):
    number = 0
    length = len(num)
    for i in range(0, len(num)):
        number = number + num[i] * base ** (length - i - 1)
    return number


def multiply(s, base, a, b, number):
    out = []
    p21 = (a[10] * b[10])
    p20 = ((p21 / base) + a[9] * b[10] + a[10] * b[9])
    p19 = ((p20 / base) + a[8] * b[10] + a[9] * b[9] + a[10] * b[8])
    p18 = ((p19 / base) + a[7] * b[10] + a[8] * b[9] + a[9] * b[8] + a[10] * b[7])
    p17 = ((p18 / base) + a[6] * b[10] + a[7] * b[9] + a[8] * b[8] + a[9] * b[7] + a[10] * b[6])
    p16 = ((p17 / base) + a[5] * b[10] + a[6] * b[9] + a[7] * b[8] + a[8] * b[7] + a[9] * b[6] + a[10] * b[5])
    p15 = ((p16 / base) + a[4] * b[10] + a[5] * b[9] + a[6] * b[8] + a[7] * b[7] + a[8] * b[6] + a[9] * b[5] + a[10] *
           b[4])
    p14 = ((p15 / base) + a[3] * b[10] + a[4] * b[9] + a[5] * b[8] + a[6] * b[7] + a[7] * b[6] + a[8] * b[5] + a[9] * b[
        4] + a[10] * b[3])
    p13 = ((p14 / base) + a[2] * b[10] + a[3] * b[9] + a[4] * b[8] + a[5] * b[7] + a[6] * b[6] + a[7] * b[5] + a[8] * b[
        4] + a[9] * b[3] + a[10] * b[2])
    p12 = ((p13 / base) + a[1] * b[10] + a[2] * b[9] + a[3] * b[8] + a[4] * b[7] + a[5] * b[6] + a[6] * b[5] + a[7] * b[
        4] + a[8] * b[3] + a[9] * b[2] + a[10] * b[1])
    p11 = ((p12 / base) + a[0] * b[10] + a[1] * b[9] + a[2] * b[8] + a[3] * b[7] + a[4] * b[6] + a[5] * b[5] + a[6] * b[
        4] + a[7] * b[3] + a[8] * b[2] + a[9] * b[1] + a[10] * b[0])
    p10 = ((p11 / base) + a[0] * b[9] + a[1] * b[8] + a[2] * b[7] + a[3] * b[6] + a[4] * b[5] + a[5] * b[4] + a[6] * b[
        3] + a[7] * b[2] + a[8] * b[1] + a[9] * b[0])
    p9 = ((p10 / base) + a[0] * b[8] + a[1] * b[7] + a[2] * b[6] + a[3] * b[5] + a[4] * b[4] + a[5] * b[3] + a[6] * b[
        2] + a[7] * b[1] + a[8] * b[0])
    p8 = ((p9 / base) + a[0] * b[7] + a[1] * b[6] + a[2] * b[5] + a[3] * b[4] + a[4] * b[3] + a[5] * b[2] + a[6] * b[
        1] + a[7] * b[0])
    p7 = ((p8 / base) + a[0] * b[6] + a[1] * b[5] + a[2] * b[4] + a[3] * b[3] + a[4] * b[2] + a[5] * b[1] + a[6] * b[0])
    p6 = ((p7 / base) + a[0] * b[5] + a[1] * b[4] + a[2] * b[3] + a[3] * b[2] + a[4] * b[1] + a[5] * b[0])
    p5 = ((p6 / base) + a[0] * b[4] + a[1] * b[3] + a[2] * b[2] + a[3] * b[1] + a[4] * b[0])
    p4 = ((p5 / base) + a[0] * b[3] + a[1] * b[2] + a[2] * b[1] + a[3] * b[0])
    p3 = ((p4 / base) + a[0] * b[2] + a[1] * b[1] + a[2] * b[0])
    p2 = ((p3 / base) + a[0] * b[1] + a[1] * b[0])
    p1 = ((p2 / base) + a[0] * b[0])
    p0 = ((p1 / base))
    v21 = p21 % base
    v20 = p20 % base
    v19 = p19 % base
    v18 = p18 % base
    v17 = p17 % base
    v16 = p16 % base
    v15 = p15 % base
    v14 = p14 % base
    v13 = p13 % base
    v12 = p12 % base
    v11 = p11 % base
    v10 = p10 % base
    v9 = p9 % base
    v8 = p8 % base
    v7 = p7 % base
    v6 = p6 % base
    v5 = p5 % base
    v4 = p4 % base
    v3 = p3 % base
    v2 = p2 % base
    v1 = p1 % base
    v0 = p0 % base
    s.add(v0 == number[0])
    s.add(v1 == number[1])
    s.add(v2 == number[2])
    s.add(v3 == number[3])
    s.add(v4 == number[4])
    s.add(v5 == number[5])
    s.add(v6 == number[6])
    s.add(v7 == number[7])
    s.add(v8 == number[8])
    s.add(v9 == number[9])
    s.add(v10 == number[10])
    s.add(v11 == number[11])
    s.add(v12 == number[12])
    s.add(v13 == number[13])
    s.add(v14 == number[14])
    s.add(v15 == number[15])
    s.add(v16 == number[16])
    s.add(v17 == number[17])
    s.add(v18 == number[18])
    s.add(v19 == number[19])
    s.add(v20 == number[20])
    s.add(v21 == number[21])
    s.add(z3.And(a[0] >= 0, a[0] < base))
    s.add(z3.And(b[0] >= 0, b[0] < base))
    s.add(z3.And(a[1] >= 0, a[1] < base))
    s.add(z3.And(b[1] >= 0, b[1] < base))
    s.add(z3.And(a[2] >= 0, a[2] < base))
    s.add(z3.And(b[2] >= 0, b[2] < base))
    s.add(z3.And(a[3] >= 0, a[3] < base))
    s.add(z3.And(b[3] >= 0, b[3] < base))
    s.add(z3.And(a[4] >= 0, a[4] < base))
    s.add(z3.And(b[4] >= 0, b[4] < base))
    s.add(z3.And(a[5] >= 0, a[5] < base))
    s.add(z3.And(b[5] >= 0, b[5] < base))
    s.add(z3.And(a[6] >= 0, a[6] < base))
    s.add(z3.And(b[6] >= 0, b[6] < base))
    s.add(z3.And(a[7] >= 0, a[7] < base))
    s.add(z3.And(b[7] >= 0, b[7] < base))
    s.add(z3.And(a[8] >= 0, a[8] < base))
    s.add(z3.And(b[8] >= 0, b[8] < base))
    s.add(z3.And(a[9] >= 0, a[9] < base))
    s.add(z3.And(b[9] >= 0, b[9] < base))
    s.add(z3.And(a[10] >= 0, a[10] < base))
    s.add(z3.And(b[10] >= 0, b[10] < base))
    s.add(z3.Not(z3.Or(z3.And(a[0] == 0, \
                              a[1] == 0, \
                              a[2] == 0, \
                              a[3] == 0, \
                              a[4] == 0, \
                              a[5] == 0, \
                              a[6] == 0, \
                              a[7] == 0, \
                              a[8] == 0, \
                              a[9] == 0, \
                              a[10] == 1, \
                              ), z3.And(b[0] == 0, \
                                        b[1] == 0, \
                                        b[2] == 0, \
                                        b[3] == 0, \
                                        b[4] == 0, \
                                        b[5] == 0, \
                                        b[6] == 0, \
                                        b[7] == 0, \
                                        b[8] == 0, \
                                        b[9] == 0, \
                                        b[10] == 1, \
                                        ))))


def vector_to_number(model, vector, base):
    dg = []
    for n in vector:
        dg.append(int(str(model.evaluate(n)), 10))
    return base2integer(dg, base)


def left_pad_with_zeros(lista, upto):
    l = []
    for i in range(0, upto - len(lista)):
        l.append(0)
    l = l + lista
    return l


def create_bit_vector(prefix, size, bits):
    v = []
    for i in range(0, size):
        v.append(z3.BitVec(prefix + str(i), bits))
    return v


def main():
    base = 100
    expected = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
    expected = base2integer(expected, 100)
    expected = integer2base(expected, base)
    size = len(expected)
    bits = 2 * (int(math.log(base, 2)) + 1) + 1

    va = create_bit_vector('a', size, bits)
    vb = create_bit_vector('b', size, bits)

    expected = left_pad_with_zeros(expected, 2 * len(expected))
    print(str(expected))

    z3.set_option("parallel.enable", True)
    # 6 Threads ran on AMD Phenom II X6
    z3.set_option("parallel.threads.max", 6)
    s = z3.SolverFor("QF_BV")

    multiply(s, base, va, vb, expected)

    time1 = datetime.now()
    if s.check() == z3.sat:
        print("sat")
        m = s.model()
        print(str(m))

        f1 = vector_to_number(m, va, base)
        f2 = vector_to_number(m, vb, base)
        print("Factor 1 = " + str(f1))
        print("Factor 2 = " + str(f2))
        print("The number (Factor 1 * Factor 2) " + str(f1 * f2))
    else:
        print("unsat")
        print(base2integer(expected, base))
        print(str(s.unsat_core()))

    time2 = datetime.now()

    print("Base " + str(base))
    print("Elapsed " + str(time2 - time1))


if __name__ == '__main__':
    main()

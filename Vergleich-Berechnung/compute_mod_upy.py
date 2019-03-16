@micropython.viper
def compute(data_len: int) -> int:
    data = bytearray(data_len)

    idx = 0
    while idx < data_len:
        data[idx] = idx % 256
        idx += 1

    loop = 10000
    dummy = 0

    print('Starting to compute.')

    while loop > 0:
        s = 0
        idx = 0

        while idx < data_len:
            s = (s + ptr8(data)[idx]) % 256
            idx += 1

        dummy ^= s
        loop -= 1

    print('Computation finished.', dummy)

compute(16*1024)

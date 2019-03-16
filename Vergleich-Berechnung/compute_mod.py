def compute(data_len):
    idx = 0

    data = bytearray(data_len)
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
            s = (s + data[idx]) % 256
            idx += 1

        dummy ^= s
        loop -= 1

    print('Computation finished.', dummy)
    return dummy

compute(16*1024)

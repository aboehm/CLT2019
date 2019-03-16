#include <stdio.h>
#include <stdlib.h>

#define DATA_LEN (16 * 1024)

static int compute(size_t data_len) {
    char* data = (char*)malloc(data_len);
    size_t idx;

    for (idx=0 ; idx<DATA_LEN ; idx++)
        data[idx] = idx % 256;

    int loop = 10000;
    int dummy = 0;

    printf("Starting to compute.\n");
    
    while (loop > 0) {
        int s = 0;

        for (idx=0 ; idx<DATA_LEN ; idx++)
            s = (s + data[idx]) % 256;

        dummy ^= s;
        loop --;
    }

    printf("Computation finished. %i\n", dummy);
    
    free(data);
    return dummy;
}

int main(int argc, char* argv[]) {
    compute(DATA_LEN);
    return 0;
}

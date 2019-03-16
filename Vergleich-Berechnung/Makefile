CFLAGS = -O2 `pkg-config --cflags python3` -fPIC
LDFLAGS = `pkg-config --libs python3`

all: compute_mod.so only_c

compute_mod.so: compute_mod.o
	$(CC) -shared $(LDFLAGS) -o $@ $<

%.c: %.py
	cython -3 $<

clean:
	rm -rf compute_mod.o compute_mod.so only_c __pycache__

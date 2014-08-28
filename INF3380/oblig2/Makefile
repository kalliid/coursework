CC = mpicc
CFLAGS = -O2 -fopenmp

PROJ = oblig2
OBJS = oblig2.o

all : oblig2 $(PROJ)

oblig2 : $(OBJS)
	$(CC) $(CFLAGS) $< -o $@ 

obj-clean:
	$(RM) *.o

exec-clean:
	$(RM) $(PROJ)

autosave-clean:
	$(RM) *~

clean:
	$(MAKE) obj-clean
	$(MAKE) exec-clean
	$(MAKE) autosave-clean

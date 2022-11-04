CC = gcc
TARGET = adder
OBJS = adder.o csapp.o

all : $(TARGET)
$(TARGET) : $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

csapp.o :
	$(CC) -c csapp.c

echoclient.o :
	$(CC) -c adder.c

clean :
	rm -f $(OBJS) $(TARGET)
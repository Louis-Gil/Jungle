CC = gcc
TARGET = server
OBJS = echoserver.o csapp.o

all : $(TARGET)
$(TARGET) : $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

csapp.o :
	$(CC) -c csapp.c

echoserver.o :
	$(CC) -c echoserver.c

clean :
	rm -f $(OBJS) $(TARGET)
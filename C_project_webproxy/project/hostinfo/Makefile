CC = gcc
TARGET = hostinfo
OBJS = hostinfo.o csapp.o

all : $(TARGET)
$(TARGET) : $(OBJS)
	$(CC) -o $(TARGET) $(OBJS)

csapp.o :
	$(CC) -c csapp.c

echoclient.o :
	$(CC) -c hostinfo.c

clean :
	rm -f $(OBJS) $(TARGET)
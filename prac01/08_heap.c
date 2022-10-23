#include <stdio.h>
#include <stdlib.h>
#define MAX_COUNT 100

typedef struct{
    int data[MAX_COUNT];
    int size;
} heapType;

void insertHeap(heapType* h, int item){ //item과 int size 타입이 같아야함
    int index;
    if(h->size >= (MAX_COUNT -1)){
        printf("Full!\n");
        return;
    }
    
    h->size++;
    index = h->size;
    h->data[index] = item; 

    while((index != 1)&&(h->data[index/2]<h->data[index])){
        int temp = h->data[index/2];
        h->data[index/2]=h->data[index];
        h->data[index]=temp;

        index = index/2;
    }

}

void printHeap(heapType* h){
    int i;
    printf("My heap: ");
    for(i=1;i<=h->size;i++)
        printf("%d ", h->data[i]);
    printf("\n");
}

int deleteHeap(heapType* h){
    int cur, child, temp;
    int topdata = h->data[1];
    if(h->size == 0){
        printf("Empty!!\n");
        return -1;
    }
    h->data[1] = h->data[h->size];
    h->size--;

    cur = 1;
    while((cur*2)<=h->size)
    {
        // 왼쪽 오른쪽 자식 중 더 큰 값을 가진 위치 -> child
        child = cur*2;
        if(((child+1)<=h->size) &&
            (h->data[child] < h->data[child+1]))
            child++;

        if(h->data[child] <= h->data[cur])
            break;
        //부모자식 값 교환
        temp=h->data[child];
        h->data[child] = h->data[cur];
        h->data[cur] = temp;

        cur = child;

    }
    return topdata;
}

void main(){
    int i;
    heapType heap;
    heap.size = 0;

    insertHeap(&heap, 17);
    insertHeap(&heap, 29);
    insertHeap(&heap, 27);
    insertHeap(&heap, 15);
    insertHeap(&heap, 34);
    printHeap(&heap);

    int count = heap.size;
    for(i=0;i<count;i++)
    {
        printf("deleted %d\n", deleteHeap(&heap));
    }
}
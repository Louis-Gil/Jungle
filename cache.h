#include "csapp.h"

#ifndef PROXY_WEB_SERVER_CACHE_H
#define PROXY_WEB_SERVER_CACHE_H

#define MAX_CACHE_SIZE 1049000
#define MAX_OBJECT_SIZE 102400

typedef struct Cache_node_type
{
    char header[MAX_OBJECT_SIZE];
    int payload[MAX_OBJECT_SIZE];
    struct Cache_node_type* prev;
    struct Cache_node_type* next;
}Cache_node;

typedef struct Cache_list_type
{
    int CurrentElementCount;
    Cache_node* frontNode;
    Cache_node* rearNode; 
}Cache_List;

Cache_List* initCache();
void insertNode();
void deleteNode();

#endif //PROXY_WEB_SERVER_CACHE_H
/*
 * mm-naive.c - The fastest, least memory-efficient malloc package.
 *
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free.
 *
 * NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your solution.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#include "mm.h"
#include "memlib.h"

/*********************************************************
 * NOTE TO STUDENTS: Before you do anything else, please
 * provide your team information in the following struct.
 ********************************************************/
team_t team = {
    /* Team name */
    "cheetah",
    /* First member's full name */
    "Gilin",
    /* First member's email address */
    "aa@aa.com",
    /* Second member's full name (leave blank if none) */
    "",
    /* Second member's email address (leave blank if none) */
    ""};

/* single word (4) or double word (8) alignment */
#define ALIGNMENT 8

/* rounds up to the nearest multiple of ALIGNMENT
사이즈를 올림하여 ALIGNMENT로 함 */
#define ALIGN(size) (((size) + (ALIGNMENT - 1)) & ~0x7)

#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))

/* Basic constants and macros */
#define WSIZE 4 /* Word and header/footer size (bytes) */
#define DSIZE 8 /* Double word size (bytes) */
// #define CHUNKSIZE (1 << 12) /* Extend heap by this amount (bytes) 처음 4kb*/
#define CHUNKSIZE 16 /* Extend heap by this amount (bytes) 처음 4kb*/
#define MINIMUM 24   /* 최소 블록 크기*/
#define MAX(x, y) ((x) > (y) ? (x) : (y))
/* Pack a size and allocated bit into a word
사이즈와 할당여부 패킹 -> 헤더 데이터 */
#define PACK(size, alloc) ((size) | (alloc))
/* Read and write a word at address p
p가 참조하는 워드 리턴 / p에 워드 저장 */
#define GET(p) (*(int *)(p))
#define PUT(p, val) (*(int *)(p) = (val))
/* Read the size and allocated fields from address p
헤더에서 사이즈만 리턴 / 할당여부만 리턴 */
#define GET_SIZE(p) (GET(p) & ~0x7)
#define GET_ALLOC(p) (GET(p) & 0x1)
/* Given block ptr bp, compute address of its header and footer
헤더와 풋터를 가리키는 포인터 리턴 */
#define HDRP(bp) ((void *)(bp) - WSIZE)
#define FTRP(bp) ((void *)(bp) + GET_SIZE(HDRP(bp)) - DSIZE)
/* Given block ptr bp, compute address of next and previous blocks
다음과 이전 블록 포인터 리턴 */
#define NEXT_BLKP(bp) ((void *)(bp) + GET_SIZE(HDRP(bp)))
#define PREV_BLKP(bp) ((void *)(bp) - GET_SIZE(HDRP(bp) - WSIZE))
/* 블록 포인터 bp의 다음, 이전 가용 블록 계산*/
#define NEXT_FREEP(bp) (*(void **)(bp + DSIZE))
#define PREV_FREEP(bp) (*(void **)(bp))

//선언 부분
static void *extend_heap(size_t words);
static void *coalesce(void *bp);
static void *find_fit(size_t asize);
static void place(void *bp, size_t asize);
static void removeBlock(void *bp);

static char *heap_listp=0;
static char *free_listp=0;

/*
 * mm_init - initialize the malloc package.
 최초 힙영역 할당  문제가 있으면 -1, 없으면 0
 */
int mm_init(void)
{
    if ((heap_listp = mem_sbrk(2 * MINIMUM)) == NULL)
        return -1;
    PUT(heap_listp, 0);                            // padding

    PUT(heap_listp + (WSIZE), PACK(MINIMUM, 1));   // header
    PUT(heap_listp + (DSIZE), 0);                  // prev
    PUT(heap_listp + (DSIZE + WSIZE), 0);          // next
    PUT(heap_listp + (MINIMUM), PACK(MINIMUM, 1)); // footer 24뒤

    PUT(heap_listp + (MINIMUM + WSIZE), PACK(0, 1));
    free_listp = heap_listp + (DSIZE); //???

    if (extend_heap(CHUNKSIZE / WSIZE) == NULL)
        return -1;
    return 0;
}

/* 힙 늘리기*/
static void *extend_heap(size_t words)
{
    char *bp;
    size_t size;

    size = (words % 2) ? (words + 1) * WSIZE : words * WSIZE;

    if (size < MINIMUM)
        size = MINIMUM;
    if ((long)(bp = mem_sbrk(size)) == -1)
        return NULL;

    PUT(HDRP(bp), PACK(size, 0));
    PUT(FTRP(bp), PACK(size, 0));
    PUT(HDRP(NEXT_BLKP(bp)), PACK(0, 1));
    // 이전 블록이 가용 블록이면 합병하고, 가용리스트에 블록 추가
    return coalesce(bp);
}

/*
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 항상 8바이트 정렬 포인터를 반환해야 한다?
 8바이트로 정렬된 payload pointer 를 반환
 */
void *mm_malloc(size_t size)
{
    size_t asize;
    size_t extendsize;
    char *bp;

    if (size <= 0)
        return NULL;

    asize = MAX(ALIGN(size) + DSIZE, MINIMUM);

    if ((bp = find_fit(asize)))
    {
        place(bp, asize);
        return bp;
    }
    // 최소 4kb씩 늘림
    extendsize = MAX(asize, CHUNKSIZE);
    if ((bp = extend_heap(extendsize / WSIZE)) == NULL)
        return NULL;
    place(bp, asize);
    return bp;
}

static void *find_fit(size_t asize)
{
    void *bp;
    /* 가용 리스트로부터 다음블록으로 가면서 할당되지 않은 블록이면 if문 실행
    asize가 블록사이즈 보다 작으면 리턴   */
    for (bp = free_listp; GET_ALLOC(HDRP(bp)) == 0; bp = NEXT_FREEP(bp))
    {
        if (asize <= (size_t)GET_SIZE(HDRP(bp)))
        {
            return bp;
        }
    }
    return NULL;
}

static void place(void *bp, size_t asize)
{
    size_t csize = GET_SIZE(HDRP(bp));

    if ((csize - asize) >= (MINIMUM))
    {
        //블록 할당
        PUT(HDRP(bp), PACK(asize, 1));
        PUT(FTRP(bp), PACK(asize, 1));
        //가용리스트에서 삭제
        removeBlock(bp);
        bp = NEXT_BLKP(bp);
        //남은 공간의 헤더 풋터 계산, 인접 가용블록과 합병???
        PUT(HDRP(bp), PACK(csize - asize, 0));
        PUT(FTRP(bp), PACK(csize - asize, 0));
        coalesce(bp);
    }
    else
    { //최소블록크기 미만일시
        PUT(HDRP(bp), PACK(csize, 1));
        PUT(FTRP(bp), PACK(csize, 1));
        removeBlock(bp);
    }
}

static void *coalesce(void *bp)
{ // prev_blkp 생김???
    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp))) || PREV_BLKP(bp) == bp;
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
    size_t size = GET_SIZE(HDRP(bp));

    if (prev_alloc && !next_alloc) // 앞이 할당 뒤가 비었음
    {
        size += GET_SIZE(HDRP(NEXT_BLKP(bp)));
        removeBlock(NEXT_BLKP(bp));
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
    }
    else if (!prev_alloc && next_alloc) // 뒤가 할당 앞이 비었음
    {
        size += GET_SIZE(HDRP(PREV_BLKP(bp)));
        bp = PREV_BLKP(bp);
        removeBlock(bp); //앞에 bp로 설정하고 삭제???
        PUT(FTRP(bp), PACK(size, 0));
        PUT(HDRP(bp), PACK(size, 0));
    }
    else if (!prev_alloc && !next_alloc) // 앞뒤 할당 안되어있음
    {
        size += GET_SIZE(HDRP(PREV_BLKP(bp))) +
                GET_SIZE(HDRP(NEXT_BLKP(bp)));
        removeBlock(PREV_BLKP(bp));
        removeBlock(NEXT_BLKP(bp));
        bp = PREV_BLKP(bp);
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
        // 이전 블록, 블록 할당인 경우는 위 행동 없음

        /* 현재 bp의 next가 가용리스트의 처음을 가리킴
        가용리스트 처음의 prev가 bp를 가리킴
        현재 bp의 prev가 null
        가용리스트의 처음이 bp를 가리킴
        */
        NEXT_FREEP(bp) = free_listp;
        PREV_FREEP(free_listp) = bp;
        PREV_FREEP(bp) = NULL;
        free_listp = bp;
    }
    return bp;
}

// 가용리스트에서 블록 제거
static void removeBlock(void *bp)
{
    if (PREV_FREEP(bp))
        NEXT_FREEP(PREV_FREEP(bp)) = NEXT_FREEP(bp);
    else
        free_listp = NEXT_FREEP(bp);
    PREV_FREEP(NEXT_FREEP(bp)) = PREV_FREEP(bp);
}

/*
 * mm_realloc - Implemented simply in terms of mm_malloc and mm_free
 최소 크기의 할당된 영역으로 포인터 반환
 ptr이 null이면 호출은 malloc(size)와 같음
 -크기가 0인 경우 free(ptr)과 같음
 realloc에 대한 호출은 ptr(이전버전)로 표시된 메모리 블록의 크기를
 */
void *mm_realloc(void *ptr, size_t size)
{
    size_t oldsize;
    void *newptr;
    size_t asize = MAX(ALIGN(size) + DSIZE, MINIMUM);

    if (size <= 0)
    {
        free(ptr);
        return 0;
    }
    if (ptr == NULL)
    {
        return malloc(size);
    }
    oldsize = GET_SIZE(HDRP(ptr));
    if (asize == oldsize) //*ptr? ptr
    {
        return ptr;
    }
    if (asize <= oldsize)
    {
        size = asize;

        if (oldsize - size <= MINIMUM)
            return ptr;
        PUT(HDRP(ptr), PACK(size, 1));
        PUT(FTRP(ptr), PACK(size, 1));
        PUT(HDRP(NEXT_BLKP(ptr)), PACK(oldsize - size, 1));
        free(NEXT_BLKP(ptr));
        return ptr;
    }
    newptr = malloc(size);

    if (!newptr)
    {
        return 0;
    }
    if (size < oldsize)
        oldsize = size;
    memcpy(newptr, ptr, oldsize);
    free(ptr);
    return newptr;
}

/*
 * mm_free - Freeing a block does nothing.
 ptr이 가리키는 블록을 개방
 malloc 또는 remalloc에 의해 생긴 포인터만 반환하는 것을 보장

 블록을 가용리스트에 추가하는 함수
 블록 포인터를 이용하여 해당블록의 header와 footer의 allocated bit을 0
 인접한 가용 블록과 합병
 */
void mm_free(void *bp)
{
    if (!bp)
        return;
    size_t size = GET_SIZE(HDRP(bp));

    PUT(HDRP(bp), PACK(size, 0));
    PUT(FTRP(bp), PACK(size, 0));
    coalesce(bp);
}
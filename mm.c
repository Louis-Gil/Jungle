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

/* 기본 선언 매크로 */
#define WSIZE 4
#define DSIZE 8
#define CHUNKSIZE (1 << 12)
#define ALIGNMENT 8
#define ALIGN(size) (((size) + (ALIGNMENT - 1)) & ~0x7)
#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))  /*macros*/
#define MAX(x, y) ((x) > (y) ? (x) : (y))    /* Pack a size and allocated bit into a word. */
#define PACK(size, alloc) ((size) | (alloc)) /* Read and write a word at address p */
#define GET(p) (*((unsigned int *)(p)))
#define PUT(p, val) (*(unsigned int *)(p) = (val)) /* Read the size and allocated fields from address p */
#define GET_SIZE(p) ((unsigned int)GET(p) & ~(ALIGNMENT - 1))
#define GET_ALLOC(p) (GET(p) & 0x1) /* Given block pointer bp, compute address of its header and footer */
#define HDRP(bp) ((void *)(bp)-WSIZE)
#define FTRP(bp) ((void *)(bp) + GET_SIZE(HDRP(bp)) - 2 * WSIZE) /* Given block pointer bp, compute address of next and previous blocks */
#define NEXT_BLKP(bp) ((void *)(bp) + GET_SIZE(((void *)(bp)-WSIZE)))
#define PREV_BLKP(bp) ((void *)(bp)-GET_SIZE(((void *)(bp)-2 * WSIZE)))

/* 추가 선언 매크로*/
/* Given block ptr bp, compute address of next and previous blocks
다음과 이전 블록 포인터 리턴 */
#define PREV_FREE_BLKP(ptr) (*(void **)(ptr))
#define NEXT_FREE_BLKP(ptr) (*(void **)(ptr + WSIZE))
/* Given block pointers ptr and prev, set the PREV pointer of ptr to *prev.
bp 전 free블록에 prev를 넣음, bp 후 free블록에 next를 넣음*/
#define SET_PREV_FREE(bp, prev) (*((void **)(bp)) = prev)
#define SET_NEXT_FREE(bp, next) (*((void **)(bp + WSIZE)) = next)

static void *heap_listp = NULL; // heap 시작주소 pointer
static void *free_listp = NULL; // free list head - 가용리스트 시작부분

/* 기본 선언  */
static void *extend_heap(size_t words);
static void *coalesce(void *bp);
static void *find_fit(size_t asize);
static void *place(void *bp, size_t asize);

/* 추가 선언*/
static void delete_node(void *bp);
static void insert_node(void *bp);

/* 최초 힙 영역 할당, 문제 있으면 -1, 없으면 0
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+  padding  +  prol header  +  prol footer  +  epilogue  +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 heap_listp                   free_listp
이후 1024 바이트 할당받는 extend_heap 실행
*/
int mm_init(void)
{
    if ((heap_listp = mem_sbrk(2 * DSIZE)) == (void *)-1)
    {
        return -1;
    }
    PUT(heap_listp, 0);                                /* Alignment padding */
    PUT(heap_listp + (1 * WSIZE), PACK(ALIGNMENT, 1)); /* Prologue header */
    PUT(heap_listp + (2 * WSIZE), PACK(ALIGNMENT, 1)); /* Prologue footer */
    PUT(heap_listp + (3 * WSIZE), PACK(0, 1));         /* Epilogue  */
    free_listp = heap_listp + DSIZE;

    /* 사이즈(바이트)를 받아서 최소단위 묶음 이상으로 늘려(bit)준다. 이후 coalesce
    init -> extend_heap -> coalesce
    malloc(할당 사이즈 부족) -> extend_heap -> coalesce
    */
    if ((extend_heap(CHUNKSIZE / WSIZE)) == NULL)
    {
        return -1;
    }
    return 0;
}

/* 사이즈(바이트)를 받아서 최소단위 묶음 이상으로 늘려(bit)준다. 이후 coalesce
init -> extend_heap -> coalesce
malloc(할당 사이즈 부족) -> extend_heap -> coalesce
*/
static void *extend_heap(size_t words)
{
    void *bp;
    size_t size;
    size = ALIGN(words * WSIZE);
    //성공시 이전 brk 주소(void*), 실패시 -1
    if ((long)(bp = mem_sbrk(size)) == -1)
        return NULL;
    /*
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    +++++++++++++++++++++++++++
    +  padding  +  prol header  +  prol footer  +  epilogue  +          생성(1024byte)
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    +++++++++++++++++++++++++++
     heap_listp                   free_listp

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    ++++++++++++++++++++++++++++
    +  padding  +  prol header  +  prol footer  +  header    +    footer  +  ..  +  epilogue +
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    ++++++++++++++++++++++++++++
                                                                  bp
    */
    PUT(HDRP(bp), PACK(size, 0));
    PUT(FTRP(bp), PACK(size, 0));
    PUT(HDRP(NEXT_BLKP(bp)), PACK(0, 1));
    return coalesce(bp);
}

/* bp를 받아서 앞뒤 블록 빈칸이면 합침
init -> extend_heap -> coalesce (효과없음)
malloc(할당 사이즈 부족) -> extend_heap -> coalesce
free -> coalesce
realloc -> malloc -> free -> coalesce ???
*/
static void *coalesce(void *bp)
{
    size_t prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp)));
    size_t next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
    size_t size = GET_SIZE(HDRP(bp));

    // case1 : prev 0, next 0
    if (prev_alloc && next_alloc)
    {
        insert_node(bp);
        return bp;
    }
    // case2 : prev 0, next 1
    else if (prev_alloc && !next_alloc)
    {
        delete_node(NEXT_BLKP(bp));
        size += GET_SIZE(HDRP(NEXT_BLKP(bp)));
        PUT(HDRP(bp), PACK(size, 0));
        PUT(FTRP(bp), PACK(size, 0));
        insert_node(bp);
    }
    // case3 : prev 1, next 0
    else if (!prev_alloc && next_alloc)
    {
        delete_node(PREV_BLKP(bp));
        size += GET_SIZE(HDRP(PREV_BLKP(bp)));
        PUT(FTRP(bp), PACK(size, 0));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));
        bp = PREV_BLKP(bp);
        insert_node(bp);
    }
    else
    {
        // case4 : prev 1, next 1
        delete_node(PREV_BLKP(bp));
        delete_node(NEXT_BLKP(bp));
        size += GET_SIZE(HDRP(PREV_BLKP(bp)));
        size += GET_SIZE(HDRP(NEXT_BLKP(bp)));
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0));
        PUT(FTRP(NEXT_BLKP(bp)), PACK(size, 0));
        bp = PREV_BLKP(bp);
        insert_node(bp);
    }
    return bp;
}

/* 가용리스트에서 해당 블록 삭제
next는 bp의 다음 free블록, prev는 bp의 이전 free블록
prev가 null이라면(처음), free_listp는 next, 아니면 전 블록에 next를 넣어줌
bp의 이후 free블록이 있다면(마지막이 아님),
 */
static void delete_node(void *bp)
{
    void *next = (void *)NEXT_FREE_BLKP(bp);
    void *prev = (void *)PREV_FREE_BLKP(bp);
    if (prev == NULL)
    { /* Start of the list */
        free_listp = next;
    }
    else
    {
        SET_NEXT_FREE(prev, next);
    }

    if (next != NULL)
    { /* Not the end of list */
        SET_PREV_FREE(next, prev);
    }
}

/* Add the block pointer bp to the free list in address order*/
static void insert_node(void *bp)
{
    void *curr = free_listp;
    void *saved = curr;
    void *prev = NULL;
    while (curr != NULL && bp < curr)
    {
        prev = PREV_FREE_BLKP(curr);
        saved = curr;
        curr = NEXT_FREE_BLKP(curr);
    }

    SET_PREV_FREE(bp, prev);
    SET_NEXT_FREE(bp, saved);
    if (prev != NULL)
    {
        SET_NEXT_FREE(prev, bp);
    }
    else
    {
        free_listp = bp; /* Insert bp before current free list head*/
    }
    if (saved != NULL)
    {
        SET_PREV_FREE(saved, bp);
    }
}

/*
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    size_t asize;      /* Adjusting block size*/
    size_t extendsize; /* Amount to extend heap if no fit */
    void *bp;
    /* Ignore spurious requests */
    if (size == 0)
    {
        return NULL;
    }

    /* Adjust block size to include overhead, alignment requirements*/
    if (size <= ALIGNMENT)
    {
        asize = 2 * ALIGNMENT; /* Minimum block size 16: 8 bytes for alignment, 8 bytes for header and footer*/
    }
    else
    {
        asize = ALIGN(size + (2 * WSIZE)); /* Add in overhead bytes and round up to nearest multiple of ALIGNMENT */
    }

    /* Search free list for a fit*/
    if ((bp = find_fit(asize)) != NULL)
    {
        bp = place(bp, asize);
        return bp;
    }

    /* No fit found. Get more meomory and place the block. */
    extendsize = MAX(asize, CHUNKSIZE);
    if ((bp = extend_heap(extendsize / WSIZE)) == NULL)
    {
        return NULL; /* No more heap space */
    }
    bp = place(bp, asize);

    return bp;
}

static void *find_fit(size_t asize)
{

    void *bp;
    for (bp = free_listp; bp != NULL; bp = NEXT_FREE_BLKP(bp))
    {
        if (asize <= GET_SIZE(HDRP(bp)))
        {
            return bp;
        }
    }
    // overlap_free_test(bp);
    return NULL;
}

/* Places the requested block and split the excess. Assumes that block
 * pointed to by bp is large enough to accomodate asize.
 *
 * The first part of the block is allocated and the second part is kept free
 */

static void *place(void *bp, size_t asize)
{
    size_t csize = GET_SIZE(HDRP(bp));
    int remaining_free_size = csize - asize;
    if ((csize - asize) >= (2 * ALIGNMENT))
    { // Enough room left to split
        delete_node(bp);
        PUT(HDRP(bp), PACK(asize, 1));
        PUT(FTRP(bp), PACK(asize, 1));
        void *orig_bp = bp;
        bp = NEXT_BLKP(bp);
        PUT(HDRP(bp), PACK(remaining_free_size, 0));
        PUT(FTRP(bp), PACK(remaining_free_size, 0));
        insert_node(bp);
        bp = orig_bp;
    }
    else
    { // No need to split; include entire free block in size.
        PUT(HDRP(bp), PACK(csize, 1));
        PUT(FTRP(bp), PACK(csize, 1));
        delete_node(bp);
    }
    return bp;
}
/*
  mm_free - frees a block of memory, enabling it to be reused later
 */
void mm_free(void *ptr)
{
    size_t size = GET_SIZE(HDRP(ptr));
    PUT(HDRP(ptr), PACK(size, 0));
    PUT(FTRP(ptr), PACK(size, 0));
    coalesce(ptr);
}
/* mm_realloc - reallocates a memory block to update it with the given s
 */
void *mm_realloc(void *ptr, size_t size)
{
    size_t asize;
    void *bp;

    /* Ignore spurious requests */
    if (size == 0)
    {
        return NULL;
    }

    /* Adjust block size to include overhead, alignment requirements*/
    if (size <= ALIGNMENT)
    {
        asize = 2 * ALIGNMENT; /* Minimum block size 16: 8 bytes for alignment, 8 bytes for header and footer*/
    }
    else
    {
        // asize = ALIGN(size + (2 * ALIGNMENT)); /* Add in overhead bytes and round up to nearest multiple of ALIGNMENT */
        asize = ALIGN(size + (2 * WSIZE));
    }

    size_t cur_size = GET_SIZE(HDRP(ptr));

    if (cur_size > asize)
    {
        bp = place(ptr, asize);
        assert(bp == ptr);
    }
    else if (cur_size < asize)
    {
        void *next_bp = NEXT_BLKP(ptr);
        void *next_block_header = HDRP(next_bp);
        /* see if next block has room for the new size */

        if (!GET_ALLOC(next_block_header) && GET_SIZE(next_block_header) >= (asize - cur_size))
        {
            delete_node(next_bp);
            PUT(HDRP(ptr), PACK(cur_size + GET_SIZE(next_block_header), 0));
            PUT(FTRP(ptr), PACK(cur_size + GET_SIZE(next_block_header), 0));

            void *temp1; // hold data going to be overwritten by the prev pointer in insert_node
            void *temp2; // hold data going to be overwritten by the next pointer in insert_node
            memcpy(&temp1, ptr, WSIZE);
            memcpy(&temp2, ptr + WSIZE, WSIZE);

            insert_node(ptr);
            bp = place(ptr, asize);

            /* copy back the saved data */
            memcpy(bp, &temp1, WSIZE);
            memcpy(bp + WSIZE, &temp2, WSIZE);
        }
        else if ((bp = find_fit(asize)) != NULL)
        { /* Search free list for a fit*/
            bp = place(bp, asize);
            memcpy(bp, ptr, cur_size - (2 * WSIZE));
            mm_free(ptr);
        }
        else
        {
            /* No fit found. Get more meomory and place the block. */
            size_t extendsize = MAX(asize, CHUNKSIZE);
            if ((bp = extend_heap(extendsize / WSIZE)) == NULL)
            {
                return NULL; /* No more heap space */
            }
            bp = place(bp, asize);
            memcpy(bp, ptr, cur_size - (2 * WSIZE));
            mm_free(ptr);
        }
    }
    else
    {
        bp = ptr;
    }

    return bp;
}
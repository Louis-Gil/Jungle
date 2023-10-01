/* file.c: Implementation of memory backed file object (mmaped object). */

#include "vm/vm.h"
#include "include/userprog/process.h"
#include "include/threads/mmu.h"
#include "devices/disk.h"


static bool file_backed_swap_in(struct page *page, void *kva);
static bool file_backed_swap_out(struct page *page);
static void file_backed_destroy(struct page *page);

/* DO NOT MODIFY this struct */
static const struct page_operations file_ops = {
	.swap_in = file_backed_swap_in,
	.swap_out = file_backed_swap_out,
	.destroy = file_backed_destroy,
	.type = VM_FILE,
};


/* The initializer of file vm
file vm 초기화 */
void vm_file_init(void)
{
}

/* Initialize the file backed page */
bool file_backed_initializer(struct page *page, enum vm_type type, void *kva)
{
	/* Set up the handler */
	page->operations = &file_ops;

	struct file_page *file_page = &page->file;
}

/* Swap in the page by read contents from the file. */
static bool
file_backed_swap_in(struct page *page, void *kva)
{
	// struct file_page *file_page UNUSED = &page->file;
	if(page==NULL)
		return false;
	
	struct container *aux = (struct container *)page->uninit.aux;
	size_t page_zero_bytes = PGSIZE - aux->page_read_bytes;
	// file_read_at(aux->file, kva, aux->page_read_bytes, aux->offset);
	file_seek(aux->file, aux->offset);
	if(file_read(aux->file, kva, aux->page_read_bytes) != (uint32_t)aux->page_read_bytes)
		return false;
	memset(kva + aux->page_read_bytes, 0, page_zero_bytes);
	
	// ##### 1 고민
	//pml4_set_page(thread_current()->pml4, page->va, kva, 1);


	return true;
}

/* Swap out the page by writeback contents to the file. */
static bool
file_backed_swap_out(struct page *page)
{
	// struct file_page *file_page UNUSED = &page->file;
	if(page==NULL)
		return false;

	struct container *aux = (struct container *)page->uninit.aux;
	if (pml4_is_dirty(thread_current()->pml4, page->va))
	{
		// file_write_at(aux->file, page, PGSIZE, aux->offset);
		file_write_at(aux->file, page->va, aux->page_read_bytes, aux->offset);
		pml4_set_dirty (thread_current()->pml4, page->va, 0);
	}
	//파일이 비워졌다, pml4_clear
	// memset(page->frame->kva, 0, PGSIZE);
	pml4_clear_page(thread_current()->pml4, page->va);
	return true;
}

/* Destory the file backed page. PAGE will be freed by the caller. */
static void
file_backed_destroy(struct page *page)
{
	struct file_page *file_page UNUSED = &page->file;
}

/* Do the mmap */
void *
do_mmap(void *addr, size_t length, int writable,
		struct file *file, off_t offset)
{
	void *ori_addr = addr;
	struct file *mfile = file_reopen(file);
	size_t read_bytes = length > file_length(file) ? file_length(file) : length;
	size_t zero_bytes = PGSIZE - read_bytes % PGSIZE;

	while (read_bytes > 0 || zero_bytes > 0)
	{
		/* Do calculate how to fill this page.
		 * We will read PAGE_READ_BYTES bytes from FILE
		 * and zero the final PAGE_ZERO_BYTES bytes. */
		size_t page_read_bytes = read_bytes < PGSIZE ? read_bytes : PGSIZE;
		size_t page_zero_bytes = PGSIZE - page_read_bytes;

		/* TODO: Set up aux to pass information to the lazy_load_segment. */
		struct container *container = (struct container *)malloc(sizeof(struct container));
		container->file = mfile;
		container->page_read_bytes = page_read_bytes;
		container->offset = offset;

		if (!vm_alloc_page_with_initializer(VM_FILE, addr,
											writable, lazy_load_segment, container))
			return NULL;

		/* Advance. */
		read_bytes -= page_read_bytes;
		zero_bytes -= page_zero_bytes;
		addr += PGSIZE;
		offset += page_read_bytes;
	}
	return ori_addr;
}

/* Do the munmap */
void do_munmap(void *addr)
{
	while (true)
	{
		struct page *page = spt_find_page(&thread_current()->spt, addr);
		
		if (page == NULL)
			break;

		struct container *aux = (struct container *)page->uninit.aux;
	
		// if (pml4_is_dirty(thread_current()->pml4, page))
		if (pml4_is_dirty(thread_current()->pml4, page->va))
		{
			// file_write_at(aux->file, page, PGSIZE, aux->offset);
			file_write_at(aux->file, addr, aux->page_read_bytes, aux->offset);
			pml4_set_dirty (thread_current()->pml4, page->va, 0);
		}

		pml4_clear_page(thread_current()->pml4, page->va);

		// aux->offset += PGSIZE;

		addr += PGSIZE;
	}
}

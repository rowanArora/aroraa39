#include <assert.h>
#include "queue.h"
#include <stdio.h>
#include <stdlib.h>

/*************************************************
 * Implement the following functions.
 * DO NOT add any global (static) variables,
 * Except in Part C.
 * You can add help functions as you need.
 ************************************************/


/*************************************************
 * ------------------Part A:---------------------- 
 * In this part, you will implement
 * a  dynamically allocated queue with
 * a linked list. 
 * DO NOT add any global (static) variables.
 *************************************************/

bool queue_A_initialized = false;

typedef struct queue_A_node {

/* Add code BEGIN */
	struct queue_A_node *next;
/* Add code END */

	void *item;

} queue_A_node_t;

queue_A_node_t *queue_A_head = NULL;
queue_A_node_t *queue_A_tail = NULL;

/* Add code BEGIN */

/* Helper functions and macros only! */
queue_A_node_t* queue_A_new_node(void *item) {
	queue_A_node_t *temp = malloc(sizeof(queue_A_node_t));
	temp->item = item;
	temp->next = NULL;
	return temp;
}
/* Add code END */

/* Perform any initialization needed so that the queue data structure can be 
 * used. 
 * Returns 0 on success or an error if the queue has already been initialized.
 */
int queue_A_initialize()
{

/* Add code BEGIN */
	if (queue_A_initialized) {
		return ERR_INITIALIZED;
	}
	else {
		queue_A_initialized = true;
		return 0;
	}
/* Add code END */

	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* Add item to the tail of the queue.
 * Returns 0 on success or an appropriate error code on failure.
 */
int queue_A_enqueue(void *item)
{

/* Add code BEGIN */
	if (!queue_A_initialized) {
		return ERR_NOT_INITIALIZED;
	}
	else {
		queue_A_node_t *temp = queue_A_new_node(item);
		if (queue_A_tail == NULL) {
			queue_A_head = queue_A_tail = temp;
			return 0;
		}
		queue_A_tail->next = temp;
		queue_A_tail = queue_A_tail->next;
		return 0;
	}
/* Add code END */

	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* Remove the item at the head of the queue and store it in the location
 * pointed to by 'item'.
 * Returns 0 on success or an appropriate error code on failure.
 */
int queue_A_dequeue(void **item)
{

/* Add code BEGIN */
	if (!queue_A_initialized) {
		return ERR_NOT_INITIALIZED;
	}
	else if (item == NULL) {
		return ERR_INVALID_ARG;
	}
	else if (queue_A_head == NULL){
		return ERR_EMPTY;
	}
	*item = queue_A_head->item;
	queue_A_node_t *temp = queue_A_head;
	queue_A_head = queue_A_head->next;
	if (queue_A_head == NULL) {
		queue_A_tail = NULL;
	}
	free(temp);
	return 0;
/* Add code END */

	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* Search the queue for 'item' and, if found, remove it from the queue.
 * Returns 0 if the item is found, or an error code if the item is not 
 * in the queue. 
 */
int queue_A_remove_from_queue(void *item)
{

/* Add code BEGIN */
	if (!queue_A_initialized) {
		return ERR_NOT_INITIALIZED;
	}
	else if (item == NULL) {
		return ERR_INVALID_ARG;
	}
	else if (queue_A_head == NULL){
		return ERR_EMPTY;
	}
	queue_A_node_t *curr = queue_A_head;
	queue_A_node_t *prev = curr;
	while (curr != NULL) {
		if (curr->item == item) {
			if (curr == queue_A_head) {
				queue_A_head = queue_A_head->next;
				if (queue_A_head == NULL) {
					queue_A_tail = NULL;
				}
			}
			else {
				prev->next = curr->next;
				
			}
			free(curr);
			return 0;
		}
		prev = curr;
		curr = curr->next;
	}
	return ERR_NO_SUCH_ITEM;
/* Add code END */

	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* Print the contents of the queue from head to tail.
 * Do not change the existing printf's, outside of the Add BEGIN/END markers.
 * Refer to tutorial handout for expected output format. 
 */
void queue_A_print_queue()
{
	printf("head: %p, tail: %p\n", queue_A_head, queue_A_tail);
	
/* Add code BEGIN */
	if (queue_A_initialized == false) {
		printf("NOT INITIALIZED\n");
		return;
	}
	else {
		queue_A_node_t *curr = queue_A_head;
		while (curr != NULL) {
			printf("[%p: %p] -> ", &curr, curr->item);
			curr = curr->next;
		}
	}	
/* Add code END */
	
	printf("(nil)\n");
}

/* Remove any items remaining in the queue and free any dynamically allocated 
 * memory used by the queue for these items, restoring the queue to the fresh, 
 * uninitialized state.
 * Returns 0 on success, or an error if the queue has not been initialized.
 */
int queue_A_destroy()
{

/* Add code BEGIN */
	if (!queue_A_initialized) {
		return ERR_NOT_INITIALIZED;
	}
	queue_A_node_t *curr = queue_A_head;
	while (curr != NULL) {
		curr->item = NULL;
		queue_A_node_t *temp = curr;
		curr = curr->next;
		free(temp);
	}
	queue_A_initialized = false;
	return 0;
/* Add code END */

	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;	
}

/* END of Part A */

/*************************************************
 * ------------------Part B:---------------------- 
 * In this part, you will implement a 
 * static queue with a max capacity using
 * the RING BUFFER introduced in the handout. 
 * DO NOT add any global (static) variables.
 *
 *************************************************/

bool queue_B_initialized = 0;

typedef struct queue_B_node {

/* Add code BEGIN */
	
	
/* Add code END */

	void *item;

} queue_B_node_t;

queue_B_node_t queue_B_nodes[PART_B_MAX_SIZE];

/* You may change the names and types of these 3 global variables.
 * You may not add any additional global variables.
 */  
int bufferLength = 0;
int writeIndex = 0;
int readIndex = 0;

/* Helper functions and macros only! */
/* Add code BEGIN */
/* Add code END */

/* Perform any initialization needed so that the queue data structure can be 
 * used. 
 * Returns 0 on success or an error if the queue has already been initialized.
 */
int queue_B_initialize()
{

/* Add code BEGIN */
	if (queue_B_initialized == 1) {
		return ERR_INITIALIZED;
	}
	else {
		queue_B_initialized = 1;
		bufferLength = 0;
		return 0;
	}
/* Add code END */

	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* Add item to the tail of the queue.
 * Returns 0 on success or an appropriate error code on failure.
 */
int queue_B_enqueue(void* item)
{

/* Add code BEGIN */
	if (queue_B_initialized == 0) {
		return ERR_NOT_INITIALIZED;
	}
	else if (bufferLength == PART_B_MAX_SIZE) {
		return ERR_FULL;
	}
	else {
		queue_B_nodes[bufferLength].item = item;
		bufferLength += 1;
		return 0;
	}
/* Add code END */

	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* Remove the item at the head of the queue and store it in the location
 * pointed to by 'item'.
 * Returns 0 on success or an appropriate error code on failure.
 */
int queue_B_dequeue(void** item)
{

/* Add code BEGIN */
	if (queue_B_initialized == 0) {
		return ERR_NOT_INITIALIZED;
	}
	else if (item == NULL) {
		return ERR_INVALID_ARG;
	}
	else if (bufferLength == 0) {
		return ERR_EMPTY;
	}
	else {
		*item = queue_B_nodes[0].item;
		bufferLength -= 1;
		int curr = 0;
		while (curr < bufferLength) {
			queue_B_nodes[curr].item = queue_B_nodes[curr + 1].item;
			curr++;
		}
		return 0;
	}
/* Add code END */
	
	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* Search the queue for 'item' and, if found, remove it from the queue.
 * Returns 0 if the item is found, or an error code if the item is not 
 * in the queue. 
 */
int queue_B_remove_from_queue(void *item)
{
	
/* Add code BEGIN */
	if (queue_B_initialized == 0) {
		return ERR_NOT_INITIALIZED;
	}
	else if (bufferLength == 0) {
		return ERR_EMPTY;
	}
	else {
		int result = -1;
		int currIndex = bufferLength - 1;
		while (currIndex >= 0) {
			if (queue_B_nodes[currIndex].item == item) {
				result = 0;
			}
			if (result == 0) {
				int old = currIndex;
				int next = old + 1;
				while (next < bufferLength) {
					queue_B_nodes[old].item = queue_B_nodes[next].item;
					old = next;
					next += 1;
				}
				queue_B_nodes[old].item = NULL;
				bufferLength -= 1;
				return 0;
			}
			currIndex--;
		}
		return ERR_NO_SUCH_ITEM;
	}
/* Add code END */

	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* Print the contents of the queue from head to tail.
 * Uncomment the first printf, and modify it to print the address of the 
 * head and tail of the queue. 
 * Refer to tutorial handout for expected output format. 
 */
void queue_B_print_queue()
{
	printf("head: %p, tail: %p\n", &queue_B_nodes[readIndex], &queue_B_nodes[writeIndex]);

	/* Add code BEGIN */
	if (queue_B_initialized == 0) {
		printf("NOT INITIALIZED\n");
		return;
	}
	int currIndex = 0;
	int tempBuffer = bufferLength;
	// int tempBuffer = writeIndex - readIndex;
	while (tempBuffer > 0) {
		printf("[%p: %p] -> ", &queue_B_nodes[currIndex], queue_B_nodes[currIndex].item);
		currIndex++;
		tempBuffer -= 1;
	}
	/* Add code END */
	
	printf("(nil)\n");
}

/* Remove any items remaining in the queue, restoring the queue to the fresh, 
 * uninitialized state.
 * Returns 0 on success, or an error if the queue has not been initialized.
 */
int queue_B_destroy()
{

/* Add code BEGIN */
	if (queue_B_initialized == 0) {
		return ERR_NOT_INITIALIZED;
	}
	else {
		int tempBuffer = bufferLength;
		// int tempBuffer = writeIndex - readIndex;
		for (int i = readIndex; tempBuffer > 0; i = (i + 1) % PART_B_MAX_SIZE) {
			queue_B_nodes[i].item = NULL;
			tempBuffer -= 1;
		}
		return 0;
	}
/* Add code END */
	
	/* Change the return value when you implement this function. */
	return ERR_NOT_IMPLEMENTED;
}

/* END of Part B */

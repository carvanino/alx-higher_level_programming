#include "lists.h"

/**
 * reserve_listint - reverses a linked list
 *
 * @head: A pointer to the first element in the list
 *
 * Return: A pointer to the beginning of the list
 *
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *transv, *nextnode;

	transv = *head;
	nextnode = *head;
	*head = NULL;

	while (nextnode != NULL)
	{
		nextnode = nextnode->next;
		transv->next = *head;
		*head = transv;
		transv = nextnode;
	}

	return (*head);
}

/**
 * listint_len - returns the number of element in a loinked list
 *
 * @head: pointer to the first element of the list
 *
 * Return: Number of element in the list
 */

size_t listint_len(listint_t *head)
{
	size_t no_nodes;
	listint_t *transv;

	transv = head;
	no_nodes = 0;
	while (transv != NULL)
	{
		no_nodes++;
		transv = transv->next;
	}
	return (no_nodes);
}

/**
 * is_palindrome - compared the linked list with its reversed if their equal
 *
 * @head: pointer to the first element in the list
 *
 * Return: 0 if it is not a palindrome
 * Otherwise: 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *rev_list, *transv, *mid_list;
	size_t nodes, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /*An Empty list or one with a single node */
	nodes = listint_len(*head); /* get the size of list */

	transv = *head;
	/* Get the middle of the list */
	for (i = 0; i < (nodes / 2) - 1; i++)
		transv = transv->next;
	if ((nodes % 2) == 0 && transv->n != transv->next->n)
		return (0);
	transv = transv->next->next;
	rev_list = reverse_listint(&transv);
	mid_list = rev_list;

	transv = *head;
	while (rev_list != NULL)
	{
		if (transv->n != rev_list->n)
			return (0);
		transv = transv->next;
		rev_list = rev_list->next;
	}
	reverse_listint(&mid_list);
	return (1);
}

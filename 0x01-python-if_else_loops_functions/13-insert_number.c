#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: ponter to the beginning of the list
 * @number: interger to be inserted into the list
 *
 * Return: address of newnode
 * Otherwise: NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *transv, *newnode;

	transv = *head;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		return (NULL);
	}
	newnode->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	while (transv->next != NULL)
	{
		if ((transv->next)->n >= number)
		{
			newnode->next = transv->next;
			transv->next = newnode;
			return (newnode);
		}
		transv = transv->next;
	}
	newnode->next = NULL;
	transv->next = newnode;
	return (newnode);
}

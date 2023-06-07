#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - a fun to insert node
 * @head: head of list
 * @number: number to be inserted
 * Return: address of node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node, *current;
node = malloc(sizeof(listint_t));
if (!node)
	return (NULL);
node->n = number;
node->next = NULL;
if (!(*head) || number < (*head)->n)
{
node->next = *head;
*head = node;
}
else
{
current = *head;
while (current->next && current->next->n <= number)
	current = current->next;
node->next = current->next;
current->next = node;
}
return (node);
}

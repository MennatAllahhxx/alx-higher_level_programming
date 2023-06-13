#include "lists.h"
/**
 * is_palindrome - to check palindrome
 * @head: head of list
 * Return: 1 if yes
 */
int is_palindrome(listint_t **head)
{
	listint_t *a, *b, *c;
	int i = 0, j, k;

	if (!head)
		return (1);
	a = *head;
	c = *head;
	while (a->next != NULL)
	{
		i++;
		a = a->next;
	}
	for (j = 0; j <= (i / 2); j++)
	{
		b = *head;
		for (k = 0; k <= (i - j); k++)
			b = b->next;
		if (c->n != b->n)
			return (0);
		c = c->next;
	}
	return (1);
}

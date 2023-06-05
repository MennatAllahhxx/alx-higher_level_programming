#include "lists.h"
/**
 * check_cyle - a fun to check
 * @list: list to be checked
 * Return: 0 if there's no cycle
 */
int check_cycle(listint_t *list)
{
listint_t *head, *current;
head = list;
current = list;
while(current != NULL)
{
current = current->next->next->next;
if (current == head)
	return (1);
}
return (0);
}

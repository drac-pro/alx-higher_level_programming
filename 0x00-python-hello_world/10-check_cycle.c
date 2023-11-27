#include "lists.h"

/**
 * check_cycle - finds loop in a linked list
 *
 * @list: pointer to first node of the list
 *
 * Return: pointer to node where loop starts
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

#include "lists.h"

/**
 * is_palindrome - checks if a single linked list is a palindrome
 *
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int len = 0, i, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	for (; current != NULL; current = current->next)
		len++;
	int array[len];

	current = *head;
	for (i = 0; i < len; i++)
	{
		array[i] = current->n;
		current = current->next;
	}

	for (i = len - 1, j = 0; i >= j; i--, j++)
	{
		if (array[j] != array[i])
			return (0);
	}
	return (1);
}

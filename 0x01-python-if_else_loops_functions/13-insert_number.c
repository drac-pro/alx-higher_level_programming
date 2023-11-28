#include "lists.h"

/**
 * insert_node - insert a number into a sorted linked list
 *
 * @head: pointer to the head of the list;
 * @number: number to be inserted
 *
 * Return: pointer to new node or NULL other wise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, new_node;

	if (**head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || *head->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	while (current && current->next && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}

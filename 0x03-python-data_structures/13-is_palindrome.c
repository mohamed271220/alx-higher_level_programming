#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to head of list
* Return: 1 if palindrome, 0 if not
*/


int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j, len;

	int arr[10000];

	if (*head == NULL)
		return (1);

	current = *head;
	len = 0;
	while (current != NULL)
	{
		arr[len] = current->n;
		current = current->next;
		len++;
	}

	for (i = 0, j = len - 1; i < len / 2; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}

	return (1);
}

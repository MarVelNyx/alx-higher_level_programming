#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function that checks if a
 * linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 = not/ 1 = is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int nodes = 0, i = 0, *arr = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		nodes++;
		temp = temp->next;
	}
	arr = malloc(sizeof(int) * nodes);
	temp = *head;
	while (temp)
	{
		arr[i++] = temp->n;
		temp = temp->next;
	}
	for (i = 0; i < nodes / 2; i++)
	{
		if (arr[i] != arr[nodes - 1 - i])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}

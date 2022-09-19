#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Checks if a singly linked list has a cycle in it
  * @list: The singly linked list to check
  *
  * Return: 1 if has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *head = list, *tail = list;
	int found = 0;

	while ((head && tail) && tail->next)
	{		
		head = head->next;

		if (tail->next || tail->next->next)	
			tail = tail->next->next;
		else
			break;

		if (head == tail)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
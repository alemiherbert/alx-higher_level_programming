#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (!list || !list->next)
		return (0);
	
	tmp = list;
	while (tmp->next)
	{
		if (tmp->next == list)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}


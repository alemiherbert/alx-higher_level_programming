#include "lists.h"
#include <stdio.h>
int get_length(listint_t **head)
{
    int length;
    listint_t *node = *head;

    for (length = 1; node->next; length++)
        node = node->next;
    return (length);
}



int is_palindrome(listint_t **head)
{
    int i, j, first, last;
    listint_t *node, *_node;

    i = 0;
    j = get_length(head) - 1;
    node = *head;

    if (!head)
        return (0);

    if (!*head)
        return 1;

    while (node && i < j)
    {
        _node = node;
        for (; _node && i < j; i++)
            _node = _node->next;

        first = node->n;
        last = _node->n;

        if (first != last)
            return 0;

        node = node->next;
        i++;
        j--;
    }

    return 1;
}


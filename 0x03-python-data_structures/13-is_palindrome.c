#include "lists.h"
#include <stdio.h>
unsigned int get_length(listint_t **head)
{
    unsigned int length;
    listint_t *node = *head;

    for (length = 1; node->next; length++)
        node = node->next;
    return (length);
}



int is_palindrome(listint_t **head)
{
    int i, j, pos, first, last, flag;
    listint_t *node, *_node;

    i = pos = 0;
    j = get_length(head);
    flag = 0;
    node = *head;
    while (!flag)
    {
        _node = node;
        for (first = _node->n; _node->next && pos < j; pos++)
            _node = _node->next;
        last = _node->n;
        
        if (first == last)
        {
            if (pos >= get_length(head) / 2)
                flag = 1;
            node = node->next;
            i++;
            j--;
        }
        else
            flag = 0;
    }

    return (flag);
}

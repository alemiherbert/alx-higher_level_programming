#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current_node, *temp_node;

    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;  

    if (!*head || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    current_node = *head;

    while (current_node->next)
    {
        if (current_node->next->n >= number)
        {
            temp_node = current_node->next;
            current_node->next = new_node;
            new_node->next = temp_node;
            return (new_node);
        }
        current_node = current_node->next;
    }

    current_node->next = new_node;
    return (new_node);
}

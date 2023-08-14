#include <stddef.h>
#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to pointer of first node of list
 * Return: void
 */
void reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer of first node of list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */

int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev_slow = NULL;
listint_t *second_half = NULL;
int result = 1;

if (*head != NULL && (*head)->next != NULL)
{
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

if (fast != NULL)
{
slow = slow->next;
}
second_half = slow;
reverse_listint(&second_half);

while (second_half != NULL)
{
if ((*head)->n != second_half->n)
{
result = 0;
break;
}
(*head) = (*head)->next;
second_half = second_half->next;
}

reverse_listint(&slow);
prev_slow->next = slow;
}
return (result);
}

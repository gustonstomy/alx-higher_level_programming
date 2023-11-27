#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: A pointer
 * Return: 0 if there is no cycle, 1 if there is a cyc
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;
	listint_t *p;

	ptr = list;
	p = list;
	while (list && ptr && ptr->next)
	{
		list = list->next;
		ptr = ptr->next->next;

		if (list == ptr)
		{
			list = p;
			p =  ptr;
			while (1)
			{
				ptr = p;
				while (ptr->next != list && ptr->next != p)
				{
					ptr = ptr->next;
				}
				if (ptr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}

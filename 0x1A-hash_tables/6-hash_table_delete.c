#include "hash_tables.h"

/**
 * hash_table_delete - Deletes a hash table.
 * @ht: A pointer to a hash table.
 */
void hash_table_delete(hash_table_t *ht)
{
	hash_table_t *head;
	hash_node_t *node;
	hash_node_t *temp;
	unsigned long int i;
  
	head = ht;
	
	for (i = 0; i < ht->size; i++)
  	{
    		if(ht->array[i] != NULL)
    		{
      			node = ht->array[i];
    		}
    		while (node != NULL)
    		{
      			temp = node->next;
      			free(node->value);
      			free(node->key);
			free(node);
      			node = temp;
    		}
  	}
  	free(ht->array);
  	free(head);
  
}

#include "hash_tables.h"

/**
 * hash_table_print - Prints a hash table.
 * @ht: A pointer to the hash table to print.
 *
 * Description: Key/value pairs are printed in the order
 *              they appear in the array of the hash table.
 */
void hash_table_print(const hash_table_t *ht)
{
    hash_node_t *node;
    unsigned int i;
    int comma = 0;

    if (ht == NULL)
    {
        return;
    }

    putchar('{');
    for (i = 0; i < ht->size; ++i)
    {
        node = ht->array[i];

        while(node != NULL) 
        {
            if (comma)
            {
                printf(", ");
            }
            printf("'%s': '%s'", node->key, node->value);
            node = node->next;
            comma = 1;
        }
    }
    puts("}");
}

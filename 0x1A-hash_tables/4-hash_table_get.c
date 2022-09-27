#include "hash_tables.h"

char *hash_table_get(const hash_table_t *ht, const char *key)
{
    hash_node_t *node;
    int position;

    position = key_index((const unsigned char *)key, ht->size);
    node = ht->array[position];

    if (node == NULL)
    {
        return 0;
    }

    while (node != NULL)
    {
        if (strcmp(node->key, key) == 0)
        {
            return node->value;
        }
        node = node->next;
    }
    return NULL; /* IF NOTHING IS FOUND */

}

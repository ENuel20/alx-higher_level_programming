#include "hash_tables.h"

/**
 * hash_table_create - Creates a hash table.
 * @size: The size of the hashtable array.
 *
 * Return: If an error occurs - NULL.
 *         Otherwise - a pointer to the new hash table.
 */
hash_table_t *hash_table_create(unsigned long int size)
{
    hash_table_t *ht;
    unsigned int i;

    ht = malloc(sizeof(hash_table_t));

    if (ht == NULL)
    {
        return 0;
    }

    ht->size = size;
    ht->array = malloc(sizeof(hash_table_t *) * size);

    for (i = 0; i < size; i++)
    {
        ht->array[i] = NULL; /* all spaces at each position
        is null for now */
    }

    return ht;
}

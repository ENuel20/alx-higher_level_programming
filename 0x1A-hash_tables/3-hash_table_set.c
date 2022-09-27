#include "hash_tables.h"

int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
    int position;
    hash_node_t *node;
    hash_node_t *new_node;

    position= key_index((const unsigned char *)key, ht->size);
    node = ht->array[position];

    if (node == NULL)
    {
        ht->array[position] = create_new_node(key, value); /* if
        node at that position is empty, create it */
        return (1);
    }
    while (node != NULL)
    {
        if (strcmp(node->key, key) == 0) /* key matches */
        {
            free(node->value); /* free existing value
            if there's any (for update) */
            node->value = strdup(value);
            return (1); /* code success */
        }
        node = node->next;
    }
    /*If key doesn't exist, create new node*/
        new_node = create_new_node(key, value);
    if (new_node == NULL)
	    return (0);

    new_node->next = ht->array[position];
    ht->array[position] = new_node;
    /* new node is chained */
    return (1);
}

/**
 * create_new_node - create a new node
 * @key: is the key. key can not be an empty string
 * @value: value associated with the key.
 * value must be duplicated. value can be an empty string
 * Return: 1 on success, 0 on failurre
 */

hash_node_t *create_new_node (const char *key, const char *value)
{
	hash_node_t *new_node;

	new_node = malloc(sizeof(hash_node_t));

	if (new_node == NULL)
		return (NULL);

	new_node->key = strdup(key);
	new_node->value = strdup(value);
	new_node->next = NULL;

	return (new_node);
}

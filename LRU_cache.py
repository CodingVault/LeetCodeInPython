#!/usr/bin/env python
# encoding: utf-8
"""
LRU_cache.py

Created by  on 2014-07-15.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

# https://oj.leetcode.com/problems/lru-cache/
# tags: hard, deque, hashtable, design

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""


############### doubly linked list ###############

class Element(object):
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next
    
    def __repr__(self):
        return '%s:%s -> %r' % (self.key, self.value, self.next)


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # self.head.next points at the oldest (least used) node,
        # self.tail points at the latest used node
        self.head = self.tail = Element(0, 0)
        self.capacity = capacity
        self.size = 0
        self.mapping = {}
    
    def append_to_tail(self, node):
        self.tail.next = node
        node.pre = self.tail
        node.next = None
        
        self.tail = node
    
    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    
    def move_to_tail(self, node):
        if node != self.tail:
            self.remove_node(node)
            self.append_to_tail(node)

    # @return an integer
    def get(self, key):
        if key in self.mapping:
            node = self.mapping[key]
            self.move_to_tail(node)
            return node.value
        
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        node = self.mapping.get(key)

        if node is None:
            # the key is not found; create a new node
            # note: do this before removing the first node
            #   in case there is only one node
            new_node = Element(key, value, self.tail)
            self.append_to_tail(new_node)
            self.mapping[key] = new_node
            self.size += 1

            if self.size > self.capacity:
                # note: self.head.next will be modified by
                #   self.remove_node, so make node a variable
                node = self.head.next
                self.remove_node(node)
                del self.mapping[node.key]
                self.size -= 1

        else:
            # the key exists; update the value and move the node
            # to the tail if necessary
            node.value = value
            self.move_to_tail(node)


############### TLE with singly linked list ###############


class Element(object):
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    """Note: `get` won't change the order in this version."""

    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = self.tail = Element(0, 0)
        self.capacity = capacity
        self.size = 0
        self.mapping = {}

    # @return an integer
    def get(self, key):
        return self.mapping.get(key, -1)

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.mapping[key] = value
        
        pre = self.head
        cursor = pre.next
        while cursor:
            if cursor.key == key:
                break
            pre = cursor
            cursor = pre.next
        
        if cursor is None:
            self.tail.next = Element(key, value)
            self.tail = self.tail.next
            self.size += 1
            
            if self.size > self.capacity:
                del self.mapping[self.head.next.key]
                self.head.next = self.head.next.next
                self.size -= 1
        
        else:
            cursor.value = value
            
            if cursor != self.tail:
                pre.next = cursor.next
                cursor.next = None
            
                self.tail.next = cursor
                self.tail = cursor
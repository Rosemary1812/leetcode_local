# ===== 146. LRU缓存机制 =====
# 难度: 中等
# 英文名: LRU Cache
# 来源: https://leetcode.cn/problems/lru-cache/description/
# 标签: codetop
#
# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
#
# 实现 `LRUCache` 类：
#
# - `LRUCache(int capacity)` 以正整数作为容量 `capacity` 初始化 LRU 缓存
# - `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 -1 。
# - `void put(int key, int value)` 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
# **进阶**：你是否可以在 `O(1)` 时间复杂度内完成这两种操作？
#
# 示例：
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
# ---------------------------------------------------------

# 思路：哈希表 + 双向链表。哈希表 O(1) 查找，双向链表 O(1) 插入/删除/移动。
#   get/put 时将节点移到链表头部（最近使用），容量满时删除链表尾部（最久未使用）。
#   Python 可用 OrderedDict 替代手写链表，内部就是哈希表+双向链表。
# 时间复杂度：get/put 均 O(1)
# 空间复杂度：O(capacity)

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))
lru.put(4, 4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))

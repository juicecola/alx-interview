0x01. Lockboxes
A lockbox interview question typically involves a scenario where you have multiple locked boxes, each potentially containing keys to other boxes. The goal is to determine if it is possible to unlock all the boxes starting from an initial unlocked box.

Here's a brief description of a typical lockbox interview question:

You are given n number of locked boxes, each numbered from 0 to n-1. The boxes are represented as a list of lists, where each inner list contains the keys present in that box. A key with the same number as a box can be used to unlock that box. However, there can also be keys that don't correspond to any boxes.

The task is to write a function, let's call it canUnlockAll(boxes), that determines whether it is possible to unlock all the boxes starting from the first box (boxes[0]). The function should return True if all the boxes can be opened, and False otherwise.

To solve this problem, you may need to simulate the process of trying out different keys and unlocking the corresponding boxes. You'll need to keep track of which boxes are unlocked and which keys you have at each step. The solution typically involves traversing the boxes and their keys, using data structures like lists or sets to track the unlocked boxes and available keys.

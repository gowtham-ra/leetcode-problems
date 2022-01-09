* I failed coming up with an approach other than full inorder traversal.
* The approach is split into two ways
* If right child is there - get the leftmost
* If right child is None - do inorder and update successor when prevNode = p
* Even better O(logN) approach is to use BST property
* If p.val >= node.val --> safely discard the left subtree
* else: mark potential successors until you reach null
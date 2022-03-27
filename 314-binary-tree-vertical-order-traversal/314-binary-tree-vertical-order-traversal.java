import java.util.*;
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<>();
        if (root == null)
            return new ArrayList<>();
        
        Map<Integer, List<Integer>> map = new HashMap<>();
        Queue<Pair<TreeNode, Integer>> que = new LinkedList<>();          
        que.add(new Pair(root, 0));
        
        while(!que.isEmpty()) {
            Pair<TreeNode, Integer> pair = que.remove();
            root = pair.getKey();
            int column = pair.getValue();
            
            if (!map.containsKey(column))
                map.put(column, new ArrayList<>());
            
            map.get(column).add(root.val);
            
            if (root.left != null)
                que.add(new Pair(root.left, column-1));
            if (root.right != null)
                que.add(new Pair(root.right, column+1));                    
        }
        
        List<Integer> keys = new ArrayList<>(map.keySet());
        Collections.sort(keys);        
        for (int key : keys) {
            output.add(map.get(key));
        }
        return output;        
    }
}
# public class Solution {
#     boolean left = true;
# 	  public List<Integer> borderView(TreeNode root) {
# 	    List<Integer>res = new ArrayList<Integer>();
# 	  	if (root==null) return res;
# 	  	preOrder(root, res);
# 	  	List<Integer>r = new ArrayList<Integer>();
#       if(root.right==null)return res;
# 	  	while(root.right!=null){
# 	  		r.add(0,root.key);
# 	  		root = root.right;
# 	    }
#       if(root.key!=res.get(res.size()-1))r.add(0,root.key);
# 	    r.remove(r.size()-1);
# 	  	res.addAll(r);
# 	  	return res;
# 	  }
# 	  public void preOrder(TreeNode root, List<Integer>res){
# 	  	if(root == null)return;
# 	  	if (left && root.left==null){
# 	  		left = false;
# 	  		res.add(root.key);
# 	    }
# 	  	else if(!left&&root.left==null && root.right==null){
# 	  		res.add(root.key);
# 	  		return;
# 	    }
# 	  	if (left) res.add(root.key);
# 	  	preOrder(root.left, res);
# 	  	preOrder(root.right, res);
# 	  }
# }

# public class Solution {
#   public int search(Dictionary dict, int target) {
#     if(dict.get(0)==null)return -1;
#   	if (dict.get(0)==target)return 0;
#   	int i = 1;
#   	while(dict.get(i)!=null && dict.get(i)<target){
#   		i = i*2;
#     }
#     if (dict.get(i)==null){    //corner case!!!!!!!!!
#       int first = i/2;
#       int end = i;
#       while(first<end){
#         int mid = (first+end)/2;
#       	if(dict.get(mid)==null){
#       		end = mid-1;
#         	continue;
#       	}else if(dict.get(mid)==target)return mid;
#         else if(dict.get(mid)>target)return findnum(dict, target, first, mid);
#         else{
#         	first = mid+1;
#         }
#       }
#       if (dict.get(first)==null ||dict.get(first)!=target) return -1;
#       else return first;
#     }else if (dict.get(i)==target) return i;
#     else{
#       return findnum(dict, target,0,i);
#   	}
#   }
#   public int findnum(Dictionary dict, int target, int first, int end){
#   		while (first<end){
#   			int mid = (first+end)/2;
#   			if (dict.get(mid)==target) return mid;
#   			else if (dict.get(mid)<target){
#   				first = mid+1;
#   				continue;
#       	}else{
#   				end = mid;
#   				continue;
#       	}
#     	}
#   		if (dict.get(first)==target) return first;
#   		return -1;
#   }
# }
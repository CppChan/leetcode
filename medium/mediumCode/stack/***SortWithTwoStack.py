# public class Solution {
# 	  public static void sort(LinkedList<Integer> s1) {
# 		    LinkedList<Integer> s2 = new LinkedList<Integer>();
# 		    int s1size = s1.size();
# 		    while(s1size>0){
# 		      int temp = s1.removeFirst();
# 		      if(s2.size()==0 || s2.getFirst()<temp){
# 		        s2.addFirst(temp);
# 		      }else{
# 		        int big = 0;
# 		        int s2size = s2.size();
# 		        while(s2size>0){
# 		          if (s2.getFirst()>temp){
# 		            s1.addFirst(s2.removeFirst());
# 		            big++;
# 		            s2size--;
# 		            continue;
# 		          }
# 		          break;
# 		        }
# 		        s2.addFirst(temp); #!!!!!!!!!attention , cannot write into the above loop, because when s2size==0, temp will not add into s2
# 		        for(int k = 0; k<big; k++){
# 		          s2.addFirst(s1.removeFirst());
# 		        }
# 		      }
# 		      s1size--;
# 		    }
# 		    Iterator iter = s2.iterator();
# 		    while(iter.hasNext()){
# 		      s1.addFirst((int) iter.next());
# 		    }
# 		  }
# 	}
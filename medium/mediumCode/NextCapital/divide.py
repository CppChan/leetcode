from collections import Counter
class Solution(object):
  def divide(self, input, multiple):
  	count_list,res = [],[]
  	for i in range(len(input)):
  		count_list.append(Counter(list(input[i])))
  	for j in range(len(count_list)):
  		temp_dict, temp_count = count_list[j].items(),0
  		for k in range(len(temp_dict)):
  			if temp_dict[k][1]>=multiple[j] and temp_dict[k][1]%multiple[j]==0:temp_count+=1
  		res.append(temp_count)
  	return res


if __name__ == "__main__":
    s = Solution()
    print s.divide(["aaabbcccc","ddfffg","ccccdds","sfesd"],[2,3,4,1])
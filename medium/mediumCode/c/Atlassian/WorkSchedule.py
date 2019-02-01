class Solution(object):
  def workSchedule(self, week, day, schedule):
  	schedule, slot, res= list(schedule), [],[]
  	for i in range(len(schedule)):
  		if schedule[i]=="?": slot.append(i)
  		else: week-=int(schedule[i])
	if week==0 and len(slot)==0:return ["".join(schedule)]#corner?
  	if week<0 or len(slot)*day<week: return[] #corner!!!!
  	self.dfs(schedule, slot, res, week, day,0)
  	return res

  def dfs(self, schedule, slot, res, week, day, index):
  	if index == len(slot)-1:
  		schedule[slot[index]]=str(week)
  		res.append("".join(schedule))
  	else:
  		for i in range(min(day+1, week+1)):
  			if (len(slot)-index-1)*day<week-i:continue
  			schedule[slot[index]]=str(i)
  			self.dfs(schedule, slot, res, week-i,day, index+1)


if __name__ == "__main__":
    s = Solution()
    print s.workSchedule(24, 4, '0864330')
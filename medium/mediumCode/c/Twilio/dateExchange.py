class Solution(object):
    def change(self,input):
        dic = {'Jan':"01","Feb":"02", "Mar":"03", "Apr":"04","May":"05","Jun":"06", "Jul":"07", "Aug":"08", "Sept":"09", "Oct":"10","Nov":"11","Dec":"12"}
        temp = input.split(" ")
        year, month, date = temp[2], dic[temp[0]], temp[1]
        if len(date)==3: date = "0"+date[0]
        else:date = date[:2]
        print year+"-"+month+"-"+date

if __name__=="__main__":
    s = Solution()
    s.change("Oct 2nd 2010")
    s.change("Jan 21st 2010")
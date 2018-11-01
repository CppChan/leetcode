#找符合domain 的出现次数最多的timestamp testcase没过

from collections import defaultdict
def max_logs(domain, logs):
    date_count,res = defaultdict(lambda: 0),[0,""]
    for i in range(len(logs)):
        if len(logs[i])==0:continue
        process(logs[i], date_count, domain, res)
    return res[1]
def process(log, date_count, domain, res):
    email_date = log.split('.com')
    email,date = email_date[0],email_date[1]
    domain_ = email.split("@")[1]
    if domain_ == domain:
        date_count[date]+=1
        if res[0]<date_count[date]:
            res[0] = date_count[date]
            res[1] = date
if __name__ == "__main__":
    print max_logs("organisation2.com", ['user1@organisation1.com20180910',
'user3@organisation1.com20180912',
'user4@organisation1.com20180912',
'user2@organisation2.com20180912',
'user2@organisation1.com20180911',
'user4@organisation2.com20180912',
'user5@organisation2.com20180910',
'user6@organisation2.com20180910',
'user2@organisation1.com20180910'])
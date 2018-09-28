for param_name in sorted(parameters.keys()):


#use zip to make a tuple , and sort based on abs(k)'s value
for k,v in sorted(zip(map(lambda x: round(x, 4), LRmodel_l1.coef_[0]),
                      churn_feat_space.columns), key=lambda x: x[0] * -1):


for i, topic_dist in enumerate(topic_word):#enumerate(): used to generate a combination of element and its index
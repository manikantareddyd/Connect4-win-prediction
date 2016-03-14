from vectorize import *
import sys
from sklearn.svm import LinearSVC
from sklearn.metrics import *

train_vectors,train_labels,test_vectors,test_labels = get_data(int(sys.argv[1]))
win=[]
draw=[]
loss=[]

# print "Data Read"
for i in range(len(train_vectors)):
    if train_labels[i]==1:
        win.append(train_vectors[i])
    elif train_labels[i]==0:
        draw.append(train_vectors[i])
    else:
        loss.append(train_vectors[i])
# print "Data Classified"
win_l = ['1' for i in win]
draw_l = ['0' for i in draw]
loss_l = ['-1' for i in loss]

# print "Building win draw classifier"
classifier_win_draw = LinearSVC()
classifier_win_draw.fit(win+draw,win_l+draw_l)

# print "Building draw loss classifier"
classifier_draw_loss = LinearSVC()
classifier_draw_loss.fit(draw+loss,draw_l+loss_l)

# print "Building loss win classifier"
classifier_loss_win = LinearSVC()
classifier_loss_win.fit(loss+win,loss_l+win_l)

predictions=[]
for i in range(len(test_vectors)):
    t_w_d   =   int(classifier_win_draw.predict([test_vectors[i]])[0])
    t_d_l   =   int(classifier_draw_loss.predict([test_vectors[i]])[0])
    t_l_w   =   int(classifier_loss_win.predict([test_vectors[i]])[0])
    t       =   [t_w_d,t_d_l,t_l_w]
    if t==[1,0,-1] or t==[0,-1,1]: p=1
    elif t==[1,0,1] or t==[1,-1,1]: p=1
    elif t==[0,0,-1] or t==[0,0,1]: p=0
    else: p=-1
    predictions.append((p))

print "*"*80
print classification_report(test_labels,predictions)
print confusion_matrix(test_labels,predictions,labels=[1,0,-1])
print "*"*80

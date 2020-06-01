from sklearn.datasets import load_iris;
from sklearn.model_selection import train_test_split
from scipy.spatial import  distance
from sklearn.metrics import accuracy_score;

def euc(a,b):
	return distance.euclidean(a,b)

class KNN():

	def fit(self,train_data,train_target):
		self.training_data=train_data;
		self.training_target=train_target;


	def closest(self,row):
		bestdistance=euc(row,self.training_data[0])
		bestindex=0;

		for i in range(len(self.training_data)):
			dist=euc(row,self.training_data[i])
			if dist<bestdistance:
				bestdistance=dist;
				bestindex=i;

		return self.training_target[bestindex];		


	def predict(self,test_data):

		prediction=[];

		i=0;
		for row in test_data:
			i+=1;

			label=self.closest(row);
			prediction.append(label);

		return prediction;		

def KnnAlgorithm():
	iris=load_iris();

	features=iris.data;
	target=iris.target;

	features_train,features_test,target_train,target_test=train_test_split(features,target,test_size=0.5);

	classifier=KNN();

	classifier.fit(features_train,target_train);

	prediction=classifier.predict(features_test);

	Accuracy=accuracy_score(target_test,prediction);
	print("\nUserdefined KnnAlgorithm Accuracy is ",Accuracy*100,"% ");

def main():
	KnnAlgorithm();

if __name__ == '__main__':
	main()
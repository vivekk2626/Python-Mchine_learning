from sklearn.datasets import load_iris;
from sklearn import tree;
from sklearn.neighbors import KNeighborsClassifier;
from sklearn.model_selection import train_test_split;
from sklearn.metrics import accuracy_score;


def DecisionAccuracy(iris):

	print("Fetaures Extracted :")
	features=iris.data;

	print("Target Extracted :\n")
	target=iris.target;

	features_train,features_test,target_train,target_test=train_test_split(features,target,test_size=0.5);

	classifier=KNeighborsClassifier();

	classifier.fit(features_train,target_train);

	prediction=classifier.predict(features_test);

	Accuracy=accuracy_score(target_test,prediction);

	Accuracy=Accuracy*100;

	return Accuracy;


def KnnAccuracy(iris):
	
	features=iris.data;

	target=iris.target;

	features_train,features_test,target_train,target_test=train_test_split(features,target,test_size=0.5);

	classifier=tree.DecisionTreeClassifier();

	classifier=classifier.fit(features_train,target_train);

	prediction=classifier.predict(features_test);

	Accuracy=accuracy_score(target_test,prediction);

	Accuracy=Accuracy*100;

	return Accuracy;


def main():

	iris=load_iris();
	AccuracyDecision=DecisionAccuracy(iris);
	AccuracyKNN=KnnAccuracy(iris);

	print("DecisionAccuracy :",AccuracyDecision);
	print("\nKNeighborsAccuracy:",AccuracyKNN);



	if(AccuracyDecision>AccuracyKNN):
		print("\nDecisionTreeClassifier is Efficient With :",AccuracyDecision,"% Accuracy ...");
	else:
		print("\nKNN Classifier is Efficient With :",AccuracyKNN,"% Accuracy ...");	


if __name__ == '__main__':
	main()
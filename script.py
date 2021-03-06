# STEPS
# get the data from csv file
# get the features and labels
# do the processing
# split the training and test data set
# define a classifier
# get the score

class DataProcessing:
    def __init__(self, filePath):
        self.csv_file_path = filePath
        self.data_frame = None
        self.features = None
        self.labels = None
        self.X_train = None
        self.Y_train = None
        self.X_test = None
        self.Y_test = None

    # get the data from csv file
    def get_data_from_csv(self):
        import pandas
        self.data_frame = pandas.read_csv(self.csv_file_path)

    # get the features and labels
    def get_features_and_labels(self):
        import numpy
        self.labels = numpy.array(self.data_frame['label'])
        self.features = numpy.array(self.data_frame.drop(['label'], 1))

    # scaling the values propotionally
    def do_scaling(self):
        from sklearn.preprocessing import scale
        scale(self.features)

    # split the training and test data set
    def split_train_and_test_data(self):
        from sklearn.model_selection import train_test_split
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.features, self.label, test.size = 0.3)

class ClassificationAlgorithms:
    def __init__(self):
        self.classifier = None

    # define a classifier
    def get_classifier(self, classifier_type, X_train, Y_train):
        if(classifier_type == 'knn'):
            from sklearn import neighbors
            self.classifier = neighbors.kneighbors.classifier().fit(X_train, Y_train)

    # get the score
    def get_score(self, X_test, Y_test):
        print(self.classifier.score(X_test, Y_test))

def main():
    dp = DataProcessing('enterCSVFilePathHere')
    dp.get_data_from_csv
    dp.get_features_and_labels
    dp.do_scaling
    dp.split_train_and_test_data

    ClassificationObject = ClassificationAlgorithms()
    ClassificationObject.get_classifier('knn', dp.X_train, dp.Y_train)
    ClassificationObject.get_score(dp.X_test, dp.Y_test)

main()

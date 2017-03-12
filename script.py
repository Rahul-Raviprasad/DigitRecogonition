# get the data from csv
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

    def get_data_from_csv(self):
        import pandas
        self.data_frame = pandas.read_csv(self.csv_file_path)

    def get_features_and_labels(self):
        import numpy
        self.labels = numpy.array(self.data_frame['label'])
        self.features = numpy.array(self.data_frame.drop(['label'], 1))

    def do_scaling(self):
        from sklearn.preprocessing import scale
        scale(self.features)

    def split_train_and_test_data(self):
        from sklearn.model_selection import train_test_split
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.features, self.label, test.size = 0.3)

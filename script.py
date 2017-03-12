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

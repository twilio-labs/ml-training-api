import logging
import pickle
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn import metrics
from datetime import datetime

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Model:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def fetch_data(self):
        self.logger.info("Downloading data...")
        self.train_data = fetch_20newsgroups(subset='train')
        self.test_data = fetch_20newsgroups(subset='test')
        self.y_train = self.train_data.target
        self.y_test = self.test_data.target

    def feat_eng(self):
        self.vectorizer = TfidfVectorizer()
        self.X_train = self.vectorizer.fit_transform(self.train_data.data)
        self.X_test = self.vectorizer.transform(self.test_data.data)

    def train_test_split(self):
        # Placeholder for train test split
        pass

    def fit(self, training_parameters=None):
        self.logger.info(f'external parameters {training_parameters}')
        self.clf = MultinomialNB()
        hparams = self.clf.get_params()
        if training_parameters:
            hparams = dict((k, training_parameters.get(k, v)) for k, v in hparams.items())
        self.clf.set_params(**hparams)
        self.logger.info(f'Fitting the model with hparams {hparams}')

        # fit model
        self.clf.fit(self.X_train, self.y_train)
        t = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        pickle.dump(self.clf, open(f"model_{t}.pkl", "wb"))
        return f"model_{t}.pkl"

    def evaluate(self):
        self.logger.info("Evaluating the model...")
        pred = self.clf.predict(self.X_test)
        return metrics.f1_score(self.y_test, pred, average='macro')

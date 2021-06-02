from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)  # 1은 세로, 0은 가로?

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:  # Delete useless data
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        # print(f'Type Check {type(this.train["Embarked"])}')
        # map 함수를 사용하여 S: 1, C: 2, Q: 3
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train['Embarked'] = this.train['Embarked'].map(embarked_mapping)
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        #
        # this.train.loc[(this.train.Embarked == 'S'), 'Embarked'] = 1
        # this.train.loc[(this.train.Embarked == 'C'), 'Embarked'] = 2
        # this.train.loc[(this.train.Embarked == 'Q'), 'Embarked'] = 3
        # this.test.loc[(this.test.Embarked == 'S'), 'Embarked'] = 1
        # this.test.loc[(this.test.Embarked == 'C'), 'Embarked'] = 2
        # this.test.loc[(this.test.Embarked == 'Q'), 'Embarked'] = 3
        return this

    @staticmethod
    def title_nominal(this) -> object:
        # this.train = this.train.fillna({'Title': 0})
        # this.test = this.test.fillna({'Title': 0})
        combine = [this.train, this.test]
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            dataset['Title'] = dataset['Title'].fillna(0)   # fillna(0) # 0은 호칭이 없는 극빈, 노예.
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        combine = [this.train, this.test]
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3,
                             'Student': 4, 'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for dataset in combine:
            dataset['Age'] = dataset['Age'].fillna(-0.5)
            dataset['AgeGroup'] = pd.cut(dataset['Age'], bins=bins, labels=labels)
            dataset['AgeGroup'] = dataset['AgeGroup'].map(age_title_mapping)
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        # print(this.test[this.test.isna().any(axis=1)].isna())
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # print(this.train['FareBand'].head(10))
        # bins = [-1, 7.91, 14.454, 31.0, np.inf]
        # print(list(pd.qcut(this.train['Fare'], 4, retbins=True))[1])
        res, bins = list(pd.qcut(this.train['Fare'], 4, retbins=True))
        print(res)
        print(bins)
        bins[0] = -1
        bins[4] = np.inf
        print(bins)
        # list 구조로 0번 인덱스는 문자이며, 2번째 인덱스가구간 값.
        for these in [this.train, this.test]:
            these['FareBand'] = pd.cut(these['Fare'], bins=bins, labels=[1, 2, 3, 4])
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def accuracy_by_svm(this):
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10,
                                         shuffle=True,
                                         random_state=0),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)

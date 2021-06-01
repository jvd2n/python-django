from titanic.models.dataset import Dataset
import pandas as pd


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
    def drop_feature(this, feature) -> object:  # Delete useless data
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
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
    def fare_band_fill_na(this) -> object:
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
        return this

    @staticmethod
    def create_k_fold(this) -> object:
        return this

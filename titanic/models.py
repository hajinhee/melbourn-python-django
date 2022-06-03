import numpy as np
import pandas as pd
from icecream import ic
from context.domains import Dataset
from context.models import Model
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier    # Classifier 분류
# from sklearn.ensemble import RandomForestRegressor   # Regressor 회귀


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname) -> object:    # Hook : __init__ 과는 결합도를 높이고 나머지 메소드와는 결합도를 낮춘다.
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
                   'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']   # id = 문제
        this.label = this.train['Survived']  # label = 정답
        this.train.drop('Survived', axis=1, inplace=True)  # axis = 축의 방향, 1=column, 0=row
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket', 'Cabin')  # garbage 삭제
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')
        k_fold = self.create_k_fold()
        accuracy = self.get_accuracy(this, k_fold)
        ic(accuracy)
        '''
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.name_nominal(this)
        this = self.age_ratio(this)
        this = self.sex_nominal(this)
        this = self.embarked_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        '''
        # self.kwargs_sample(name='이순신')
        # self.name_nominal(this)
        # self.df_info(this)
        return this

    def learning(self, train_fname, test_fname):
        this = self.preprocess(train_fname, test_fname)
        k_fold = self.create_k_fold()
        ic(f'사이킷런 알고리즘 정확도: {self.get_accuracy(this, k_fold)}')
        self.submit(this)

    @staticmethod
    def submit(this):
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./save/submission.csv', index=False)

    @staticmethod
    def df_info(this) -> None:
        [print(f'{i.info()}') for i in [this.train, this.test]]  # columns, null-count, Dtype
        ic(this.train.head(5))
        ic(this.test.head(5))

    @staticmethod
    def null_check(this) -> None:
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this) -> None:
        ic(f'id 의 타입  {type(this.id)}')
        ic(f'id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def print_this(this) -> None:
        print('*'*100)
        ic(f'1. Train 의 타입 : {type(this.train)}\n')        # this.train, this.test, this.id = 객체, property => 앞으로 가공할거라
        ic(f'2. Train 의 컬럼 : {this.train.columns}\n')
        ic(f'3. Train 의 상위 1개 : {this.train.head(1)}\n')   # ()가 있는 건 메소드
        ic(f'4. Train 의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5. Test 의 타입 : {type(this.test)}\n')
        ic(f'6. Test 의 컬럼 : {this.test.columns}\n')
        ic(f'7. Test 의 상위 1개 : {this.test.head(1)}\n')
        ic(f'8. Test 의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'9. id 의 타입 : {type(this.id[:10])}\n')
        print('*' * 100)

    @staticmethod
    def drop_feature(this, *feature) -> object:  # Asterisk(*): 여러 개의 인자 값을 tuple 형태로 한 번에 받음
        # for i in feature:
        #     this.train.drop(i, axis=1, inplace=True)
        #     this.test.drop(i, axis=1, inplace=True)
        # [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]
        [i.drop(list(feature), axis=1, inplace=True) for i in [this.train, this.test]]
        return this

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs))
        {print(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()}  # key: name, val: 이순신
    '''
    Categorical vs. Quantitative
    Cate -> nominal(이름) vs. ordinal(순서)
    Quan -> interval(상대적) vs. ratio(절대적)
    '''

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def extract_title_from_name(this) -> object:  # train, test => df(object)
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.', expand=False)  # 정규식
        return this

    @staticmethod
    def remove_duplicate(this) -> dict:    # 실제로 삭제 하는 게 아니라 어떤 신분이 있는 지 확인만!
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))  # Train과 Test 각각 중복 제거
        a = list(set(a))  # 2개 파일의 중복 제거
        # print(f'>>> {a}')
        # [these.drop_duplicates(subset=['Title'], inplace=True) for these in [this.train, this.test]]
        # ↑ 실제로 컬럼에 있는 중복 값들을 모두 제거 하는 함수
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for these in [this.train, this.test]:         # replace: 컬럼 내의 일부 단어를 바꿀 때 사용
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화 없음
            # Mrs 는 변화 없음
            these['Title'] = these['Title'].fillna(0)  # 결측치(NaN)는 노동자 계급으로
            these['Title'] = these['Title'].map(title_mapping)  # 자연어를 기계어로 변환
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # scaling
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in [this.train, this.test]:
            these['Age'] = these['Age'].fillna(-0.5)   # 결측치(누락 데이터/NaN) 치환 처리
            these['AgeGroup'] = pd.cut(these['Age'], bins, labels=labels)
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        fare_mapping = {1, 2, 3, 4}
        # bins = [-1, 8, 15, 31, np.inf]  # np.inf: 무한대
        for these in [this.train, this.test]:
            these['Fare'] = these['Fare'].fillna(1)
            these['FareBand'] = pd.qcut(these['Fare'], 4, fare_mapping)  # pd.qcut(데이터, 범위, 맵핑)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})  # test에는 NaN값이 없어서 train에만
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)  # shuffle=True 중복 출제 허용

    @staticmethod
    def get_accuracy(this, k_fold):
        score = cross_val_score(RandomForestClassifier(), this.train, this.label, cv=k_fold, n_jobs=1, scoring='accuracy')
        return round(np.mean(score)*100, 2)  # *백분률, 평균
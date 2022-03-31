import random
import string
import numpy as np
import pandas as pd
from icecream import ic

from context.models import Model
from hello.domains import members


class Quiz30:
    '''
    데이터프레임 문제 Q02
    ice df:     A   B   C
            1   1   2   3
            2   4   5   6
            3   7   8   9
            4   10  11  12
    '''
    def quiz30_df_4_by_3(self) -> str:
        # l1 = [i for i in range(1, 4)]
        # l2 = [i for i in range(4, 7)]
        # l3 = [i for i in range(7, 10)]
        # l4 = [i for i in range(10, 13)]
        # l5 = [l1, l2, l3, l4]
        l6 = [[i for i in range(j * 3 + 1, j * 3 + 4)] for j in range(4)]
        df = pd.DataFrame(l6, index=range(1, 5), columns=['A', 'B', 'C'])
        ic(df)
        # d1 = {'1':l1,'2':l2,'3':l3,'4':l4}
        # d2 = pd.DataFrame.from_dict(d, orient='index', columns=['A', 'B', 'C'])
        return None

    '''
    데이터프레임 문제 Q03. 
    두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
    ic| df:     0   1   2
            0  97  57  52
            1  56  83  80
    '''
    def quiz31_rand_2_by_3(self) -> str:
        '''
        l1 = [myRandom(10, 99) for i in range(3)]
        l2 = [myRandom(10, 99) for i in range(3)]
        l3 = list([myRandom(10, 99) for i in range(3)] for i in range(2))
        df = pd.DataFrame(l3, index=range(2), columns=range(3))
        '''
        # numpy 사용한 예제
        df = pd.DataFrame(np.random.randint(10, 99, size=(2, 3)))
        ic(df)
        return None

    '''
    데이터프레임 문제 Q04.
    국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
    단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
    ic| df4:        국어  영어  수학  사회
            lDZid   57   90   55    24
            Rnvtg   12   66   43    11
            ljfJt   80   33   89    10
            ZJaje   31   28   37    34
            OnhcI   15   28   89    19
            claDN   69   41   66    74
            LYawb   65   16   13    20
            QDBCw   44   32    8    29
            PZOTP   94   78   79    96
            GOJKU   62   17   75    49
        '''
    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

    def quiz32_df_grade(self) -> str:
        data = np.random.randint(0, 101, (10, 4))
        idx = [self.id(5) for i in range(10)]
        col = ['국어', '영어', '수학', '사회']

        df_list = pd.DataFrame(data, idx, col)
        ic(df_list)

        df_dict = pd.DataFrame.from_dict(dict(zip(idx, data)), orient='index', columns=col)
        ic(df_dict)
        return None

    def quiz33_df_loc(self) -> str:
        # key = ['a', 'b', 'c', 'd']
        # value = np.random.randint(0, 100, (4, 3))
        # d = [{i:j for i, j in zip(['a', 'b', 'c', 'd'], np.random.randint(0, 100, 4))} for i in range(3)]
        df = self.createDf(keys=['a', 'b', 'c', 'd'],
                           vals=np.random.randint(0, 100, 4),
                           len=3)
        # ic(df)
        subjects = ['자바', '파이썬', '자바스크립트', 'SQL']
        scores = np.random.randint(0, 100, (24, 4))
        students = members()
        students_scores = {students: scores for students, scores in zip(students, scores)}  # dict(zip(students, scores))
        df = pd.DataFrame.from_dict(students_scores, orient='index', columns=subjects)
        # ic(df)
        model = Model()
        grade_df = model.new_model(fname='grade.csv')

        print('Q1. 파이썬의 점수만 출력하시오')
        python_scores = grade_df.loc[:, '파이썬']
        print(type(python_scores))       # Series => indexing
        ic(python_scores)

        print('Q2. 조현국의 점수만 출력하시오')
        cho_scores = grade_df.loc['조현국']
        print(type(cho_scores))          # Series => indexing
        ic(cho_scores)

        print('Q3. 조현국의 과목별 점수를 출력하시오')
        cho_subjects_scores = grade_df.loc[['조현국']]
        print(type(cho_subjects_scores))  # DataFrame => slicing
        ic(cho_subjects_scores)
        return None

    @staticmethod
    def createDf(keys, vals, len):
        return pd.DataFrame([dict(zip(keys, vals)) for i in range(len)])

    def quiz34_df_iloc(self) -> str:
        # ic(df.iloc[0])
        '''
        ic| df.iloc[0]: a    15
                        b    14
                        c    12
                        d    47
                        Name: 0, dtype: int32
        '''
        # ic(df.iloc[[0]])
        '''
        ic| df.iloc[[0]]:     a  b   c   d
                          0  99  0  76  77
        '''
        # ic(df.iloc[[0, 1]])
        '''
        ic| df.iloc[[0, 1]]:     a   b   c   d
                             0  75  15  58  99
                             1  75  15  58  99
        '''
        # ic(df.iloc[:3])
        '''
        ic| ddf.iloc[:3]:       a   b   c   d
                            0  51  84  36  77
                            1  51  84  36  77
                            2  51  84  36  77
        '''
        # ic(df.iloc[[True, False, True]])
        '''
        ic| df.iloc[[True, False, True]]:      a   b   c   d
                                           0  22  56  78  68
                                           2  22  56  78  68
        '''
        # ic(df.iloc[0, 1])
        '''
        ic| df.iloc[0, 1]: 7
        '''
        # ic(df.iloc[0, 2], [1, 3])
        '''
        ic| df.iloc[0, 2]: 41, [1, 3]
        '''
        # ic(df.iloc[:, [True, False, True, False]])
        '''
        ic| df.iloc[:, [True, False, True, False]]:     a   c
                                                    0  75  71
                                                    1  75  71
                                                    2  75  71
        '''
        # ic(df.iloc[:, lambda df: [0, 2]])
        '''
        ic| df.iloc[:, lambda df: [0, 2]]:     a   c
                                            0  86  90
                                            1  86  90
                                            2  86  90
        '''
        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
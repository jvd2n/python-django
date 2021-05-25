class Member(object):
    m_id = ''
    pwd = ''
    email = ''
    phone = ''

    # def __init__(self, m_id, pwd, email, phone):
    #     self.m_id = m_id
    #     self.pwd = pwd
    #     self.email = email
    #     self.phone = phone

    def join(self, m_id, pwd, email, phone):
        self.m_id = m_id
        self.pwd = pwd
        self.email = email
        self.phone = phone

    def login(self, m_id, pwd):
        if self.m_id == m_id and self.pwd == pwd:
            print(f'{m_id}님, 환영합니다.')
        else:
            print(f'잘못된 입력입니다.')

    def change_pwd(self, orig_pwd, new_pwd):
        if self.pwd == orig_pwd:
            self.pwd = new_pwd
        else:
            pass

    def to_string(self):
        return f'{self.m_id}, {self.email}, {self.phone}'

    @staticmethod
    def main():
        member = Member()
        while 1:
            menu = input('1 JOIN 2 LOGIN 3 MYPAGE '
                         '4 UPDATE 5 REMOVE\n0 EXIT\n>> ')
            if menu == '1':
                member.join(input('id? '), input('pwd? '),
                            input('email? '), input('phone? '))
            elif menu == '2':
                member.login(input('your id : '), input('your pw : '))
            elif menu == '3':
                print(member.to_string())
            elif menu == '0':
                break


Member.main()

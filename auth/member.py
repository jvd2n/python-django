class Member(object):
    # m_id = ''
    # pwd = ''
    # email = ''
    mem_list = []

    def __init__(self, m_id=None, pwd=None, email=None):
        if m_id is None and pwd is None and email is None:
            print('Default Constructor')
        else:
            self.m_id = m_id
            self.pwd = pwd
            self.email = email
            print('__init__ Constructor')

    def __str__(self):
        return f'{self.m_id}({self.email})'

    def join(self, m_id, pwd, email):
        is_exist = False
        for i in self.mem_list:
            if i.m_id == m_id:
                is_exist = True
        if is_exist:
            print(f'ERROR : {m_id} is N/A')
        else:
            self.mem_list.append(Member(m_id, pwd, email))
            print(f'SUCCESS : {m_id} JOINED')

    def login(self, m_id, pwd):
        is_exist = False
        for i in self.mem_list:
            if i.m_id != m_id:
                continue
            else:
                is_exist = True
                if i.pwd == pwd:
                    print(f'Welcome, {m_id}')
                else:
                    print('Wrong Password')
        if is_exist:
            pass
        else:
            print('There is no ID')

    def member_info(self):
        for i, j in enumerate(self.mem_list):
            print(f'|{i}| {j}')

    @staticmethod
    def main():
        member = Member()
        mem_ls = []
        while 1:
            menu = input('1 JOIN 2 LOGIN 3 MEMBER_INFO\n'
                         '4 UPDATE 5 REMOVE\n0 EXIT\n>> ')
            if menu == '1':
                member.join(input('id? '), input('pwd? '), input('email? '))
            elif menu == '2':
                member.login(input('your id : '), input('your pw : '))
            elif menu == '3':
                member.member_info()
            elif menu == '4':
                pass
            elif menu == '5':
                pass
            elif menu == '0':
                break
            else:
                print('Wrong Menu NO.')


Member.main()

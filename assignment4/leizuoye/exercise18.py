#coding:utf-8

import exercise4 
User_Mange=exercise4.User_Mange

class userpwd_Mange(User_Mange):
    def change_pwd(self,name,password):
        if (name in self.user_text) and self.check_pwd(name,password):
            ntime=exercise4.time.time()
            self.user_text[name].update({password:ntime})
        else:
            print("账号错误或密码曾经存在")
    def check_pwd(self,name,this_pwd):
        if name in self.user_text:
            if this_pwd not in self.user_text[name]:
                return True
        return False 
    def login(self,login_name):
        get_keydict = self.user_text.get(login_name)
        ctime =0
        for cpwd in get_keydict:
            if get_keydict[cpwd]>ctime:
                get_keydict[cpwd]
                right_key = cpwd
        if exercise4.time.time()-get_keydict[cpwd]>(365*24*60*60):
            print("超过12个月未修改密码，请修改后登陆")
            return None
        else:
            return super(userpwd_Mange,self).login(login_name)


a1 =userpwd_Mange()
a1.add_user("python", "123456")
a1.change_pwd("python","56789")
a1.add_user("diannao","987654")
a1.change_pwd("diannao","963258")
a1._User_Mange__echo_user()
a1.login("python")

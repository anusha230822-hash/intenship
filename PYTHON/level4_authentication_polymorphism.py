from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self, user, cred):
        pass

class PasswordAuth(Authentication):
    def __init__(self, store):
        self.store = store
    def login(self, user, cred):
        return self.store.get(user) == cred

class OTPAuth(Authentication):
    def __init__(self, valid_otps):
        self.valid_otps = valid_otps
    def login(self, user, cred):
        return cred in self.valid_otps

if __name__ == '__main__':
    pa = PasswordAuth({'u':'p'})
    oa = OTPAuth({'1234'})
    print('PasswordAuth', pa.login('u','p'))
    print('OTPAuth', oa.login('x','1234'))

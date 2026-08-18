from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self, user, credential):
        pass

class PasswordAuth(Authentication):
    def __init__(self, store):
        self.store = store
    def login(self, user, credential):
        return self.store.get(user) == credential

class OTPAuth(Authentication):
    def __init__(self, valid_otps):
        self.valid_otps = valid_otps
    def login(self, user, credential):
        return credential in self.valid_otps

class GoogleLogin(Authentication):
    def login(self, user, credential):
        return credential == 'google_token'

class Biometric(Authentication):
    def login(self, user, credential):
        return credential == 'biometric_hash'

if __name__ == '__main__':
    pa = PasswordAuth({'u':'p'})
    oa = OTPAuth({'1111'})
    gl = GoogleLogin()
    bio = Biometric()
    print('Password', pa.login('u','p'))
    print('OTP', oa.login('x','1111'))
    print('Google', gl.login('g','google_token'))
    print('Biometric', bio.login('b','biometric_hash'))

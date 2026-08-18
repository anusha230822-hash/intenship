from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def login(self, user, credential):
        pass

    @abstractmethod
    def logout(self, user):
        pass

class PasswordAuth(Authentication):
    def __init__(self, store):
        self.store = store
    def login(self, user, credential):
        return self.store.get(user) == credential
    def logout(self, user):
        return f"{user} logged out"

class OTPAuth(Authentication):
    def __init__(self, valid_otps):
        self.valid_otps = valid_otps
    def login(self, user, credential):
        return credential in self.valid_otps
    def logout(self, user):
        return f"{user} logged out"

if __name__ == "__main__":
    p = PasswordAuth({'alice':'pass123'})
    o = OTPAuth({'9999'})
    print(p.login('alice','pass123'))
    print(o.login('bob','9999'))
    print(p.logout('alice'))
    print(o.logout('bob'))

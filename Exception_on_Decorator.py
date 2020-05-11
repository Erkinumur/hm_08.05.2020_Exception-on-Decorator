from functools import wraps


class User:
    def balance_exc_decorator(func):
        @wraps(func)
        def wrapper(self):
            try:
                func(self)
            except:
                raise Exception('No username defined!')
        return wrapper

    def password_exc_decorator(func):
        @wraps(func)
        def wrapper(self, new_pass):
            try:
                func(self, new_pass)
            except:
                raise Exception("No password to change!")
        return wrapper

    @balance_exc_decorator
    def get_account_balance(self):
        return self._balance

    @password_exc_decorator
    def change_password(self, new_pass):
        print(f'Ваш старый пароль "{self._password}" был заменен!')
        self._password = new_pass


u = User()
u.change_password('12345')

    

    
from functools import wraps


exc = ''
class User:
    def exc_decorator(func):
        @wraps(func)
        def wrapper(self, new_pass):
            try:
                func(self, new_pass)
            except:
                raise Exception(exc)
        return wrapper

    @balance_exc_decorator
    def get_account_balance(self):
        global exc
        exc = 'No username defined!'
        
        return self._balance

    @password_exc_decorator
    def change_password(self, new_pass):
        global exc
        exc = 'No password to change!'
        print(f'Ваш старый пароль "{self._password}" был заменен!')
        self._password = new_pass


u = User()
u.change_password('12345')

    

    
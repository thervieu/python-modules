class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

    def iscorrupt(self):
        dict_ = self.__dict__
        if len(dict_) % 2 == 0:
            return True
        name_ = 0
        id_ = 0
        value_ = 0

        for item in dict_:
            if item.startswith('b') or item.startswith('zip') or item.startswith('addr'):
                return True
            if item == 'name':
                name_ = 1
            if item == 'id':
                id_ = 1
            if item == 'value':
                value_ = 1
        if name_ == 0 or id_ == 0 or value_ == 0:
            return True
        return False

class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        if isinstance(account, Account) is False:
            raise TypeError('Bank: add: type must be Account')
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if len(self.account) < 2:
            return False
        if isinstance(origin, int) is False and isinstance(origin, str) is False:
            raise TypeError("Bank: transfer: origin is either the account's id or its name")
        if isinstance(dest, int) is False and isinstance(dest, str) is False:
            raise TypeError("Bank: transfer: dest is either the account's id or its name")
        if isinstance(amount, (int, float)) is False:
            raise TypeError('Bank: transfer: amount must be an int or float')
        for a in self.account:
            if origin is a.id or origin is a.name:
                or_a = a
                break
            if a == self.account[len(self.account) - 1]:
                raise ValueError('Bank: transfer: origin not in the accounts')
        for a in self.account:
            if dest is a.id or dest is a.name:
                dest_a = a
                break
            if a == self.account[len(self.account) - 1]:
                raise ValueError('Bank: transfer: origin not in the accounts')
        if amount < 0:
            raise ValueError('Bank: transfer: amount must be positive')
        if or_a.value < amount:
            return False
        if or_a.iscorrupt() or dest_a.iscorrupt():
            return False
        or_a.transfer(-amount)
        dest_a.transfer(+amount)
        return True

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """

        if isinstance(account, int) is False and isinstance(account, str) is False:
            raise TypeError("Bank: fix_account: account is either the account's id or its name")
        for i in range(len(self.account)):
            if account is self.account[i].id or account is self.account[i].name:
                nb = i
                break
            if self.account[i] == self.account[len(self.account) - 1]:
                raise ValueError('Bank: fix_account: account not in the accounts')

        del_list = []
        for item in self.account[nb].__dict__:
            if item.startswith('b') or item.startswith('zip') or item.startswith('addr'):
                del_list.append(item)

        for item in del_list:
            del self.account[nb].__dict__[item]
        if len(self.account[nb].__dict__) % 2 == 0:
            self.account[nb].__dict__['onemore'] = '111'
        self.account[nb].__dict__['name']
        self.account[nb].__dict__['id']
        self.account[nb].__dict__['value']
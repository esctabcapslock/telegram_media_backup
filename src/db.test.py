import db
if __name__ == '__main__':
    c = db.db_init()
    print(f'exists_photo zero: {db.exists_photo(c, 0,0, '1234')}')

'''

import src.db
db = src.db
c = db.db_init()
'''

from ps4b import *

c = Message('ball! car, house2 1234')


print(c.get_message_text())
print(c.get_word_lst())
print(c.apply_shift(4))
print(c.apply_shift(25))

b = PlaintextMessage('ball! car, house',4)


print(b.get_shift())
print(b.get_encryption_dict())
print(b.get_message_text_encrypted())

b.change_shift(5)

print(b.get_shift())
print(b.get_encryption_dict())
print(b.get_message_text_encrypted())

c = CiphertextMessage('gfqq! hfx, mtzyj')


print(c.decrypt_message())


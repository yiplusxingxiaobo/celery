from tasks import add,sub

add.delay(1,33)
sub.delay(88,87)
print('hello world this is a async work')

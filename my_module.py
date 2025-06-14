def test_function(content):
    print(f'This is an imported function with the parameter: {content}')

class Test:
    def __init__(self):
        self.name = 'My app'
        self.value = 12
        
    def do_something(self):
        print('Hello')
test_var = 'test'

print(__name__)
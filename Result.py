class OK:
    code: 200
    success: True
    data: []
    def __init__(self, data):
        self.code = 200
        self.success = True
        self.data = data
    def to_json(self):
        return {
            'code': self.code,
            'success': self.success,
            'data': self.data
        }
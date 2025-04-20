class MCPContext:
    def __init__(self, user_input: str):
        self.user_input = user_input
        self.schema = None
        self.query = ""
        self.result = None

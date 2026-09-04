class Run:
    ALLOWED_TRANSITIONS = {
        "PENDING": {"RUNNING"},
        "RUNNING": {"SUCCESS", "FAILED"},
        "SUCCESS": set(),
        "FAILED": set()
        }
    def __init__(self, run_id, query):
        self.run_id = run_id
        self.query = query
        self.status = "PENDING"
        self.current_stage = None
    def change_status(self, new_status):
        allowed_statuses = self.ALLOWED_TRANSITIONS[self.status]
        if not isinstance(new_status,str):
            raise TypeError("INVALID_TYPE")
        if new_status in allowed_statuses:
            self.status = new_status
        else:
            raise ValueError(f"ILLEGAL_TRANSITION ({self.status}) ---> {new_status}")
        

run = Run("123", "test")

run.change_status("RUNNING")
run.change_status("SUCCESS")

try:
    run.change_status("FAILED")
except ValueError as error:
    print(error)

print(run.status)